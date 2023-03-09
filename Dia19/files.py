""" from itertools import count


fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
   if line.startswith('Subject: '):
      count = count + 1
print('There were', count, 'subject line in', fname) """

# f = open('../files/reading_file_example.txt')
""" print(f)

txt = f.read()
print(type(txt))
print(txt) """

#  f = open('../files/reading_file_example.txt')
""" lines = f.readlines()
print(type(lines))
print(lines)
f.close() """

"""with open('../files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
   print(type(lines))
   print(lines) """
   
""" with open('../files/reading_file_example.txt', 'a') as f:
   f.write('This text has to be appended at the end')

with open('../files/writing_file_example.txt', 'w') as f:
   f.write('This text will be written in a newly created file') """

""" import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('../files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4) """

import xlrd
excel_book = xlrd.open_workbook('../files/sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)
print(excel_book)


































