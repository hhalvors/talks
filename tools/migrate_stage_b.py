#!/usr/bin/env python3
"""Stage B of the talks repo: older decks from ~/research, matched to CV rows
in hhalvors.github.io/data/talks-master.yaml.

Copies (never moves) each deck's sources and PDF, plus files the .tex pulls in
(\\includegraphics, \\input, \\bibliography), into ~/talks/<id>/. Raster images
are copied for local builds only; .gitignore keeps them out of the repo.
Appends to MIGRATION-LOG.md. Usage: python3 tools/migrate_stage_b.py [HOME]
"""
import os, re, shutil, sys

H = os.path.expanduser(sys.argv[1] if len(sys.argv) > 1 else '~')
TALKS, RES = os.path.join(H, 'talks'), os.path.join(H, 'research')

# id -> stems under ~/research (first stem = the talk's main deck)
MAP = {
    'texas2007':     ['antimatter/texas'],
    'irvine2013':    ['structural-foundations'],
    'cuny2013':      ['cuny-slides'],
    'uwo2013':       ['uwo-slides'],
    'cmu2013':       ['theories'],
    'madrid2013':    ['madrid', 'madrid-aqft', 'madrid-cbh', 'madrid-particles', 'madrid-rindler'],
    'cambridge2014': ['dung-slides'],
    'oxford2014':    ['dung-ox'],
    'lse2014':       ['surplus'],
    'psa2014':       ['psa2014-hh'],
    'nagoya2015':    ['nagoya'],
    'munich2016':    ['munich-slides'],
    'stanford2017':  ['stanford2'],
    'buenos2017':    ['buenos-slides'],
    'apa2020':       ['apa2020-slides'],
    'copenhagen2022': ['bohrs-plads'],
    'bohr-potsdam':  ['bohr-unity'],          # slides beside the existing text
}
KEEP = ('.tex', '.pdf', '.bib', '.sty', '.md', '.qmd')
EXTS = ('', '.pdf', '.png', '.jpg', '.jpeg', '.eps', '.tex', '.bib', '.sty')
DEP = re.compile(r'\\(?:includegraphics|input|include|bibliography|addbibresource)\s*(?:\[[^\]]*\])?\{([^}]+)\}')
log = ['\n# Stage B (older decks from ~/research)']

def copy(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if os.path.exists(dst):
        return False
    shutil.copy2(src, dst)
    return True

for tid, stems in MAP.items():
    d = os.path.join(TALKS, tid)
    log.append(f'\n## {tid}')
    for stem in stems:
        base = os.path.join(RES, os.path.dirname(stem))
        name = os.path.basename(stem)
        for f in sorted(os.listdir(base)):
            if f.startswith(name + '.') and os.path.splitext(f)[1] in KEEP \
               and f[len(name):].count('.') == 1:
                if copy(os.path.join(base, f), os.path.join(d, f)):
                    log.append(f'- {f} (copied from research/{os.path.dirname(stem) or "."})')
        tex = os.path.join(base, name + '.tex')
        if not os.path.exists(tex):
            continue
        for m in DEP.finditer(open(tex, errors='ignore').read()):
            for n in (x.strip() for x in m.group(1).split(',')):
                if not n or n.startswith('http'):
                    continue
                for e in (EXTS if not os.path.splitext(n)[1] else ('',)):
                    if n.startswith('\\') or '#' in n:
                        break
                    p = os.path.join(base, n + e)
                    if os.path.isfile(p):
                        if copy(p, os.path.join(d, n + e)):
                            log.append(f'  - dependency {n + e}')
                        break
                else:
                    log.append(f'  - MISSING dependency {n} (for {name}.tex)')

with open(os.path.join(TALKS, 'MIGRATION-LOG.md'), 'a') as fh:
    fh.write('\n'.join(log) + '\n')
print('done', len(MAP))
