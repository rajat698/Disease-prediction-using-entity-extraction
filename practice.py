import re

text_disease = open('diseasedata.txt', 'r').read()
string = text_disease
match = re.search("vomiting", string)
print('%d,%d' % (match.start(), match.end()))