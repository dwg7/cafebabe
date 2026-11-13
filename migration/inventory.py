#!/usr/bin/env python3
"""Inventory of cafebabe's knowledge, for the miso migration (stage 0 baseline).

Standard library only. Prints a summary and writes a JSON inventory.

    python3 migration/inventory.py                      # summary of the working tree
    python3 migration/inventory.py --write FILE.json    # also write the inventory
    python3 migration/inventory.py --compare FILE.json  # fail if anything decreased

The inventory is the definition of "no knowledge lost" (capability C3/C4 in
migration/PLAN.md): sections, known uses, corrections, external URLs and
decision references must not decrease across the migration.
"""
import json
import re
import subprocess
import sys

URL = re.compile(r'https?://[^\s)>`\]]+')
MDLINK = re.compile(r'\]\(([^)\s]+\.md)(#[^)]*)?\)')
DREF = re.compile(r'\bD[0-9]{1,3}\b')
CORRECTION = re.compile(r'\*\*(訂正|追記|訂正・深掘り|訂正・追記)[^*]*\*\*')
HEDGE = re.compile(r'未検証|未確認|推論|未再現')


def tracked_markdown():
    out = subprocess.run(['git', 'ls-files', '*.md'], capture_output=True, text=True, check=True).stdout
    return [p for p in out.split('\n') if p and not p.startswith(('scratch/', 'migration/'))]


def sections(path, text):
    """Level-2 sections outside code fences: title, tag, known-use bullets, corrections."""
    res, cur, in_fence, in_known = [], None, False, False
    for ln in text.split('\n'):
        if ln.lstrip().startswith('```'):
            in_fence = not in_fence
        if not in_fence and ln.startswith('## '):
            cur = {'file': path, 'title': ln[3:].strip(), 'tag': None, 'known_use_bullets': 0,
                   'has_known_uses': False, 'corrections': 0}
            res.append(cur)
            in_known = False
            continue
        if cur is None:
            continue
        if ln.startswith('**タグ**'):
            cur['tag'] = ln.split(':', 1)[1].strip() if ':' in ln else ln
        if '実例(Known uses)' in ln:
            cur['has_known_uses'] = True
            in_known = True
            continue
        if in_known and ln.startswith('**') and '実例' not in ln:
            in_known = False
        if in_known and ln.startswith('- '):
            cur['known_use_bullets'] += 1
        cur['corrections'] += len(CORRECTION.findall(ln))
    return res


def build():
    files, secs, urls, links, anchors, drefs, hedges = [], [], set(), 0, 0, 0, 0
    for p in tracked_markdown():
        text = open(p, encoding='utf-8').read()
        files.append({'path': p, 'lines': text.count('\n'), 'bytes': len(text.encode('utf-8'))})
        urls.update(u.rstrip('.,;') for u in URL.findall(text))
        for m in MDLINK.finditer(text):
            links += 1
            anchors += 1 if m.group(2) else 0
        if p.startswith('patterns/'):
            secs += sections(p, text)
            drefs += len(DREF.findall(text))
            hedges += len(HEDGE.findall(text))
    pat = [f for f in files if f['path'].startswith('patterns/')]
    totals = {
        'markdown_files': len(files),
        'markdown_lines': sum(f['lines'] for f in files),
        'markdown_bytes': sum(f['bytes'] for f in files),
        'pattern_files': len(pat),
        'pattern_lines': sum(f['lines'] for f in pat),
        'pattern_sections': len(secs),
        'pattern_sections_tagged': sum(1 for s in secs if s['tag']),
        'pattern_sections_with_known_uses': sum(1 for s in secs if s['has_known_uses']),
        'known_use_bullets': sum(s['known_use_bullets'] for s in secs),
        'dated_corrections': sum(s['corrections'] for s in secs),
        'hedge_mentions_in_patterns': hedges,
        'internal_md_links': links,
        'internal_md_links_with_anchor': anchors,
        'external_urls_unique': len(urls),
        'decision_refs_in_patterns': drefs,
    }
    head = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()
    return {'commit': head, 'totals': totals, 'files': files, 'sections': secs, 'external_urls': sorted(urls)}


NON_DECREASING = ['pattern_sections', 'pattern_sections_with_known_uses', 'known_use_bullets',
                  'dated_corrections', 'external_urls_unique', 'decision_refs_in_patterns']


def main(argv):
    inv = build()
    for k, v in inv['totals'].items():
        print('%-36s %s' % (k, v))
    if '--write' in argv:
        path = argv[argv.index('--write') + 1]
        json.dump(inv, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print('wrote', path)
    if '--compare' in argv:
        base = json.load(open(argv[argv.index('--compare') + 1], encoding='utf-8'))
        bad = [k for k in NON_DECREASING if inv['totals'][k] < base['totals'][k]]
        lost = sorted(set(base['external_urls']) - set(inv['external_urls']))
        for k in bad:
            print('DECREASED %s: %s -> %s' % (k, base['totals'][k], inv['totals'][k]))
        for u in lost:
            print('LOST URL', u)
        return 1 if bad or lost else 0
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
