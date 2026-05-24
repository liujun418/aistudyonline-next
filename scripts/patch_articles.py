#!/usr/bin/env python3
"""
Patch article-content.ts with faithful MD-to-HTML converted entries.
Locates each entry by its exact structure and replaces it entirely.
"""
import re
import os

ENTRY_DIR = r'C:\Users\jun\aistudyonline-next\scripts'
TS_FILE = r'C:\Users\jun\aistudyonline-next\src\lib\article-content.ts'

def read_entry(slug):
    path = os.path.join(ENTRY_DIR, f'{slug}_entry.txt')
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

# The 6 slugs in the order they appear in the file
SLUGS = [
    '6-must-have-openclaw-skills',
    'ai-workforce-virtual-employees',
    'alexander-wang-meta-ai-superintelligence',
    'deerflow-multi-agent-tool',
    'free-ai-knowledge-base-tool-tutorial',
    'top-10-claude-code-commands',
]

def patch_file():
    with open(TS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    for slug in SLUGS:
        new_entry = read_entry(slug)

        # Build regex pattern matching the old entry structure
        # Existing format:
        # \t// ====== slug ======
        # \t"slug": {
        # \t\tcontent: `...content...`,
        # \t\tcontentZh: `...zh_content...`,
        # \t},
        old_pattern = (
            r'\t// ====== ' + re.escape(slug) + r' ======\n'
            r'\t"' + re.escape(slug) + r'": \{\n'
            r'\t\tcontent: `[^`]*`,\n'
            r'\t\tcontentZh: `[^`]*`,\n'
            r'\t\},'
        )

        match = re.search(old_pattern, content)
        if not match:
            print(f'ERROR: Could not find entry for {slug}')
            # Try alternative pattern
            print('  Trying alternative pattern...')
            alt_pattern = (
                r'// ====== ' + re.escape(slug) + r' ======\n'
                r'"' + re.escape(slug) + r'": \{\n'
                r'content: `[^`]*`,\n'
                r'contentZh: `[^`]*`,\n'
                r'\},'
            )
            match = re.search(alt_pattern, content)
            if match:
                print(f'  Found with alt pattern!')
            else:
                continue

        old_start = match.start()
        old_end = match.end()

        content = content[:old_start] + new_entry + content[old_end:]
        print(f'Replaced: {slug}')

    with open(TS_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    print('\nFile patched successfully!')


if __name__ == '__main__':
    patch_file()
