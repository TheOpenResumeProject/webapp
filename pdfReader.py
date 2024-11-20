from pypdf import PdfReader
import re


def cleaner(list_array, item):
    res = [i for i in list_array if i != item]
    return res


def pefReader(data):

    reader = PdfReader(data)
    content = reader.pages[0].extract_text() + reader.pages[1].extract_text()
    content_lower = content.lower()
    education_array = []
    work_array = []
    summary_array = []
    personal_data = []
    content_array = content_lower.split(' ')
    elements = ' '.join(content_array)
    pattern_2 = r' {2,}'
    results = re.sub(pattern_2, '  ', elements)
    result_arr = results.split(' ')
    result_arr.remove('')
    new_arr = cleaner(result_arr, '')
    try:
        end_of_summary = new_arr.index('\neducation:')
        end_of_edu = new_arr.index('\nwork')
        end_of_work = new_arr.index('\nleadership')
        end_of_publications = new_arr.index('')
        end_of_bio = new_arr.index('\nobjective')

    except ValueError:
        print('Value does not exist')
    try:
        for i, x in enumerate(new_arr):
            if x.strip() == "education:":  # stripe function takes care of the \n that is present with education just like it is with every new line. also regex may be better # since characters like : will cause a probelm with indiviusal word search.
                for i in range(i, end_of_edu):
                    education_array.append(new_arr[i])
    except IndexError:
        print('Educational experience not found')

    try:
        for a, b in enumerate(new_arr):
            if b.strip() == "work" and new_arr[a + 1].strip() == "experience:":
                for a in range(a, end_of_work):
                    work_array.append(new_arr[a])
    except IndexError:
        print('Work experience not found')

    try:
        for c, d in enumerate(new_arr):
            if d.strip() == "objective" or d.strip() == "summary":
                for c in range(c, end_of_summary):
                    summary_array.append(new_arr[c])
    except IndexError:
        print('Professional summary not found')

    try:
        for e, f in enumerate(new_arr):
            if f.strip() == "publications" or d.strip() == "projects":
                for c in range(c, end_of_publications):
                    summary_array.append(new_arr[c])
    except IndexError:
        print('Publications not found')

    try:
        for g, h in enumerate(new_arr[0:15]):
            personal_data.append(h)
    except IndexError:
        print('Publications not found')

    #print(new_arr)
    print(f'\n Personal Data: {personal_data} \n\n Candidate Objective: {summary_array} \n\n '
          f'Educational experince : {education_array} \n\n Work Experience : {work_array}')


pefReader('MMujtaba-CV.pdf')
