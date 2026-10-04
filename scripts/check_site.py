#!/usr/bin/env python3
"""Check the built site in _site/: structure rules, internal links and anchors.

Rules come from the blog's design system: every reader-facing page carries the site header
with .nav-brand linking to "/", and the theme toggle. Exit status 1 if anything fails.
"""
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote

OUT = Path(__file__).resolve().parent.parent / '_site'


class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title, self._in_title = '', False
        self.ids, self.hrefs, self.srcs = set(), [], []
        self.h1 = 0
        self.brand_href = None
        self.toggle = False
        self.canonical = self.desc = None
        self.lang = None
        self.has_main = False
        self.table_rows = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.add(a['id'])
        if tag == 'html':
            self.lang = a.get('lang')
        if tag == 'title':
            self._in_title = True
        if tag == 'h1':
            self.h1 += 1
        if tag == 'main':
            self.has_main = True
        if tag == 'a':
            if 'nav-brand' in (a.get('class') or '').split():
                self.brand_href = a.get('href')
            if a.get('href'):
                self.hrefs.append(a['href'])
        if tag in ('script', 'link') and (a.get('src') or a.get('href')):
            (self.srcs if tag == 'script' else self.hrefs).append(a.get('src') or a.get('href'))
        if tag == 'button' and a.get('id') == 'theme-toggle':
            self.toggle = True
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonical = a.get('href')
        if tag == 'meta' and a.get('name') == 'description':
            self.desc = a.get('content')
        if tag == 'tr' and a.get('data-lic'):
            self.table_rows += 1

    def handle_endtag(self, tag):
        if tag == 'title':
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


pages = {}
for f in sorted(OUT.rglob('*.html')):
    p = P()
    p.feed(f.read_text(encoding='utf-8'))
    pages[f] = p

errors = []
titles = {}
for f, p in pages.items():
    name = f.relative_to(OUT).as_posix()
    if p.brand_href != '/':
        errors.append(f'{name}: .nav-brand must link to "/" (found {p.brand_href!r})')
    if not p.toggle:
        errors.append(f'{name}: theme toggle button missing')
    if p.h1 != 1:
        errors.append(f'{name}: expected one <h1>, found {p.h1}')
    if not p.has_main:
        errors.append(f'{name}: no <main>')
    if p.lang != 'en':
        errors.append(f'{name}: <html lang> missing')
    if not p.title.strip():
        errors.append(f'{name}: empty <title>')
    if not p.desc:
        errors.append(f'{name}: no meta description')
    if not (p.canonical or '').startswith('https://tech.anujsadani.in/awesome-decision-models/'):
        errors.append(f'{name}: canonical URL wrong: {p.canonical!r}')
    titles.setdefault(p.title, []).append(name)

for t, names in titles.items():
    if len(names) > 1:
        errors.append(f'duplicate title {t!r}: {names}')

checked = 0
for f, p in pages.items():
    name = f.relative_to(OUT).as_posix()
    for href in p.hrefs + p.srcs:
        if href.startswith(('http://', 'https://', 'mailto:', '//')) or href == '/':
            continue
        checked += 1
        path, _, anchor = href.partition('#')
        if path == '':
            target = f
        else:
            target = (f.parent / unquote(path)).resolve()
            if target.is_dir():
                target = target / 'index.html'
        if not target.exists():
            errors.append(f'{name}: broken link {href!r}')
            continue
        if anchor and target.suffix == '.html':
            tp = pages.get(target) or pages.get(Path(str(target)))
            if tp is None:
                for k, v in pages.items():
                    if k.resolve() == target.resolve():
                        tp = v
                        break
            if tp is not None and anchor not in tp.ids:
                errors.append(f'{name}: anchor #{anchor} not found in {target.relative_to(OUT.resolve()).as_posix()}')

sitemap = (OUT / 'sitemap.xml').read_text(encoding='utf-8')
for f in pages:
    rel = f.relative_to(OUT).parent.as_posix()
    loc = 'https://tech.anujsadani.in/awesome-decision-models/' + ('' if rel == '.' else rel + '/')
    if loc not in sitemap:
        errors.append(f'sitemap missing {loc}')

tools_page = next((p for f, p in pages.items() if f.relative_to(OUT).as_posix() == 'tools/index.html'), None)
if tools_page is None or tools_page.table_rows < 100:
    errors.append('tools page missing or has too few rows')

print(f'{len(pages)} pages, {checked} internal links checked, tools rows: {tools_page.table_rows if tools_page else 0}')
if errors:
    print(f'{len(errors)} problem(s):')
    for e in errors:
        print('  -', e)
    sys.exit(1)
print('OK')
