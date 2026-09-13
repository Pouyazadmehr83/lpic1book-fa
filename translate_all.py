#!/usr/bin/env python3
import os
import re
import sys
import glob
import json
import time
import urllib.request
import urllib.parse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, 'original-book', 'content')
DEST_DIR = os.path.join(BASE_DIR, 'persian-book', 'content')
LOG_FILE = os.path.join(BASE_DIR, 'translation.log')


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# Technical terms post-processing dictionary
GLOSSARY = [
    (r'\bاتوبوس سریال جهانی\b', 'گذرگاه سریال سراسری (USB)'),
    (r'\bاتوبوس\b(?=\s+(?:سیستم|داده|PCI|PCIe|USB|آدرس|گذرگاه))', 'گذرگاه'),
    (r'\bسیستم فایل شبه\b', 'سیستم‌فایل مجازی/شبه‌فایل (Pseudo Filesystem)'),
    (r'\bسیستم فایل\b', 'سیستم‌فایل (Filesystem)'),
    (r'\bدستگاه های ذخیره سازی انبوه\b', 'دستگاه‌های ذخیره‌سازی حجیم (Mass Storage)'),
    (r'\bفضای کاربر\b', 'فضای کاربری (User Space)'),
    (r'\bفضای هسته\b', 'فضای کرنل (Kernel Space)'),
    (r'\bهسته\b(?=\s+(?:لینوکس|کرنل))', 'کرنل/هسته'),
    (r'\bبوت لودر\b', 'بوت‌لودر (Bootloader)'),
    (r'\bنقطه اتصال\b(?=\s+(?:`/|/dev|/sys|/proc|/mnt|/media))', 'نقطه مانت (Mount Point)'),
    (r'\bدایرکتوری\b', 'دایرکتوری (پوشه)'),
    (r'\bدستگاه های کاراکتری\b', 'دستگاه‌های کاراکتری (Character Devices)'),
    (r'\bدستگاه های بلوک\b', 'دستگاه‌های بلوکی (Block Devices)'),
    (r'\bدستگاه های بلوکی\b', 'دستگاه‌های بلوکی (Block Devices)'),
    (r'\bدستگاه های جانبی\b', 'دستگاه‌های جانبی (Peripherals)'),
    (r'\bقطع درخواست\b', 'درخواست وقفه (Interrupt Request - IRQ)'),
    (r'\bزمان بندی فرآیند\b', 'زمان‌بندی فرآیندها (Process Scheduling)'),
    (r'\bحافظه پنهان\b', 'حافظه کش (Cache)'),
    (r'\bپارتیشن\b', 'پارتیشن (Partition)'),
    (r'\bمجوزهای فایل\b', 'مجوزهای دسترسی به فایل (File Permissions)'),
    (r'\bپیوند سخت\b', 'پیوند سخت (Hard Link)'),
    (r'\bپیوند نمادین\b', 'پیوند نمادین (Symbolic Link)'),
    (r'\bجدول پارتیشن\b', 'جدول پارتیشن (Partition Table)'),
    (r'\bخط فرمان\b', 'خط فرمان (Command Line)'),
    (r'\bعبارات منظم\b', 'عبارات باقاعده (Regular Expressions - Regex)'),
    (r'\bمتغیرهای محیطی\b', 'متغیرهای محیطی (Environment Variables)'),
    (r'\bمدیر بسته\b', 'مدیر بسته‌ها (Package Manager)'),
    (r'\bمخازن\b', 'مخازن نرم‌افزاری (Repositories)'),
    (r'\bوظایف زمان بندی شده\b', 'زمان‌بندی وظایف (Cron Jobs / Scheduling)'),
    (r'\bورودی استاندارد\b', 'ورودی استاندارد (Standard Input - stdin)'),
    (r'\bخروجی استاندارد\b', 'خروجی استاندارد (Standard Output - stdout)'),
    (r'\bخطای استاندارد\b', 'خطای استاندارد (Standard Error - stderr)'),
    (r'\bتغییر مسیر\b', 'ریدایرکت / تغییر مسیر (Redirection)'),
    (r'\bلوله گذاری\b', 'پایپینگ / خط لوله (Piping)'),
    (r'\bخط لوله\b', 'پایپ / لوله (Pipe)'),
]

def log(msg):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    formatted = f"[{timestamp}] {msg}"
    print(formatted)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(formatted + '\n')

def translate_chunk(text, retries=3):
    if not text.strip():
        return text
    url = 'https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=en&tl=fa&q=' + urllib.parse.quote(text)
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=20) as r:
                res = json.loads(r.read().decode())
                if isinstance(res, list) and len(res) > 0:
                    return res[0]
        except Exception as e:
            time.sleep(1 + attempt * 2)
    return text

def translate_file_content(content):
    # 1. Parse frontmatter
    lines = content.splitlines()
    body_start = 0
    in_fm = True
    fm_lines = []
    frontmatter = {}
    
    for i, line in enumerate(lines):
        if in_fm:
            if ': ' in line and i < 15:
                k, v = line.split(': ', 1)
                frontmatter[k.strip().lower()] = v.strip()
                fm_lines.append((k.strip(), v.strip()))
                body_start = i + 1
            elif line.strip() == '':
                body_start = i + 1
                break
            else:
                break
                
    body = '\n'.join(lines[body_start:])
    
    # 2. Protect blocks
    tokens = {}
    token_counter = 0

    def add_token(match, prefix):
        nonlocal token_counter
        tok = f"___{prefix}_{token_counter}___"
        token_counter += 1
        tokens[tok] = match.group(0)
        return tok

    # Protect code blocks (fenced with 3 or more backticks or tildes)
    body = re.sub(r'(`{3,})[^\n]*\n[\s\S]*?\1', lambda m: add_token(m, "FCODE"), body)
    body = re.sub(r'(~{3,})[^\n]*\n[\s\S]*?\1', lambda m: add_token(m, "FCODE"), body)

    # Protect iframes
    body = re.sub(r'<iframe[\s\S]*?</iframe>', lambda m: add_token(m, "IFRAME"), body)

    # Protect raw HTML blocks
    body = re.sub(r'<(div|table|video|audio)[\s\S]*?</\1>', lambda m: add_token(m, "HTML"), body)

    # Protect images
    body = re.sub(r'!\[.*?\]\(.*?\)', lambda m: add_token(m, "IMG"), body)

    # Protect inline code
    body = re.sub(r'`[^`\n]+`', lambda m: add_token(m, "INLINE"), body)

    # Protect markdown links: [text](url) -> tokenize url
    url_counter = 0
    def replace_link(m):
        nonlocal url_counter
        anchor, url = m.group(1), m.group(2)
        url_tok = f"___URL_{url_counter}___"
        url_counter += 1
        tokens[url_tok] = url
        return f"[{anchor}]({url_tok})"
    
    body = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', replace_link, body)

    # 3. Translate body in chunks
    paragraphs = body.split('\n\n')
    translated_paras = []
    current_chunk = []
    current_len = 0

    for p in paragraphs:
        if current_len + len(p) > 2500 and current_chunk:
            chunk_text = '\n\n'.join(current_chunk)
            translated_paras.append(translate_chunk(chunk_text))
            current_chunk = [p]
            current_len = len(p)
            time.sleep(0.2)
        else:
            current_chunk.append(p)
            current_len += len(p)

    if current_chunk:
        chunk_text = '\n\n'.join(current_chunk)
        translated_paras.append(translate_chunk(chunk_text))

    translated_body = '\n\n'.join(translated_paras)

    # 4. Restore tokens
    for tok, orig in tokens.items():
        translated_body = translated_body.replace(tok, orig)

    # 5. Apply technical glossary refinement
    for pattern, repl in GLOSSARY:
        translated_body = re.sub(pattern, repl, translated_body)

    # 6. Translate Title and Summary if present
    fa_title = ''
    if 'title' in frontmatter:
        fa_title = translate_chunk(frontmatter['title'])
        for pattern, repl in GLOSSARY:
            fa_title = re.sub(pattern, repl, fa_title)

    fa_summary = ''
    if 'summary' in frontmatter:
        fa_summary = translate_chunk(frontmatter['summary'])
        for pattern, repl in GLOSSARY:
            fa_summary = re.sub(pattern, repl, fa_summary)

    # Reconstruct frontmatter
    fm_out = []
    for k, v in fm_lines:
        if k.lower() == 'title':
            fm_out.append(f"Title: {fa_title}")
        elif k.lower() == 'summary':
            fm_out.append(f"Summary: {fa_summary}")
        else:
            fm_out.append(f"{k}: {v}")
            
    return '\n'.join(fm_out) + '\n\n' + translated_body

def main():
    os.makedirs(DEST_DIR, exist_ok=True)
    os.makedirs(os.path.join(DEST_DIR, 'pages'), exist_ok=True)

    files = sorted(glob.glob(os.path.join(SRC_DIR, '*.md')))
    # Also include pages
    page_files = sorted(glob.glob(os.path.join(SRC_DIR, 'pages', '*.md')))
    all_files = files + page_files
    
    total = len(all_files)
    log(f"Starting translation of {total} files...")

    for idx, src_path in enumerate(all_files, 1):
        rel_path = os.path.relpath(src_path, SRC_DIR)
        dest_path = os.path.join(DEST_DIR, rel_path)
        
        # Check if already translated and valid
        if os.path.exists(dest_path) and os.path.getsize(dest_path) > 300:
            # Check if non-empty and has Persian
            with open(dest_path, 'r', encoding='utf-8') as f:
                head = f.read(500)
                if any('\u0600' <= char <= '\u06FF' for char in head):
                    log(f"[{idx}/{total}] Skipping already translated: {rel_path}")
                    continue

        log(f"[{idx}/{total}] Translating: {rel_path} ...")
        try:
            with open(src_path, 'r', encoding='utf-8') as f:
                content = f.read()

            translated = translate_file_content(content)
            
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            with open(dest_path, 'w', encoding='utf-8') as f:
                f.write(translated)
            
            log(f"[{idx}/{total}] Completed: {rel_path} (Output size: {len(translated)} bytes)")
            time.sleep(0.3)
        except Exception as e:
            log(f"[{idx}/{total}] ERROR translating {rel_path}: {e}")

    log("Translation process finished successfully!")

if __name__ == '__main__':
    main()
