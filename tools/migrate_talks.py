#!/usr/bin/env python3
"""Stage A of the talks repo: one folder per talk id in ~/talks.

Files already in ~/talks are moved (never deleted); files from the website repo
and ~/research are copied. Where two locations hold different versions of the
same file, the newer becomes the main file and the older is kept beside it as
<name>.local-YYYY-MM-DD (gitignored). Writes MIGRATION-LOG.md.
"""
import os, re, shutil, sys, time, hashlib

H = os.path.expanduser(sys.argv[1] if len(sys.argv) > 1 else '~/mnt')
TALKS = os.path.join(H, 'talks')
WEB = os.path.join(H, 'hhalvors.github.io', 'talks')
RES = os.path.join(H, 'research')
log = []

# id -> list of (location, stem). location in {'talks','web','res'}
MAP = {
 'pittsburgh2026': [('web', 'pittsburgh2026')],
 'schock': [('res', 'schock'), ('web', 'schock'), ('res', 'schock-beamer')],
 'equivalence-oslo': [('res', 'equivalence-oslo'), ('web', 'equivalence-oslo')],
 'reunions2026': [('web', 'reunions2026')],
 'bohr-causality': [('web', 'bohr-causality')],
 'climacus': [('talks', 'climacus'), ('web', 'climacus')],
 'b4bohr': [('web', 'b4bohr')],
 'venice-determinism': [('web', 'venice-determinism')],
 'equivalence': [('talks', 'equivalence'), ('web', 'equivalence')],
 'reduction': [('talks', 'reduction'), ('web', 'reduction')],
 'determinism': [('talks', 'nijmegen2025-slides'), ('talks', 'nijmegen2025')],
 'brandes': [('web', 'brandes')],
 'bohr-potsdam': [('web', 'bohr-potsdam')],
 'math-lang': [('web', 'math-lang')],
 'equivalence-foundations': [('web', 'equivalence-foundations')],
 'shifty': [('talks', 'shifty'), ('web', 'shifty'), ('talks', 'shifty-quotes')],
 'bohr-roots': [('talks', 'bohr-roots'), ('web', 'bohr-roots'), ('web', 'bohr-roots-beamer')],
 'windbag': [('talks', 'windbag'), ('web', 'windbag'), ('talks', 'windbag-citater'), ('web', 'windbag-citater')],
 'irvine2023': [('talks', 'irvine2023'), ('web', 'irvine2023')],
 'stockholm2023': [('talks', 'stockholm2023'), ('web', 'stockholm2023')],
 'konstanz': [('web', 'konstanz')],
 'bohr-values': [('talks', 'bohr-values'), ('web', 'bohr-values')],
 'hole-dispense': [('web', 'hole-dispense')],
 'formal-outline': [('web', 'formal-outline')],
 'vienna2023': [('web', 'vienna2023')],
 'illinois2019': [('web', 'illinois2019')],
 'prague2019': [('web', 'prague2019')],
 'munich2018-2cat': [('web', 'munich2018-2cat')],
 'salzburg2018': [('web', 'salzburg2018')],
 'munich2018': [('web', 'munich2018')],
 'rutgers2015': [('web', 'rutgers2015')],
}
ROOT = {'talks': TALKS, 'web': WEB, 'res': RES}
KEEP_EXT = ('.tex', '.md', '.qmd', '.html', '.pdf', '.pptx', '.key', '.bib', '.sty')
RASTER = ('.jpg', '.jpeg', '.png', '.gif', '.jp2', '.webp', '.wmf', '.bmp', '.tif', '.tiff')

def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()

def strip_notes(text):
    out, depth, innotes, fence = [], 0, False, False
    for line in text.split('\n'):
        if line.startswith('```'):
            fence = not fence
        if not fence and not innotes and line.strip() == '::: notes':
            innotes, depth = True, 1
            continue
        if innotes:
            if not fence and re.match(r'^:::+\s*\S', line):
                depth += 1
            elif not fence and re.match(r'^:::+\s*$', line):
                depth -= 1
                if depth == 0:
                    innotes = False
            continue
        out.append(line)
    s = '\n'.join(out)
    s = re.sub(r'<!--.*?-->\n*', '', s, flags=re.S)
    blocks = re.split(r'(?m)^(?=#{1,2} )', s)
    s = ''.join(b for b in blocks if not (b.startswith('#') and '{.bench}' in b.split('\n', 1)[0]))
    return re.sub(r'\n{3,}', '\n\n', s)

def place(src, dest_dir, how):
    """Put src into dest_dir; resolve version conflicts by date."""
    name = os.path.basename(src)
    dest = os.path.join(dest_dir, name)
    if os.path.exists(dest):
        if md5(src) == md5(dest):
            if how == 'mv':
                os.rename(src, dest + '.dup-ignored') if False else None
            return 'same'
        newer_src = os.path.getmtime(src) > os.path.getmtime(dest)
        old = dest if newer_src else src
        stamp = time.strftime('%Y-%m-%d', time.localtime(os.path.getmtime(old)))
        keep = os.path.join(dest_dir, f'{name}.local-{stamp}')
        if newer_src:
            os.rename(dest, keep)
            (shutil.move if how == 'mv' else shutil.copy2)(src, dest)
            log.append(f'  - {name}: newer version from {how} source; older kept as {os.path.basename(keep)}')
        else:
            if how == 'mv':
                shutil.move(src, keep)
            else:
                shutil.copy2(src, keep)
            log.append(f'  - {name}: kept existing newer file; other version saved as {os.path.basename(keep)}')
        return 'conflict'
    (shutil.move if how == 'mv' else shutil.copy2)(src, dest)
    return 'new'

DEP = re.compile(r'\\(?:includegraphics|input|include|bibliography|addbibresource|usepackage)\s*(?:\[[^\]]*\])?\{([^}]+)\}')
MDIMG = re.compile(r'!\[[^\]]*\]\(([^)\s]+)')

def deps(srcfile):
    txt = open(srcfile, errors='ignore').read()
    names = []
    for m in DEP.finditer(txt):
        names += [x.strip() for x in m.group(1).split(',')]
    names += MDIMG.findall(txt)
    return [n for n in names if n and not n.startswith('http')]

for tid, entries in MAP.items():
    d = os.path.join(TALKS, tid)
    os.makedirs(d, exist_ok=True)
    log.append(f'\n## {tid}')
    for loc, stem in entries:
        root = ROOT[loc]
        how = 'mv' if loc == 'talks' else 'cp'
        files = [f for f in os.listdir(root) if f.startswith(stem + '.') and f[len(stem):].count('.') == 1]
        for f in sorted(files):
            src = os.path.join(root, f)
            ext = os.path.splitext(f)[1].lower()
            if how == 'cp' and ext not in KEEP_EXT:
                continue          # build clutter stays behind in web/research
            r = place(src, d, how)
            if r == 'new':
                log.append(f'- {f} ({"moved" if how == "mv" else "copied from " + loc})')
            # dependencies of sources
            if ext in ('.tex', '.md', '.qmd'):
                for n in deps(os.path.join(d, f)):
                    cands = [n] if os.path.splitext(n)[1] else [n + e for e in ('.pdf', '.png', '.jpg', '.jpeg', '.tex', '.bib', '.sty')]
                    for c in cands:
                        for base in (root, TALKS, WEB):
                            p = os.path.join(base, c)
                            if os.path.isfile(p):
                                tgt = os.path.join(d, c)
                                os.makedirs(os.path.dirname(tgt), exist_ok=True)
                                if not os.path.exists(tgt):
                                    shutil.copy2(p, tgt)
                                    tag = ' (raster: local only)' if os.path.splitext(c)[1].lower() in RASTER else ''
                                    log.append(f'  - dependency {c}{tag}')
                                break
                        else:
                            continue
                        break
    # nordisk decks: publish without speaker notes
    for f in os.listdir(d):
        if f.endswith('.md'):
            p = os.path.join(d, f)
            t = open(p).read()
            if '::: notes' in t or '{.bench}' in t:
                os.rename(p, p + '.with-notes')
                open(p, 'w').write(strip_notes(t))
                log.append(f'  - {f}: speaker notes stripped; full version kept as {f}.with-notes (gitignored)')

open(os.path.join(TALKS, 'MIGRATION-LOG.md'), 'w').write('# Migration log (stage A)\n' + '\n'.join(log) + '\n')
print('done', len(MAP))
