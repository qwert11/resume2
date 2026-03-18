from pathlib import Path
import yaml

def load_yaml(path):
    with open(path,'r',encoding='utf-8') as f:
        return yaml.safe_load(f)

def has_any_tag(item_tags,target_tags):
    return bool(set(item_tags or []).intersection(set(target_tags or [])))

def filter_items(items,target_tags,full_mode=False):
    if full_mode:
        return items
    return [x for x in items if has_any_tag(x.get('tags',[]),target_tags)]

def ensure_dir(path):
    Path(path).mkdir(parents=True,exist_ok=True)
