"""Fix glyphs the deck fonts lack, in a .pptx:
- Greek (Lato, IBM Plex Mono and Libre Baskerville have none) -> Noto Serif, which is embedded.
- Arrows (U+2190-21FF) in Lato / Libre Baskerville / Noto Serif runs -> Arial (present on every PowerPoint machine).
Runs are split where needed; all other run formatting is kept.
usage: python3 fixgreek.py in.pptx out.pptx
"""
import sys, re, copy, zipfile
from lxml import etree

A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
GREEK = '[Ͱ-Ͽἀ-῿]+'
ARROW = '[←-⇿]+'
src, dst = sys.argv[1:3]
fixed = 0

def set_face(rpr, face):
    for tag in ('latin', 'ea', 'cs'):
        for el in rpr.findall(A + tag):
            rpr.remove(el)
    after = None
    for tag in ('sym', 'hlinkClick', 'hlinkMouseOver', 'rtl', 'extLst'):
        after = rpr.find(A + tag)
        if after is not None:
            break
    for tag in ('latin', 'ea', 'cs'):
        el = etree.Element(A + tag, typeface=face, charset='0')
        if after is not None:
            after.addprevious(el)
        else:
            rpr.append(el)

zin = zipfile.ZipFile(src)
with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as z:
    for n in zin.namelist():
        d = zin.read(n)
        if re.match(r'ppt/slides/slide\d+\.xml$', n):
            root = etree.fromstring(d)
            for r in list(root.iter(A + 'r')):
                t = r.find(A + 't'); rpr = r.find(A + 'rPr')
                text = t.text or ''
                latin = rpr.find(A + 'latin') if rpr is not None else None
                face = latin.get('typeface') if latin is not None else ''
                rules = []
                if re.search(GREEK, text) and face != 'Noto Serif':
                    rules.append((GREEK, 'Noto Serif'))
                if re.search(ARROW, text) and face.startswith(('Lato', 'Libre', 'Noto')):
                    rules.append((ARROW, 'Arial'))
                if not rules:
                    continue
                split = re.compile('(' + '|'.join(p for p, _ in rules) + ')')
                for part in [p for p in split.split(text) if p]:
                    nr = copy.deepcopy(r)
                    nr.find(A + 't').text = part
                    for pat, target in rules:
                        if re.fullmatch(pat, part):
                            if nr.find(A + 'rPr') is None:
                                nr.insert(0, etree.Element(A + 'rPr', lang='en-US'))
                            set_face(nr.find(A + 'rPr'), target)
                    r.addprevious(nr)
                r.getparent().remove(r)
                fixed += 1
            d = etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)
        z.writestr(zin.getinfo(n), d)
print('runs fixed (Greek -> Noto Serif, arrows -> Arial):', fixed)
