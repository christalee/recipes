# begin{recipe}{$TITLE}
# \textbf{Source:} $SOURCE \hfill
# \ing[$QTY]{$UNIT}{$ING}
# \ing[]{}{}\n$STEP\n
# \newstep $STEP\n
# \freeform $TEXT \n

import re
import sys

input = open(sys.argv[1])
# output = open('template.rmd')
output = ''
previous = ''
for l in input:
    # print(l)
    m = re.search(r'\\begin{recipe}{(.*?)}', l)
    if m:
        output += '---\ntitle: ' + m.group(1)

    m = re.search(r'\\textbf{Source:} (.*?) \\hfill', l)
    if m:
        output += '\nsource: ' + m.group(1) + '\n---\n'

    m = re.search(r'\\freeform (.*?)\n', l)
    if m:
        output += '\n' + m.group(1) + '\n'

    m = re.search(r'\\ing\[(.*?)\].*?{(.*?)}.*?{(.*?)}', l)
    if m:
        output += '\n* ' + ' '.join([m.group(1), m.group(2), m.group(3)])

    m = re.search(r'(.*?)\n', l)
    n = re.search(r'\\ing', previous)
    if m and n:
        output += '\n- ' + m.group(1)

    m = re.search(r'\\newstep (.*?)\n', l)
    if m:
        output += '\n- ' + m.group(1)

    # print(m)
    previous = l[:]
print(output)
