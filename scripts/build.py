from pathlib import Path
import argparse, json, shutil
from jinja2 import Environment, FileSystemLoader
from docx import Document
from docx.shared import Pt
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from utils import load_yaml, filter_items, has_any_tag, ensure_dir
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'; TARGETS=ROOT/'targets'; TEMPLATES=ROOT/'templates'; ASSETS=ROOT/'assets'; OUTPUT=ROOT/'output'
FONT_REGULAR='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; FONT_BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def register_fonts():
    pdfmetrics.registerFont(TTFont('DejaVuSans', FONT_REGULAR)); pdfmetrics.registerFont(TTFont('DejaVuSans-Bold', FONT_BOLD))
def labels(profile, lang='en'):
    sec=profile['sections']; return {'projects':sec['projects'][lang],'details':sec['details'][lang],'education':sec['education'][lang]}
def wrap_lines(text,width=95):
    words=text.split(); lines=[]; cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if len(t)<=width: cur=t
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines
def build_docx(path, profile, target, experiences, projects, education, highlight):
    doc=Document(); doc.styles['Normal'].font.name='Arial'; doc.styles['Normal'].font.size=Pt(10.5)
    doc.add_heading(profile['name']['en'],0); p=doc.add_paragraph(); p.add_run(profile['titles'][target['title_key']]['en']).bold=True
    doc.add_paragraph(profile['summary'][target['summary_key']]['en']); doc.add_heading('Core stack',level=1); doc.add_paragraph(', '.join(highlight[:12]))
    doc.add_heading('Projects',level=1)
    for pr in projects:
        p=doc.add_paragraph(); p.add_run(f"{pr['name']['en']} ({pr['period']})").bold=True; doc.add_paragraph('Role: '+pr['role']['en']); doc.add_paragraph(pr['description']['en'])
    doc.add_heading('Experience',level=1)
    for ex in experiences:
        p=doc.add_paragraph(); p.add_run(f"{ex['company']['en']} | {ex['title']['en']}").bold=True; doc.add_paragraph(f"{ex['start']} - {ex['end']}")
        for b in ex['bullets']['en']: doc.add_paragraph(b, style='List Bullet')
    doc.add_heading('Education',level=1)
    for e in education: doc.add_paragraph(f"{e['specialty']['en']} — {e['institution']['en']} ({e['period']})", style='List Bullet')
    doc.save(path)
def build_pdf(path, profile, target, experiences, projects, education, highlight):
    register_fonts(); c=canvas.Canvas(str(path),pagesize=A4); width,height=A4; x=42; y=height-50
    def line(text,font='DejaVuSans',size=10,leading=14):
        nonlocal y; c.setFont(font,size)
        for ln in wrap_lines(text):
            c.drawString(x,y,ln); y-=leading
            if y<55:
                c.showPage(); y=height-50; c.setFont(font,size)
    line(profile['name']['en'],'DejaVuSans-Bold',18,22); line(profile['titles'][target['title_key']]['en'],'DejaVuSans-Bold',12,18); line(profile['summary'][target['summary_key']]['en'])
    y-=6; line('Core stack','DejaVuSans-Bold',12,18); line(', '.join(highlight[:12]))
    y-=6; line('Projects','DejaVuSans-Bold',12,18)
    for pr in projects:
        line(f"{pr['name']['en']} ({pr['period']})",'DejaVuSans-Bold',10,15); line('Role: '+pr['role']['en']); line(pr['description']['en'])
    y-=6; line('Experience','DejaVuSans-Bold',12,18)
    for ex in experiences:
        line(f"{ex['company']['en']} | {ex['title']['en']}",'DejaVuSans-Bold',10,15); line(f"{ex['start']} - {ex['end']}")
        for b in ex['bullets']['en']: line('• '+b)
    y-=6; line('Education','DejaVuSans-Bold',12,18)
    for e in education: line(f"- {e['specialty']['en']} — {e['institution']['en']} ({e['period']})")
    c.save()
def build_target(target_id):
    master=load_yaml(DATA/'master.yaml'); profile=master['profile']; experiences=load_yaml(DATA/'experience.yaml'); projects=load_yaml(DATA/'projects.yaml'); skills=load_yaml(DATA/'skills.yaml')['skills']; education=load_yaml(DATA/'education.yaml')['education']; achievements=load_yaml(DATA/'achievements.yaml')['achievements']; target=load_yaml(TARGETS/f'{target_id}.yaml')
    full_mode=target_id=='full'; tags=target['include_tags']; exp_f=filter_items(experiences,tags,full_mode); proj_f=filter_items(projects,tags,full_mode)
    highlight=[]
    for s in skills:
        if full_mode or has_any_tag(s.get('tags',[]),tags):
            if s['name'] not in highlight: highlight.append(s['name'])
    overview_points=[{'uk':'10+ років у enterprise, retail та industrial системах.','en':'10+ years in enterprise, retail, and industrial systems.'},{'uk':'Delphi desktop + .NET / ASP.NET full stack в одному профілі.','en':'Delphi desktop + .NET / ASP.NET full stack in one profile.'},{'uk':'SQL, інтеграції, audit, доступи, internal systems.','en':'SQL, integrations, audit, access control, internal systems.'},{'uk':'Legacy modernization: Delphi 6 -> Delphi 12/13.','en':'Legacy modernization: Delphi 6 -> Delphi 12/13.'}]
    out_dir=OUTPUT/target_id; ensure_dir(out_dir); root_prefix='../' if target_id!='full' else ''; assets_prefix='../' if target_id!='full' else ''; page_title=f"{profile['name']['en']} | {profile['titles'][target['title_key']]['en']}"
    js_data={'profile':profile,'sections':profile['sections'],'ui':profile['ui'],'titleTextObj':profile['titles'][target['title_key']],'summaryTextObj':profile['summary'][target['summary_key']]}
    env=Environment(loader=FileSystemLoader(str(TEMPLATES)))
    html=env.get_template('site.html.j2').render(target=target,page_title=page_title,title_text=profile['titles'][target['title_key']]['en'],name_text=profile['name']['en'],summary_text=profile['summary'][target['summary_key']]['en'],highlight_skills=highlight[:12],achievements=achievements[:4],education=education,projects=proj_f[:6],experiences=exp_f,overview_points=overview_points,root_prefix=root_prefix,assets_prefix=assets_prefix,downloads_prefix='./',js_data=json.dumps(js_data, ensure_ascii=False))
    (out_dir/'index.html').write_text(html,encoding='utf-8')
    md=env.get_template('resume.md.j2').render(profile_name=profile['name']['en'],title_text=profile['titles'][target['title_key']]['en'],summary_text=profile['summary'][target['summary_key']]['en'],projects=proj_f,experiences=exp_f,education=education,labels=labels(profile,'en'))
    (out_dir/'resume.md').write_text(md,encoding='utf-8')
    build_docx(out_dir/'resume.docx', profile, target, exp_f, proj_f, education, highlight); build_pdf(out_dir/'resume.pdf', profile, target, exp_f, proj_f, education, highlight)
def prepare_site():
    site=OUTPUT/'site'
    if site.exists(): shutil.rmtree(site)
    site.mkdir(parents=True, exist_ok=True); shutil.copytree(ASSETS, site/'assets', dirs_exist_ok=True); shutil.copytree(OUTPUT/'full', site, dirs_exist_ok=True)
    for t in ['dotnet','delphi','web']: shutil.copytree(OUTPUT/t, site/t, dirs_exist_ok=True)
def main():
    p=argparse.ArgumentParser(); p.add_argument('--target', choices=['full','dotnet','delphi','web']); p.add_argument('--all', action='store_true'); args=p.parse_args()
    if args.all:
        for t in ['full','dotnet','delphi','web']: build_target(t)
        prepare_site()
    elif args.target: build_target(args.target)
    else: raise SystemExit('Use --target or --all')
if __name__=='__main__': main()
