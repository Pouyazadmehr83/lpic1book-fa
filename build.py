#!/usr/bin/env python3
import os
import re
import glob
import shutil
import json
import markdown
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.join(BASE_DIR, 'persian-book', 'content')
SITE_DIR = os.path.join(BASE_DIR, 'persian-book', 'site')
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')


TOPIC_INFO = {
    'intro': {'title': 'مقدمه و شروع کار', 'exam': 'عمومی', 'badge': 'پیش‌نیاز'},
    '101': {'title': 'مبحث ۱۰۱: معماری سیستم (System Architecture)', 'exam': 'آزمون ۱۰۱', 'badge': 'مبحث ۱۰۱'},
    '102': {'title': 'مبحث ۱۰۲: نصب لینوکس و مدیریت بسته‌ها (Package Management)', 'exam': 'آزمون ۱۰۱', 'badge': 'مبحث ۱۰۲'},
    '103': {'title': 'مبحث ۱۰۳: دستورات گنو و یونیکس (GNU & Unix Commands)', 'exam': 'آزمون ۱۰۱', 'badge': 'مبحث ۱۰۳'},
    '104': {'title': 'مبحث ۱۰۴: دیسک‌ها، سیستم‌فایل‌ها و سلسله‌مراتب (Devices & Filesystems)', 'exam': 'آزمون ۱۰۱', 'badge': 'مبحث ۱۰۴'},
    '105': {'title': 'مبحث ۱۰۵: پوسته‌ها و اسکریپت‌نویسی (Shells & Scripting)', 'exam': 'آزمون ۱۰۲', 'badge': 'مبحث ۱۰۵'},
    '106': {'title': 'مبحث ۱۰۶: رابط‌های کاربری و دسکتاپ (User Interfaces & Desktops)', 'exam': 'آزمون ۱۰۲', 'badge': 'مبحث ۱۰۶'},
    '107': {'title': 'مبحث ۱۰۷: وظایف مدیریتی سیستم (Administrative Tasks)', 'exam': 'آزمون ۱۰۲', 'badge': 'مبحث ۱۰۷'},
    '108': {'title': 'مبحث ۱۰۸: سرویس‌های اساسی سیستم (Essential Services)', 'exam': 'آزمون ۱۰۲', 'badge': 'مبحث ۱۰۸'},
    '109': {'title': 'مبحث ۱۰۹: مبانی شبکه (Networking Fundamentals)', 'exam': 'آزمون ۱۰۲', 'badge': 'مبحث ۱۰۹'},
    '110': {'title': 'مبحث ۱۱۰: امنیت سیستم (Security)', 'exam': 'آزمون ۱۰۲', 'badge': 'مبحث ۱۱۰'},
}

def parse_frontmatter(content):
    meta = {}
    lines = content.splitlines()
    body_start = 0
    in_fm = True
    for i, line in enumerate(lines):
        if in_fm:
            if ': ' in line and i < 15:
                k, v = line.split(': ', 1)
                meta[k.strip().lower()] = v.strip()
                body_start = i + 1
            elif line.strip() == '':
                body_start = i + 1
                break
            else:
                break
    body = '\n'.join(lines[body_start:])
    return meta, body

def get_group_key(sortorder, filename):
    if sortorder in ['010', '020'] or filename.startswith('000'):
        return 'intro'
    prefix = filename[:3]
    if prefix in TOPIC_INFO:
        return prefix
    return 'intro'

def clean_html(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')

    # Code blocks
    for pre in soup.find_all('pre'):
        pre['dir'] = 'ltr'
        pre['class'] = pre.get('class', []) + ['code-block']
        wrapper = soup.new_tag('div', attrs={'class': 'code-wrapper', 'dir': 'ltr'})
        
        header = soup.new_tag('div', attrs={'class': 'code-header'})
        label = soup.new_tag('span', attrs={'class': 'code-label'})
        label.string = 'دستور / کد ترمینال'
        copy_btn = soup.new_tag('button', attrs={'class': 'copy-btn', 'type': 'button', 'onclick': 'copyCode(this)'})
        copy_btn.string = 'کپی کد'
        
        header.append(label)
        header.append(copy_btn)
        
        pre.wrap(wrapper)
        wrapper.insert(0, header)

    # Inline code
    for code in soup.find_all('code'):
        if code.parent and code.parent.name != 'pre':
            code['dir'] = 'ltr'
            code['class'] = code.get('class', []) + ['inline-code']
            bdi = soup.new_tag('bdi')
            code.wrap(bdi)

    # YouTube iframes
    for iframe in soup.find_all('iframe'):
        wrapper = soup.new_tag('div', attrs={'class': 'video-container'})
        iframe.wrap(wrapper)
        iframe['loading'] = 'lazy'

    # Images
    for img in soup.find_all('img'):
        img['class'] = img.get('class', []) + ['content-img', 'img-fluid']
        src = img.get('src', '')
        if src.startswith('/images/'):
            img['src'] = '.' + src
        elif src.startswith('images/'):
            img['src'] = './' + src

    # Blockquotes
    for bq in soup.find_all('blockquote'):
        bq['class'] = bq.get('class', []) + ['callout-box']

    # Tables
    for table in soup.find_all('table'):
        table['class'] = table.get('class', []) + ['table', 'table-styled']
        tbl_wrapper = soup.new_tag('div', attrs={'class': 'table-responsive'})
        table.wrap(tbl_wrapper)

    return str(soup)

def generate_sidebar_html(chapters_by_group, current_url):
    html = []
    exams = [
        ('مقدمه و شروع', ['intro']),
        ('آزمون ۱۰۱ (LPIC-1 Exam 101)', ['101', '102', '103', '104']),
        ('آزمون ۱۰۲ (LPIC-1 Exam 102)', ['105', '106', '107', '108', '109', '110']),
    ]
    
    for exam_title, group_keys in exams:
        html.append('<div class="sidebar-section">')
        html.append(f'<div class="sidebar-section-title">{exam_title}</div>')
        
        for gkey in group_keys:
            if gkey not in chapters_by_group:
                continue
            group_chapters = chapters_by_group[gkey]
            group_info = TOPIC_INFO.get(gkey, {'title': gkey, 'badge': ''})
            
            is_group_active = any(c['url'] == current_url for c in group_chapters)
            open_attr = 'open' if is_group_active or gkey == 'intro' else ''
            
            html.append(f'<details class="sidebar-group" {open_attr}>')
            html.append(f'<summary class="sidebar-group-title">{group_info["title"]}</summary>')
            html.append('<ul class="sidebar-list">')
            
            for ch in group_chapters:
                active_class = 'active' if ch['url'] == current_url else ''
                weight_tag = f'<span class="ch-weight" title="وزن در آزمون">{ch["weight"]}</span>' if ch.get('weight') else ''
                html.append(f'<li class="sidebar-item {active_class}"><a href="{ch["url"]}" class="sidebar-link"><span class="ch-title">{ch["title"]}</span>{weight_tag}</a></li>')
                
            html.append('</ul>')
            html.append('</details>')
            
        html.append('</div>')
        
    html.append('<div class="sidebar-section">')
    html.append('<div class="sidebar-section-title">صفحات تکمیلی</div>')
    html.append('<ul class="sidebar-list">')
    html.append(f'<li class="sidebar-item {"active" if current_url == "index.html" else ""}"><a href="index.html" class="sidebar-link">صفحه اصلی کتاب</a></li>')
    html.append(f'<li class="sidebar-item {"active" if current_url == "support.html" else ""}"><a href="support.html" class="sidebar-link">حمایت از جادی (Donate)</a></li>')
    html.append('</ul>')
    html.append('</div>')
    
    return '\n'.join(html)

def build_site():
    os.makedirs(SITE_DIR, exist_ok=True)
    os.makedirs(os.path.join(SITE_DIR, 'images'), exist_ok=True)
    
    # Copy static assets (CSS, JS)
    if os.path.exists(STATIC_DIR):
        for item in glob.glob(os.path.join(STATIC_DIR, '*')):
            if os.path.isfile(item):
                shutil.copy(item, SITE_DIR)

    # Copy images
    img_dir = os.path.join(CONTENT_DIR, 'images')
    if os.path.exists(img_dir):
        for item in glob.glob(os.path.join(img_dir, '*')):
            if os.path.isfile(item):
                shutil.copy(item, os.path.join(SITE_DIR, 'images'))
            elif os.path.isdir(item):
                dest = os.path.join(SITE_DIR, 'images', os.path.basename(item))
                if os.path.exists(dest):
                    shutil.rmtree(dest)
                shutil.copytree(item, dest)


    # Read templates
    with open(os.path.join(TEMPLATES_DIR, 'chapter.html'), 'r', encoding='utf-8') as f:
        chapter_template = f.read()
    with open(os.path.join(TEMPLATES_DIR, 'index.html'), 'r', encoding='utf-8') as f:
        index_template = f.read()
    with open(os.path.join(TEMPLATES_DIR, 'support.html'), 'r', encoding='utf-8') as f:
        support_template = f.read()

    files = sorted(glob.glob(os.path.join(CONTENT_DIR, '*.md')))
    chapters = []

    for fpath in files:
        fname = os.path.basename(fpath)
        if fname.lower() in ['readme.md', 'content.md', 'summary.md']:
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            raw = f.read()
        meta, body = parse_frontmatter(raw)
        
        sortorder = meta.get('sortorder', '999').zfill(3)
        title = meta.get('title', fname.replace('.md', ''))
        
        weight = ''
        w_match = re.search(r'\*(?:Weight|وزن)\s*:\s*(\d+)\*', body, re.IGNORECASE)
        if w_match:
            weight = f'وزن: {w_match.group(1)}'
            
        html_fname = fname.replace('.md', '.html')
        group_key = get_group_key(sortorder, fname)
        
        chapters.append({
            'filename': fname,
            'url': html_fname,
            'title': title,
            'sortorder': sortorder,
            'group_key': group_key,
            'weight': weight,
            'summary': meta.get('summary', ''),
            'raw_body': body,
            'fpath': fpath
        })

    chapters.sort(key=lambda c: c['sortorder'])

    chapters_by_group = {}
    for ch in chapters:
        g = ch['group_key']
        chapters_by_group.setdefault(g, []).append(ch)

    search_index = []
    for ch in chapters:
        search_index.append({
            'title': ch['title'],
            'url': ch['url'],
            'group': TOPIC_INFO.get(ch['group_key'], {}).get('title', ''),
            'exam': TOPIC_INFO.get(ch['group_key'], {}).get('exam', ''),
            'weight': ch['weight']
        })
        
    with open(os.path.join(SITE_DIR, 'search_index.json'), 'w', encoding='utf-8') as f:
        json.dump(search_index, f, ensure_ascii=False, indent=2)

    total_chapters = len(chapters)
    print(f"Building site for {total_chapters} chapters...")

    for idx, ch in enumerate(chapters):
        prev_ch = chapters[idx - 1] if idx > 0 else None
        next_ch = chapters[idx + 1] if idx < total_chapters - 1 else None

        md_html = markdown.markdown(
            ch['raw_body'],
            extensions=['extra', 'tables', 'fenced_code', 'toc']
        )
        content_html = clean_html(md_html)
        
        sidebar_html = generate_sidebar_html(chapters_by_group, ch['url'])
        group_info = TOPIC_INFO.get(ch['group_key'], {'title': ch['group_key'], 'exam': 'LPIC-1', 'badge': ''})

        pager_html = '<div class="chapter-pager">'
        if prev_ch:
            pager_html += f'<a href="{prev_ch["url"]}" class="pager-btn prev-btn"><span class="pager-hint">← درس قبلی</span><span class="pager-title">{prev_ch["title"]}</span></a>'
        else:
            pager_html += '<div class="pager-empty"></div>'
            
        if next_ch:
            pager_html += f'<a href="{next_ch["url"]}" class="pager-btn next-btn"><span class="pager-hint">درس بعدی →</span><span class="pager-title">{next_ch["title"]}</span></a>'
        else:
            pager_html += '<div class="pager-empty"></div>'
        pager_html += '</div>'

        weight_badge = f'<span class="meta-item weight-tag">{ch["weight"]}</span>' if ch.get('weight') else ''

        page_out = chapter_template
        page_out = page_out.replace('{{TITLE}}', ch['title'])
        page_out = page_out.replace('{{EXAM}}', group_info.get('exam', 'LPIC-1'))
        page_out = page_out.replace('{{TOPIC_TITLE}}', group_info.get('title', ''))
        page_out = page_out.replace('{{TOPIC_BADGE}}', group_info.get('badge', ''))
        page_out = page_out.replace('{{WEIGHT_BADGE}}', weight_badge)
        page_out = page_out.replace('{{SIDEBAR_HTML}}', sidebar_html)
        page_out = page_out.replace('{{CONTENT_HTML}}', content_html)
        page_out = page_out.replace('{{PAGER_HTML}}', pager_html)

        with open(os.path.join(SITE_DIR, ch['url']), 'w', encoding='utf-8') as f:
            f.write(page_out)

    # Build index.html
    generate_home_page(index_template, chapters_by_group)
    # Build support.html
    generate_support_page(support_template, chapters_by_group)

    print("Site build finished successfully!")

def generate_home_page(index_template, chapters_by_group):
    sidebar_html = generate_sidebar_html(chapters_by_group, 'index.html')
    
    home_src = os.path.join(CONTENT_DIR, 'pages', 'home.md')
    home_body = ""
    if os.path.exists(home_src):
        with open(home_src, 'r', encoding='utf-8') as f:
            _, home_body = parse_frontmatter(f.read())
            
    home_html = markdown.markdown(home_body, extensions=['extra']) if home_body else ""
    home_html = clean_html(home_html)

    cards_101 = []
    for gkey in ['101', '102', '103', '104']:
        if gkey in chapters_by_group:
            chs = chapters_by_group[gkey]
            info = TOPIC_INFO[gkey]
            first_url = chs[0]['url']
            lessons_html = ''.join([f'<li><a href="{c["url"]}">{c["title"]}</a></li>' for c in chs[:4]])
            more_html = f'<li class="more-link"><a href="{first_url}">مشاهده تمام {len(chs)} بخش این مبحث ←</a></li>' if len(chs) > 4 else ''
            cards_101.append(f'''
            <div class="topic-card">
                <div class="topic-card-header">
                    <span class="topic-num">{info["badge"]}</span>
                    <h3>{info["title"]}</h3>
                </div>
                <ul class="topic-card-lessons">
                    {lessons_html}
                    {more_html}
                </ul>
            </div>
            ''')

    cards_102 = []
    for gkey in ['105', '106', '107', '108', '109', '110']:
        if gkey in chapters_by_group:
            chs = chapters_by_group[gkey]
            info = TOPIC_INFO[gkey]
            first_url = chs[0]['url']
            lessons_html = ''.join([f'<li><a href="{c["url"]}">{c["title"]}</a></li>' for c in chs[:4]])
            more_html = f'<li class="more-link"><a href="{first_url}">مشاهده تمام {len(chs)} بخش این مبحث ←</a></li>' if len(chs) > 4 else ''
            cards_102.append(f'''
            <div class="topic-card">
                <div class="topic-card-header">
                    <span class="topic-num">{info["badge"]}</span>
                    <h3>{info["title"]}</h3>
                </div>
                <ul class="topic-card-lessons">
                    {lessons_html}
                    {more_html}
                </ul>
            </div>
            ''')

    page_out = index_template
    page_out = page_out.replace('{{SIDEBAR_HTML}}', sidebar_html)
    page_out = page_out.replace('{{HOME_INTRO_HTML}}', home_html)
    page_out = page_out.replace('{{CARDS_101}}', ''.join(cards_101))
    page_out = page_out.replace('{{CARDS_102}}', ''.join(cards_102))

    with open(os.path.join(SITE_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(page_out)

def generate_support_page(support_template, chapters_by_group):
    sidebar_html = generate_sidebar_html(chapters_by_group, 'support.html')
    sup_src = os.path.join(CONTENT_DIR, 'pages', 'support.md')
    sup_body = ""
    if os.path.exists(sup_src):
        with open(sup_src, 'r', encoding='utf-8') as f:
            _, sup_body = parse_frontmatter(f.read())
            
    content_html = clean_html(markdown.markdown(sup_body, extensions=['extra'])) if sup_body else ""
    
    page_out = support_template
    page_out = page_out.replace('{{SIDEBAR_HTML}}', sidebar_html)
    page_out = page_out.replace('{{CONTENT_HTML}}', content_html)

    with open(os.path.join(SITE_DIR, 'support.html'), 'w', encoding='utf-8') as f:
        f.write(page_out)

if __name__ == '__main__':
    build_site()
