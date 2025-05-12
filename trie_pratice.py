import PyPDF2
import matplotlib.pyplot as plt
from win32gui import FlashWindowEx
import pdfplumber
from numOfIslandsDfs import numOfIslands
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter



def pdf_opener(path):
    words = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                #text = text.replace("\n", " ")  # Convert newlines to spaces
                words.append(text.strip())
    return words


conjunctions = [
    "the", "and", "but", "or", "nor", "for", "yet", "so", "of",
    "although", "because", "since", "unless", "while", "whereas", "though",
    "if", "when", "whenever", "where", "wherever", "after", "before",
    "until", "once", "as", "than", "that", "whether", "even", "though",
    "provided", "lest", "in", "order", "to", "such", "which", "who",
    "whose", "whom", "whomever", "whereby", "therefore", "thus", "hence",
    "moreover", "however", "furthermore", "nevertheless", "consequently",
    "accordingly", "nonetheless", "besides", "otherwise", "meanwhile",
    "subsequently", "notwithstanding", "via", "by", "on", "through",
    "within", "outside", "inside", "between", "among", "throughout",
    "along", "beyond", "whereupon", "henceforth", "per", "amid", "about",
    "at", "over", "under", "considering", "concerning", "regarding",
    "following", "based", "due", "owing", "with", "regard", "pertaining"
]
education_words = [
    "education", "degree", "diploma", "certificate", "certification",
    "bachelor", "bachelors", "B.S.", "B.S", "M.S.", "M.S", "master", "masters", "doctorate", "phd",
    "associate", "associates", "major", "minor", "gpa", "cgpa", "grade",
    "summa", "cum", "laude", "magna", "dean", "honor", "scholarship",
    "university", "college", "high", "school", "academy", "graduation",
    "graduated", "expected", "year", "class", "relevant", "coursework",
    "concentration", "program", "training", "continuing", "professional",
    "development", "workshops", "seminars", "transcript", "credits",
    "units", "research", "thesis", "dissertation", "capstone", "project",
    "extracurricular", "activities", "student", "organizations", "society",
    "merit", "distinction", "enrollment", "matriculation", "undergrad",
    "postgraduate", "vocational", "technical", "apprenticeship",
    "internship", "fellowship", "residency", "mooc", "bootcamp",
    "elearning", "certifications", "licensure", "institution",
    "distance", "learning", "stem", "humanities", "business",
    "engineering", "medical", "law", "psychology", "finance",
    "accounting", "arts", "science", "technology", "computer",
    "statistics", "math", "economics", "biology", "chemistry",
    "physics", "political", "liberal", "communications", "journalism",
    "literature", "philosophy", "pedagogy", "tesol", "esl", "bilingual",
    "diversity", "instructional", "curriculum", "assessment", "special",
    "student", "classroom", "management", "teaching", "professor",
    "lecturer", "educator", "dean", "chancellor", "advisor", "counselor",
    "may"
]
job_experience_words = [
    "experience", "work", "employment", "job", "position", "role",
    "title", "responsibilities", "duties", "achievements", "tasks",
    "skills", "leadership", "management", "supervision", "collaboration",
    "communication", "mentoring", "training", "coaching", "development",
    "strategy", "execution", "performance", "growth", "results",
    "improvement", "productivity", "innovation", "problem", "solving",
    "decision", "making", "adaptability", "time", "organization",
    "project", "deadlines", "clients", "customers", "stakeholders",
    "vendors", "negotiation", "budget", "revenue", "sales", "marketing",
    "operations", "technology", "software", "hardware", "engineering",
    "design", "testing", "support", "helpdesk", "quality", "assurance",
    "data", "analysis", "documentation", "research", "risk", "consulting",
    "freelance", "internship", "contract", "temporary", "remote",
    "onsite", "telecommute", "supervisor", "manager", "director",
    "senior", "junior", "executive", "associate", "specialist",
    "consultant", "coordinator", "lead", "head", "president", "founder",
    "entrepreneur", "owner", "administrator", "trainer", "volunteer",
    "intern", "entry", "mid", "senior", "contractor", "subcontractor",
    "freelancer", "startup", "scaling", "cross", "global",
    "regional", "national", "local", "networking", "client", "meetings",
    "product", "development", "employee", "onboarding", "reviews",
    "company", "policies", "kpis", "metrics", "analytics", "pipeline",
    "crm", "customer", "support", "presentation"]

objective_words = [
    "seeking", "motivated", "goal", "oriented", "position",
    "opportunity", "career", "growth", "utilize", "skills",
    "experience", "contribute", "professional", "dynamic",
    "challenging", "environment", "learning", "enhance",
    "expand", "achieve", "success", "innovative", "passionate",
    "aspiring", "advance", "dedicated", "entry", "results",
    "driven", "adaptable", "problem", "solving", "leadership",
    "teamwork", "strategic", "detail", "analytical", "creative",
    "self", "motivated", "efficient", "people", "oriented",
    "solution", "focused", "fast", "paced", "impactful",
    "meaningful", "ambitious", "reliable", "hardworking",
    "visionary", "excited", "eager", "learn", "proactive",
    "resourceful", "customer", "focused", "deadline", "driven",
    "hands", "strong", "work", "ethic", "thrives", "pressure"
]

'''

education_words = [
    "Education", "Degree", "Diploma", "Certificate", "Certification",
    "Bachelor", "Bachelors", "Masters", "Master", "of", "Doctorate", "PhD", "Associates",
    "Associate", "Major", "Minor", "May", "Dec", "December",
    "GPA", "CGPA", "Honors", "Summa", "Cum", "Laude", "Magna", "Dean", "Scholarship",
    "University", "College", "High", "School", "Institution", "Academy",
    "Graduation", "Completed", "Expected", "Year", "Course", "Courses",
    "Relevant", "Studies", "Field", "Concentration", "Program", "Training",
    "Continuing", "Professional", "Development", "Workshops", "Seminars",
    "Credits", "Units", "Transcript", "Research", "Thesis", "Dissertation",
    "Capstone", "Project", "Study", "Subjects", "Extracurricular", "Activities",
    "Organizations", "Clubs", "Societies", "Honor", "Roll", "Academic",
    "Performance", "Achievement", "Awards", "Merit", "Distinction",
    "Educational", "Background", "Alma", "Mater", "Enrollment", "Matriculation",
    "Vocational", "Technical", "Apprenticeship", "Online", "Bootcamp",
    "MOOC", "E-Learning", "Certifications", "Licensure", "Accredited",
    "Institution", "Credits", "Internship", "Practicum", "Fellowship",
    "Residency", "Postgraduate", "Undergraduate", "Doctoral", "Master’s",
    "Bachelor’s", "Associate’s", "STEM", "Humanities", "Business",
    "Engineering", "Medical", "Law", "Psychology", "Finance", "Accounting",
    "Arts", "Science", "Technology", "Computer", "Information", "Systems",
    "Leadership", "Data", "Analysis", "Statistics", "Math",
    "Economics", "Biology", "Chemistry", "Physics", "Environmental", "Health",
    "Social", "Sciences", "History", "Political", "Science", "Liberal",
    "Studies", "Communications", "Journalism", "Literature", "Philosophy",
    "Education", "Pedagogy", "Teaching", "TESOL", "ESL", "Bilingual",
    "Multicultural", "Diversity", "Instructional", "Curriculum", "Assessment",
    "Educational", "Policy", "Special", "Education", "Counseling", "Development",
    "Learning", "Methodologies", "Strategies", "Student", "Engagement",
    "Classroom", "Management", "Education", "Administration"
]

job_experience_words = [
    "Experience", "Position", "Job", "Role", "Title", "Responsibilities",
    "Duties", "Achievements", "Accomplishments", "Tasks", "Skills",
    "Leadership", "Management", "Team", "Collaboration", "Communication",
    "Supervision", "Mentoring", "Training", "Coaching", "Development",
    "Strategy", "Execution", "Performance", "Growth", "Results",
    "Improvement", "Efficiency", "Productivity", "Innovation", "Solutions",
    "Problem-solving", "Decision-making", "Initiative", "Adaptability",
    "Time Management", "Organization", "Project", "Project Management",
    "Deadline", "Client", "Customer", "Vendor", "Stakeholder",
    "Negotiation", "Budget", "Cost", "Revenue", "Sales", "Marketing",
    "Product", "Service", "Operations", "Technology", "Software",
    "Hardware", "IT", "Engineering", "Development", "Design", "Testing",
    "Support", "Helpdesk", "Maintenance", "Analysis", "Data", "Reporting",
    "Documentation", "Research", "Quality", "Compliance", "Risk",
    "Strategy", "Consulting", "Customer Service", "Support", "Sales",
    "Client Relations", "Salesforce", "Contract", "Freelance",
    "Internship", "Part-time", "Full-time", "Temporary", "Remote",
    "On-site", "Telecommute", "Job Description", "Task", "Function",
    "Role", "Position", "Supervisor", "Manager", "Director",
    "Senior", "Junior", "Executive", "Associate", "Specialist",
    "Consultant", "Coordinator", "Lead", "Head", "President",
    "Founder", "Entrepreneur", "Owner", "Team Lead", "Team Member",
    "Assistant", "Administrator", "Trainer", "Trainer", "Supervisor",
    "Volunteer", "Intern", "Entry-level", "Mid-level", "Senior-level",
    "Supervisor", "Mentor", "Coach", "Consultant", "Founder",
    "Executive", "Leader", "Entrepreneur", "Contractor", "Subcontractor",
    "Freelancer", "Volunteer", "Start-up", "Scaling",
    "Leadership Development", "Cross-functional", "Cross-team",
    "Global", "Regional", "National", "Local", "Remote",
    "Workshops", "Presentations", "Client Meetings", "Customer Engagement",
    "Training", "Certifications", "Onboarding", "Employee Development",
    "Company Policies", "Performance Review", "Satisfaction", "Feedback"
]
objective_words = [
    "seeking", "motivated", "goal", "oriented", "position", "opportunity", "career",
    "develop", "growth", "utilize", "skills", "experience", "contribute", "dynamic",
    "professional", "challenging", "environment", "learning", "enhance", "expand",
    "achieve", "success", "innovative", "passionate", "aspiring", "advance",
    "dedicated", "entry-level", "results-driven", "adaptable", "problem-solving"
]

'''


class TrieNode:
    def __init__(self):  # constructor method
        self.children = {}  # initiates a dictionary
        self.endOfWord = 0  # attribute of the class

    def insert(self, word: str, tag=None):
        word = word.lower()
        pointer = self
        for char in word:  #for each character in word if that char already exists then it has a property which is the end of the word and is a number, add to that number the tag of the existing method
            if char not in pointer.children:
                pointer.children[char] = TrieNode()
            pointer = pointer.children[char]
        if pointer.endOfWord:
            pointer.endOfWord = str(pointer.endOfWord) + str(tag)
        else:
            pointer.endOfWord = str(tag)

    def search(self, word):
        word = word.lower()
        pointer = self
        for char in word:
            if char not in pointer.children:
                return '0'
            pointer = pointer.children[char]
        return pointer.endOfWord


trie = TrieNode()
for words in education_words:
    trie.insert(words, 1)
for words in job_experience_words:
    trie.insert(words, 2)
for words in objective_words:
    trie.insert(words, 3)
for words in conjunctions:
    trie.insert(words, 4)

final_data_list = []
fixed_data_list = []
restored_list = []
pages = pdf_opener('Fake_Resume_Jane_Doe.pdf')  #array of two strings
process_lines = []
for page in pages:
    process_lines += page.split('\n')
clean_lines = []
for i in process_lines:
    clean_lines.append(i.replace(",", ""))
raw_words = []
for line in clean_lines:
    raw_words.append(line.split())
mapped_words = []
for line in raw_words:
    mapping = []
    fixed_data_list.append(line.copy())
    #print(line)
    for word in line:
        result = trie.search(word)
        mapping.append(result)
    restored_list.append(mapping.copy())
    mapped_words.append(mapping)
    #print(mapping)

IDsetNonZero = numOfIslands(mapped_words)
data_table = []
set_count = 0
x_counter=0
for elements in IDsetNonZero:
    set_count += 1
    for x, y in elements:
        x_counter += 1
        row = {'row':x ,'col':y, 'code':restored_list[x][y]}
        data_table.append(row)
df = pd.DataFrame(data_table)
#df.to_csv('recovered_data_1.csv', index=False)

d_file = pd.read_csv('recovered_data.csv')



new_rows = []
for index, row in d_file.iterrows():
    code = row['code']
    if 10 <= code <= 99:
        q = code // 10
        r = code % 10
        new_rows.append({'row': row['row'], 'col':row['col'], 'code':q})
        new_rows.append({'row': row['row'], 'col':row['col'], 'code':r})
    elif 100 <= code <= 1000:
        quo = code // 100
        unit_r = code % 100
        quao = unit_r // 10
        quao1 = unit_r % 10
        new_rows.append({'row': row['row'], 'col': row['col'], 'code': quo})
        new_rows.append({'row': row['row'], 'col': row['col'], 'code': quao})
        new_rows.append({'row': row['row'], 'col': row['col'], 'code': quao1})
    else:
        new_rows.append(row.to_dict())

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
p_df = pd.DataFrame(new_rows)

#p_df.to_csv('recovered_data.csv', index=False)
x_axis = p_df['code']
y_axis = p_df['row']
labl = p_df['col']

plt.scatter(x_axis, y_axis, c=labl, cmap='viridis')
plt.colorbar()
#plt.show()

education = []
for dicts in new_rows:
    if dicts['code'] == 1:
        education.append(dicts)

row_c = Counter()

for dicts in education:
    row_c[dicts['row']] += 1

education.clear()
for r,c in row_c.items():
    education.append((r,c))
#print(education)

fltrd = []
for i in education:
    if i[1] != 1:
        fltrd.append(i)
education = fltrd

#print(education)

final_edu = []
j_l = []
for i in education:
    j_l.append(i[0])
    cnt = 0
for j in education:
    k = j[0]
    final_edu.append(k)

final_edu_set = set(final_edu)



longest = 0
longest_seq = []
for n in final_edu:
    if (n-1) not in final_edu_set:
        current = n
        current_seq = [current]
        while (current + 1) in final_edu_set:
            current += 1
            current_seq.append(current)

        if len(current_seq) > longest:
            longest = len(current_seq)
            longest_seq = current_seq
#print(fixed_data_list)

extracted_education = []
for i in longest_seq:
    extracted_education.append(fixed_data_list[i])
print(extracted_education)