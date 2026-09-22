(function () {
  var KEY = 'resume-lang';
  var data = window.RESUME_DATA || {};

  function detect() {
    var tz = (Intl.DateTimeFormat().resolvedOptions().timeZone || '').toLowerCase();
    var nav = (navigator.language || '').toLowerCase();
    if (tz.indexOf('kyiv') >= 0 || tz.indexOf('kiev') >= 0 || nav.indexOf('uk') === 0) return 'uk';
    return 'en';
  }

  function tr(obj, lang) {
    return (obj && (obj[lang] || obj.en || obj.uk)) || '';
  }

  function setText(sel, value) {
    document.querySelectorAll(sel).forEach(function (el) { el.textContent = value; });
  }

  function downloads(lang) {
    var suffix = lang === 'uk' ? '.uk' : '';
    var map = { '[data-dl-pdf]': 'pdf', '[data-dl-docx]': 'docx', '[data-dl-md]': 'md' };
    Object.keys(map).forEach(function (sel) {
      document.querySelectorAll(sel).forEach(function (el) {
        el.setAttribute('href', './resume' + suffix + '.' + map[sel]);
      });
    });
  }

  function apply(lang) {
    try { localStorage.setItem(KEY, lang); } catch (e) {}
    document.querySelectorAll('[data-lang]').forEach(function (b) {
      b.classList.toggle('active', b.dataset.lang === lang);
    });

    var ui = data.ui || {}, sec = data.sections || {};
    setText('[data-i18n-name]', tr(data.profile && data.profile.name, lang));
    setText('[data-i18n-target-title]', tr(data.titleTextObj, lang));
    setText('[data-i18n-summary]', tr(data.summaryTextObj, lang));

    setText('[data-theme-mode="auto"]', tr(ui.auto, lang));
    setText('[data-theme-mode="light"]', tr(ui.light, lang));
    setText('[data-theme-mode="dark"]', tr(ui.dark, lang));
    setText('[data-lang="uk"]', tr(ui.ua, lang));
    setText('[data-lang="en"]', tr(ui.en, lang));
    setText('[data-i18n-btn-pdf]', tr(ui.pdf, lang));
    setText('[data-i18n-btn-word]', tr(ui.word, lang));
    setText('[data-i18n-btn-markdown]', tr(ui.markdown, lang));
    setText('[data-i18n-nav-full]', tr(ui.full, lang));
    setText('[data-i18n-nav-dotnet]', tr(ui.dotnet, lang));
    setText('[data-i18n-nav-delphi]', tr(ui.delphi, lang));
    setText('[data-i18n-nav-web]', tr(ui.web, lang));
    setText('[data-i18n-nav-ai]', tr(ui.ai, lang));
    setText('[data-i18n-profiles-hint]', tr(ui.profiles_hint, lang));
    setText('[data-i18n-present]', tr(ui.present, lang));
    setText('[data-i18n-earlier]', tr(ui.earlier, lang));

    setText('[data-i18n-section-summary_cards]', tr(sec.summary_cards, lang));
    setText('[data-i18n-section-stack]', tr(sec.stack, lang));
    setText('[data-i18n-section-strengths]', tr(sec.strengths, lang));
    setText('[data-i18n-section-education]', tr(sec.education, lang));
    setText('[data-i18n-section-projects]', tr(sec.projects, lang));
    setText('[data-i18n-section-details]', tr(sec.details, lang));
    setText('[data-i18n-section-domain]', tr(sec.domain, lang));
    setText('[data-i18n-section-languages]', tr(sec.languages, lang));
    setText('[data-i18n-section-side]', tr(sec.side, lang));

    document.querySelectorAll('[data-uk][data-en]').forEach(function (el) {
      el.textContent = lang === 'uk' ? el.dataset.uk : el.dataset.en;
    });

    downloads(lang);
    document.documentElement.lang = lang;
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('[data-lang]').forEach(function (b) {
      b.addEventListener('click', function () { apply(b.dataset.lang); });
    });
    var saved = null;
    try { saved = localStorage.getItem(KEY); } catch (e) {}
    apply(saved || detect());
  });
})();
