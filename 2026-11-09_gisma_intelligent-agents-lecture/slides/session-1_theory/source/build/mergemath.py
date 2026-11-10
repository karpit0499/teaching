"""Merge math pieces (Noto Serif text boxes laid side by side, subscripts as smaller boxes) into one
text box per expression, with native PowerPoint subscripts. Run on the raw export, before animate.py.
usage: python3 mergemath.py in.pptx out.pptx
"""
import sys, copy
from pptx import Presentation
from lxml import etree

A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
PX = 6350
src, dst = sys.argv[1:3]
prs = Presentation(src)
merged = 0
for slide in prs.slides:
    pieces = []
    for sh in slide.shapes:
        if not sh.has_text_frame or not sh.text_frame.text:
            continue
        runs = [r for p in sh.text_frame.paragraphs for r in p.runs]
        if runs and all(r.font.name == 'Noto Serif' for r in runs) and len(sh.text_frame.paragraphs) == 1:
            pieces.append(sh)
    pieces.sort(key=lambda s: (s.left))
    groups = []
    for sh in pieces:
        for g in groups:
            last = g[-1]
            vo = min(last.top + last.height, sh.top + sh.height) - max(last.top, sh.top)
            sz = lambda x: x.text_frame.paragraphs[0].runs[0].font.size
            big, small = max(sz(last), sz(sh)), min(sz(last), sz(sh))
            same_or_sub = small == big or small <= big * 0.7   # equal sizes, or a subscript next to its base
            if vo > 0 and same_or_sub and -14 * PX <= sh.left - (last.left + last.width) <= 12 * PX:
                g.append(sh); break
        else:
            groups.append([sh])
    for g in groups:
        if len(g) < 2:
            continue
        size = max(r.font.size for s in g for p in s.text_frame.paragraphs for r in p.runs)
        mains = [s for s in g if s.text_frame.paragraphs[0].runs[0].font.size == size]
        top = min(s.top for s in mains); bottom = max(s.top + s.height for s in mains)
        left = min(s.left for s in g); right = max(s.left + s.width for s in g)
        pad = int((right - left) * 0.2)
        keep = mains[0]._element
        new = copy.deepcopy(keep)
        xfrm = new.find(f'.//{A}xfrm')
        xfrm.find(f'{A}off').set('x', str(left - pad)); xfrm.find(f'{A}off').set('y', str(top))
        xfrm.find(f'{A}ext').set('cx', str(right - left + 2 * pad)); xfrm.find(f'{A}ext').set('cy', str(bottom - top))
        body = new.find(f'.//{A}bodyPr'); body.set('wrap', 'none')
        for c in list(body): body.remove(c)
        para = new.find(f'.//{A}p')
        para.find(f'{A}pPr').set('algn', 'ctr')
        tmpl = para.find(f'{A}r')
        for r in para.findall(f'{A}r'): para.remove(r)
        end = para.find(f'{A}endParaRPr')
        for s in g:
            for r in s.text_frame.paragraphs[0].runs:
                nr = copy.deepcopy(r._r)
                rpr = nr.find(f'{A}rPr')
                if r.font.size < size:
                    rpr.set('sz', str(int(size.pt * 100))); rpr.set('baseline', '-25000')
                end.addprevious(nr)
        keep.addprevious(new)
        for s in g:
            s._element.getparent().remove(s._element)
        merged += 1
prs.save(dst)
print('merged', merged, 'expressions')
