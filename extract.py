
import re



def extracted_email(data):
    email = re.findall("[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+@[a-z]+.{4}", data.lower())
    if email:
        return email[0]
    return None


def extracted_phoneNumber(data):
    phone = re.findall(r'\d{3}\W?\d{3}\W?\d{4}', data.lower())
    if phone:
        return phone[0]
    return None


def extracted_name(data):
    ext_name = []
    pattern = r'\b[A-Z][a-z]*\b|\b[A-Z]+\b'
    matches = list(re.finditer(pattern, data))
    if matches:
        for i in range(2):
            ext_name.append(matches[i].group())
        return ext_name
    return None


def extracted_education(data):
    # logic of this function, collect 10 elements after the word educaiton appears
    cleaned_data = [item.strip().lower() for item in data]
    ext_education = []
    starting_i = -1
    for i in range(len(cleaned_data) - 1):
        if cleaned_data[i] == 'education':
            starting_i = i
    if starting_i != -1:
        for j in range(starting_i, (starting_i + 20), 1):
            ext_education.append(cleaned_data[j])
        return ext_education
    return None


def extracted_wrkexp(data):
    # logic of this function, collect 10 elements after the word work experince appears
    cleaned_data = [item.strip().lower() for item in data]
    ext_work = []
    starting_i = -1
    for i in range(len(cleaned_data) - 1):
        if ((cleaned_data[i] == 'work' and cleaned_data[i + 1] == 'experience') or
                cleaned_data[i] == 'employment' or cleaned_data[i] == "experience"):
            starting_i = i
    if starting_i != -1:
        for j in range(starting_i, (starting_i + 10), 1):
            ext_work.append(cleaned_data[j])
        return ext_work
    return None


def extracted_summary(data):
    # logic of this function, collect 10 elements after summary or professional summary appears
    ext_sum = []
    starting_i = -1
    for i in range(len(data) - 1):
        if data[i].strip().lower() == 'professional summary':
            starting_i = i

    if starting_i != -1:
        for j in range(starting_i + 1, (starting_i + 10), 1):
            ext_sum.append(data[j])
        return ext_sum
    else:
        return None

