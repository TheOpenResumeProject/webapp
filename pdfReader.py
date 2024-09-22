from pypdf import PdfReader
import re


def pefReader(data):
    reader = PdfReader(data)
    content = reader.pages[0].extract_text()
    content_lower = content.lower()
    education_array = []
    content_array = content_lower.split(' ')
    elements = ' '.join(content_array)
    pattern_2 = r' {2,}'
    results = re.sub(pattern_2, '  ', elements)
    result_arr = results.split(' ')
    for i, x in enumerate(result_arr):
        if x == 'education':
            for j in range(i - 2, i + 120):
                education_array.append(content_array[j])
    education_exp = ' '.join(education_array)
    #print(content_array)
    print(education_exp)

pefReader('MMujtaba-CV.pdf')
