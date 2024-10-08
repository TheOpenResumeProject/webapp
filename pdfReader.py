from pypdf import PdfReader
import re

def cleaner(list_array, item):
    res = [i for i in list_array if i != item]
    return res

def pdfReader(data):
    item =''
    reader = PdfReader(data)
    content = reader.pages[0].extract_text()
    content_lower = content.lower()
    education_array = []
    content_array = content_lower.split(' ')
    elements = ' '.join(content_array)
    pattern_2 = r' {2,}'
    results = re.sub(pattern_2, '  ', elements)
    result_arr = results.split(' ')
    result_arr.remove('')
    new_arr = cleaner(result_arr, '')
    print(new_arr[0])
    y = new_arr.index('\nwork')
    for i, x in enumerate(new_arr):
        if x.strip() == "education:": #stripe function takes care of the \n that is present with education just like it is with every new line. also regex may be better # since characters like : will cause a probelm with indiviusal word search.
           for i in range(i, y):
                education_array.append(new_arr[i])

    print(education_array)
pdfReader('MMujtaba-CV.pdf')
