from PyPDF2 import PdfReader
import sys
import json

file = sys.argv[1]
pdf_reader = PdfReader(open(file, 'rb'))
dictionary1 = dict()
dictionary = dict()
dictionary1['document.pagecount'] = pdf_reader._get_num_pages()
dictionary1['document.fieldcount'] = len(pdf_reader.get_form_text_fields())
field = pdf_reader.get_form_text_fields()
for key in field:
    dictionary1[key] = field[key]
dictionary["map"] = dictionary1
file1 = sys.argv[2]
x = json.dumps(dictionary, indent= 2)
with open (file1, 'w') as f:
    f.write(x)
