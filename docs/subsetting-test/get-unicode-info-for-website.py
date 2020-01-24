
# Download a web page, and print Unicode information about all the text.
import unicodedata
import sys

import lxml.html
import requests

r = requests.get(sys.argv[1])
root = lxml.html.document_fromstring(r.content)
text = str(root.text_content())
code_points = sorted(set(text))
for point in code_points:
    try:
        name = unicodedata.name(point)
    except ValueError:
        name = ascii(point)
    print("U+{:04X}: {}".format(ord(point), name))