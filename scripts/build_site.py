#!/usr/bin/env python3
"""Build the static website from the repository's Markdown.

Output goes to _site/ (not committed; the GitHub Actions workflow builds and deploys it).
The Markdown files stay the single source of truth. Run:  python scripts/build_site.py
"""
import datetime
import html
import json
import os
import re
import shutil
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / '_site'
SITE = 'https://tech.anujsadani.in/awesome-decision-models'
REPO = 'https://github.com/asadani/awesome-decision-models'
BOOK = 'https://tech.anujsadani.in/decision-models-guide/'
BLOG = 'https://tech.anujsadani.in/'
PERSON = 'https://anujsadani.in/#person'

# --------------------------------------------------------------------------- facts from the repo


def read(p):
    return (ROOT / p).read_text(encoding='utf-8')


README = read('README.md')
m = re.search(r'Last fact-checked: \*\*([^*]+)\*\*', README)
CHECKED_TEXT = m.group(1).strip() if m else 'unknown date'
try:
    CHECKED_ISO = datetime.datetime.strptime(CHECKED_TEXT, '%d %b %Y').date().isoformat()
except ValueError:
    CHECKED_ISO = datetime.date.today().isoformat()

# --------------------------------------------------------------------------- markdown


def gh_slug(value, sep='-'):
    """Heading ids that match GitHub's anchors, so links written for the README keep working."""
    v = value.strip().lower()
    v = re.sub(r'[^\w\s-]', '', v, flags=re.UNICODE)
    return re.sub(r'\s', '-', v)


def new_md():
    return markdown.Markdown(
        extensions=['tables', 'toc', 'fenced_code', 'sane_lists'],
        extension_configs={'toc': {'slugify': gh_slug}},
        output_format='html',
    )


CATEGORY_FILES = sorted((ROOT / 'categories').glob('*.md'))
ROUTES = {'README.md': '', 'LEARN.md': 'learn', 'models.md': 'models', 'benchmarks.md': 'benchmarks',
          'papers.md': 'papers', 'GAPS.md': 'gaps', 'REFERENCES.md': 'references', 'CONTRIBUTING.md': 'contributing'}
for f in CATEGORY_FILES:
    ROUTES[f'categories/{f.name}'] = f'category/{f.stem}'


def rel(from_slug, to_slug, anchor=''):
    depth = from_slug.count('/') + 1 if from_slug else 0
    prefix = '../' * depth if depth else './'
    target = prefix + (to_slug + '/' if to_slug else '')
    return target + (('#' + anchor) if anchor else '')


def rewrite_links(body, from_slug, from_file):
    base_dir = os.path.dirname(from_file)

    def fix(match):
        href = match.group(1)
        if href.startswith(('http://', 'https://')):
            return f'href="{href}" rel="noopener"'
        if href.startswith(('#', 'mailto:')):
            return f'href="{href}"'
        path, _, anchor = href.partition('#')
        norm = os.path.normpath(os.path.join(base_dir, path)).replace('\\', '/')
        if norm in ROUTES:
            return f'href="{rel(from_slug, ROUTES[norm], anchor)}"'
        return f'href="{REPO}/blob/main/{norm}" rel="noopener"'

    return re.sub(r'href="([^"]*)"', fix, body)


def decorate(body):
    # self-linking headings
    body = re.sub(r'<h([23]) id="([^"]+)">(.*?)</h\1>',
                  lambda mm: f'<h{mm.group(1)} id="{mm.group(2)}">{mm.group(3)}'
                             f'<a class="anchor" href="#{mm.group(2)}" aria-label="Link to this section">#</a></h{mm.group(1)}>',
                  body, flags=re.S)
    # scrollable, focusable tables
    body = body.replace('<table>', '<div class="data-table" role="region" aria-label="Table" tabindex="0"><table>')
    body = body.replace('</table>', '</table></div>')
    return body


def render(text, from_slug, from_file):
    md = new_md()
    out = md.convert(text)
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', out, flags=re.S)
    title = html.unescape(re.sub(r'<[^>]+>', '', h1.group(1))).strip() if h1 else ''
    out = re.sub(r'<h1[^>]*>.*?</h1>', '', out, count=1, flags=re.S)
    p1 = re.search(r'<p>(.*?)</p>', out, flags=re.S)
    first = html.unescape(re.sub(r'<[^>]+>', '', p1.group(1))).strip() if p1 else ''
    return decorate(rewrite_links(out, from_slug, from_file)), title, re.sub(r'\s+', ' ', first)


def inline(text, from_slug='tools', from_file='README.md'):
    md = new_md()
    out = md.convert(text).strip()
    out = re.sub(r'^<p>|</p>$', '', out)
    return rewrite_links(out, from_slug, from_file)


# --------------------------------------------------------------------------- tools table

LIC_GROUP = {'MIT': 'permissive', 'Apache-2.0': 'permissive', 'CC-BY-4.0': 'permissive', 'BSD-3-Clause': 'permissive',
             'AGPL-3.0': 'copyleft', 'GPL-3.0': 'copyleft', 'LGPL-3.0': 'copyleft',
             'none stated': 'none', 'unclear': 'unclear', 'n/a': 'na'}
LIC_LABEL = {'permissive': 'Permissive (MIT, Apache, CC BY)', 'copyleft': 'Copyleft (GPL family)',
             'none': 'No license stated', 'unclear': 'License unclear', 'na': 'Not a code repo'}
ROW = re.compile(r'^\| \[([^\]]+)\]\(([^)]+)\)((?: \(`[^`]*`\))?) \| (.*) \| ([^|]+) \|$')


def parse_tools():
    tools = []
    for f in CATEGORY_FILES:
        cat_title, section, in_table = '', '', False
        for line in f.read_text(encoding='utf-8').split('\n'):
            if line.startswith('# '):
                cat_title = line[2:].strip()
            elif line.startswith('## '):
                section = line[3:].strip()
                in_table = False
            if line.strip() == '| Tool | What it does | License |':
                in_table = True
                continue
            if in_table and not line.startswith('|'):
                in_table = False
            if in_table:
                r = ROW.match(line)
                if r:
                    name, url, extra, desc, lic = r.groups()
                    tools.append(dict(name=name, url=url, extra=extra.strip(), desc=desc, lic=lic.strip(),
                                      cat=cat_title, section=section, slug=f'category/{f.stem}'))
    return tools


TOOLS = parse_tools()

# --------------------------------------------------------------------------- page chrome

NAV = [('', 'Home'), ('learn', 'Learn'), ('models', 'Models'), ('tools', 'Tools'), ('benchmarks', 'Benchmarks'),
       ('papers', 'Papers'), ('gaps', 'Gaps'), ('references', 'References')]
PAGES_BUILT = []


def esc(s):
    return html.escape(s, quote=True)


def chrome(slug, title, eyebrow, deck, body, wide=False, description='', scripts='', home=False):
    prefix = '../' * (slug.count('/') + 1) if slug else './'
    url = f'{SITE}/{slug + "/" if slug else ""}'
    page_title = (f'{title} · Awesome Decision Models' if not home else
                  'Awesome Decision Models: typed decision models, benchmarks, papers and tools')
    desc = (description or deck or title)[:300]
    current = slug if slug in dict(NAV) else ('tools' if slug.startswith('category/') else slug)
    subnav = ''.join(
        '<a href="%s"%s>%s</a>' % (rel(slug, s), ' aria-current="page"' if s == current else '', label) for s, label in NAV)
    ld = {
        '@context': 'https://schema.org',
        '@type': 'WebSite' if home else 'WebPage',
        '@id': url + '#page' if not home else SITE + '/#website',
        'url': url, 'name': page_title, 'description': desc, 'inLanguage': 'en',
        'dateModified': CHECKED_ISO,
        'license': 'https://creativecommons.org/licenses/by/4.0/',
        'author': {'@type': 'Person', '@id': PERSON, 'name': 'Anuj Sadani', 'url': 'https://anujsadani.in/'},
        'isPartOf': {'@id': BLOG + '#blog'} if home else {'@id': SITE + '/#website'},
    }
    meta_line = f'<span>Fact-checked {esc(CHECKED_TEXT)}</span><span class="hero-meta-sep">/</span><span>CC BY 4.0</span>'
    hero = (f'<header class="hero"><div class="hero-eyebrow">{esc(eyebrow)}</div><h1>{esc(title)}</h1>'
            f'{f"<p class=hero-deck>{esc(deck)}</p>" if deck else ""}<div class="hero-meta">{meta_line}</div></header>')
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(page_title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="author" content="Anuj Sadani">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="Awesome Decision Models">
<meta property="og:title" content="{esc(page_title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="https://tech.anujsadani.in/assets/profile-pic.png">
<meta name="twitter:card" content="summary">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<script>
  (function () {{
    try {{
      var saved = localStorage.getItem('theme');
      var theme = saved || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
      document.documentElement.setAttribute('data-theme', theme);
    }} catch (e) {{}}
  }})();
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<nav class="top">
  <a class="nav-brand" href="/">Anuj Sadani | Tech</a>
  <div class="nav-right">
    <span class="nav-tag">Awesome Decision Models</span>
    <button class="theme-toggle" id="theme-toggle" type="button" aria-label="Toggle dark mode" title="Toggle dark mode">
      <span class="theme-icon-moon" aria-hidden="true">&#9790;</span>
      <span class="theme-icon-sun" aria-hidden="true">&#9728;</span>
    </button>
  </div>
</nav>
<nav class="sub" aria-label="Sections">{subnav}</nav>
<main id="main" class="page-wrap{" wide" if wide else ""}">
{hero}
<div class="prose">
{body}
</div>
</main>
<footer>
  <span>Awesome Decision Models &middot; text licensed <a href="{rel(slug, 'references')}#this-repositorys-own-license">CC BY 4.0</a> &middot; fact-checked {esc(CHECKED_TEXT)}</span>
  <div class="footer-refs">
    <a href="{REPO}" rel="noopener">GitHub</a>
    <a href="{BOOK}" rel="noopener">The book</a>
    <a href="{BLOG}" rel="noopener">Blog</a>
    <a href="{rel(slug, 'references')}">Credits</a>
  </div>
</footer>
<script>
  (function () {{
    var btn = document.getElementById('theme-toggle');
    if (!btn) return;
    btn.addEventListener('click', function () {{
      var cur = document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
      var next = cur === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      try {{ localStorage.setItem('theme', next); }} catch (e) {{}}
    }});
  }})();
</script>
{scripts}
</body>
</html>
'''
    target = OUT / slug / 'index.html' if slug else OUT / 'index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(doc, encoding='utf-8')
    PAGES_BUILT.append(slug)


# --------------------------------------------------------------------------- build pages

OUT.mkdir(parents=True, exist_ok=True)
# Clear the contents but keep the folder itself: on Windows a local dev server can hold it open.
for child in OUT.iterdir():
    shutil.rmtree(child) if child.is_dir() else child.unlink()
(OUT / 'assets').mkdir()
shutil.copy(ROOT / 'site' / 'site.css', OUT / 'assets' / 'site.css')
shutil.copy(ROOT / 'site' / 'tools.js', OUT / 'assets' / 'tools.js')
(OUT / '.nojekyll').write_text('', encoding='utf-8')

n_tools = len(TOOLS)
refs = read('REFERENCES.md')
n_papers = len(re.findall(r'^\| \[2609\.', refs, flags=re.M))
mm = re.search(r'Index of all (\d+) GitHub repositories', refs)
n_repos = int(mm.group(1)) if mm else 0

DECKS = {
    'learn': 'The best introductions, tutorials and explainers on decision models, in reading order. Each one was read before it was listed.',
    'models': 'Hosted and open-weight decision models compared, with sizes, licenses and what each source actually reports.',
    'benchmarks': 'What has been measured, by whom, and with what caveats. Almost nothing here is independently replicated.',
    'papers': f'{n_papers} September 2026 arXiv papers on typed decision models, summarized in plain language.',
    'gaps': 'What is already built, what is not, and the evidence and limits behind that answer.',
    'references': 'Credits, licenses and attribution for every source this site draws on.',
    'contributing': 'How to add models, benchmarks, papers and tools.',
}
EYEBROWS = {'learn': 'Start here', 'models': 'Models', 'benchmarks': 'Evidence', 'papers': 'Research', 'gaps': 'Analysis',
            'references': 'Credits & licenses', 'contributing': 'Contribute'}
WIDE = {'models', 'benchmarks', 'papers', 'gaps', 'references'}

# generic markdown pages
for src, slug in ROUTES.items():
    if slug == '':
        continue
    body, title, first = render(read(src), slug, src)
    if slug.startswith('category/'):
        chrome(slug, title, 'Tools by category', '', body, wide=True, description=first)
    else:
        chrome(slug, title, EYEBROWS.get(slug, ''), DECKS.get(slug, ''), body, wide=slug in WIDE,
               description=DECKS.get(slug) or first)

# tools page
cats = []
for t in TOOLS:
    if t['cat'] not in cats:
        cats.append(t['cat'])
rows = []
for t in TOOLS:
    g = LIC_GROUP.get(t['lic'], 'unclear')
    desc_html = inline(t['desc'], 'tools', 'categories/x.md')
    text = ' '.join([t['name'], t['desc'], t['cat'], t['section'], t['lic']]).lower()
    extra = f' <small>{esc(t["extra"])}</small>' if t['extra'] else ''
    rows.append(
        f'<tr data-text="{esc(text)}" data-cat="{esc(t["cat"])}" data-lic="{g}">'
        f'<td><a href="{esc(t["url"])}" rel="noopener">{esc(t["name"])}</a>{extra}</td>'
        f'<td>{desc_html}</td>'
        f'<td><a class="cat" href="{rel("tools", t["slug"])}#{gh_slug(t["section"])}">{esc(t["cat"])}</a>'
        f'<br><small class="cat">{esc(t["section"])}</small></td>'
        f'<td><span class="chip {g}">{esc(t["lic"])}</span></td></tr>')
cat_opts = ''.join(f'<option value="{esc(c)}">{esc(c)}</option>' for c in cats)
lic_opts = ''.join(f'<option value="{k}">{v}</option>' for k, v in LIC_LABEL.items())
tools_body = f'''
<p class="note">Descriptions are written in original wording from each project's own GitHub description (as of 04 Oct 2026).
The tools have not been run. The license is what GitHub reports for each repo and is not legal advice: a repo with no
license is all rights reserved by default. Sources and the full license index are on the
<a href="{rel("tools", "references")}">credits page</a>.</p>
<div class="filters">
  <div><label for="q">Search</label><input id="q" type="search" placeholder="e.g. router, browser, MCP, memory" autocomplete="off"></div>
  <div><label for="cat">Category</label><select id="cat"><option value="">All categories</option>{cat_opts}</select></div>
  <div><label for="lic">License</label><select id="lic"><option value="">Any license</option>{lic_opts}</select></div>
</div>
<p class="count" id="count" aria-live="polite">Showing {n_tools} of {n_tools} projects</p>
<div class="data-table" role="region" aria-label="Tools" tabindex="0">
<table>
<thead><tr><th>Tool</th><th>What it does</th><th>Category</th><th>License</th></tr></thead>
<tbody id="tools-body">
{chr(10).join(rows)}
</tbody>
</table>
<p class="empty" id="empty" hidden>No projects match. Try fewer words or clear a filter.</p>
</div>
'''
chrome('tools', 'Tools', 'Tools', f'{n_tools} projects built on decision models, searchable and filterable by category and license.',
       tools_body, wide=True, description=f'{n_tools} projects built on decision models, filterable by category and license.',
       scripts=f'<script src="{rel("tools", "")}assets/tools.js"></script>')

# home
sections = {}
for chunk in re.split(r'\n(?=## )', README):
    if chunk.startswith('## '):
        sections[chunk.split('\n', 1)[0][3:].strip()] = chunk
want = ['What is a decision model?', 'Suggested reading order', 'How to read the evidence in this repo', 'Related lists', 'License']
readme_md = '\n\n'.join(sections[w] for w in want if w in sections)
readme_html, _, _ = render(readme_md, '', 'README.md')

cards = [
    ('learn', 'Start here', 'Learn', 'Fourteen hand-picked introductions, tutorials and explainers, in reading order.'),
    ('models', 'Compare', 'Models', 'Hosted and open-weight decision models, with sizes, licenses and runtimes.'),
    ('tools', 'Search', 'Tools', f'{n_tools} projects you can filter by category and license.'),
    ('benchmarks', 'Evidence', 'Benchmarks', 'What has been measured, by whom, and the caveats before you quote it.'),
    ('papers', 'Research', 'Papers', f'{n_papers} arXiv papers, summarized and dated.'),
    ('gaps', 'Analysis', 'Gaps', 'What already exists, what does not, and how that was checked.'),
]
cards_html = ''.join(
    f'<a class="card" href="{rel("", s)}"><div class="card-label">{lab}</div><h3>{t}</h3><p>{d}</p></a>' for s, lab, t, d in cards)
home_body = f'''
<div class="banner"><span class="banner-badge">NEW</span>
<p>Strands Decider, Cloudflare Clef, GLiDE, Perplexity and OpenAI's Decisions API all appeared between 30 Sep and 02 Oct 2026.
Every performance claim for them is still vendor-reported. See <a href="{rel("", "benchmarks")}">benchmarks</a>.</p></div>
<div class="stats">
  <div class="stat"><b>{n_tools}</b><span>tools with licenses</span></div>
  <div class="stat"><b>{n_papers}</b><span>arXiv papers</span></div>
  <div class="stat"><b>{n_repos}</b><span>repos license-checked</span></div>
  <div class="stat"><b class="sm">{esc(CHECKED_TEXT)}</b><span>last fact-check</span></div>
</div>
<p class="stats-note">Counts as of {esc(CHECKED_TEXT)}. The category is a few weeks old and moves fast.</p>
<div class="cards-grid">{cards_html}</div>
<div class="book">
  <div><h2>Want the long version?</h2>
  <p>"Decision models: from a typed prediction to an accountable action" is a short book on what these models return, how to read the numbers, and the policy that belongs between a prediction and an action. Read it online, with narration.</p></div>
  <a class="btn" href="{BOOK}" rel="noopener">Read the book</a>
</div>
{readme_html}
'''
chrome('', 'Decision models', 'Awesome list · model-agnostic',
       f'A guide to non-generative models that return typed answers with probabilities instead of text: the models, the benchmarks and their caveats, the papers, and {n_tools} tools, each with its license.',
       home_body, wide=False, description='A model-agnostic, fact-checked guide to decision models: models, benchmarks, papers and a searchable, license-aware list of tools.',
       home=True)

# sitemap
urls = ''.join(
    f'<url><loc>{SITE}/{s + "/" if s else ""}</loc><lastmod>{CHECKED_ISO}</lastmod></url>' for s in sorted(PAGES_BUILT))
(OUT / 'sitemap.xml').write_text(
    f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n',
    encoding='utf-8')
print(f'built {len(PAGES_BUILT)} pages, {n_tools} tools, {n_papers} papers, {n_repos} repos -> {OUT}')
