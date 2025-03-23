import json
from par import *
data = {
  "version": "0.0.1",
  "format": "orf",
  "meta": {
    "name": "John Doe",
    "sort": "chronological",
    "sort_order": "asc",
    "tags": [
      "tech",
      "software_development",
      "backend"
    ]
  },
  "data": {
    "personal": {
      "name": "John Doe",
      "phone_number": "8009001000",
      "country_code": "+1",
      "address_line_1": "null",
      "address_line_2": "null",
      "city": "Raleigh",
      "state": "NC",
      "zip": "null",
      "country": "us",
      "email": "john.doe@email.com",
      "url_linkedin": "null",
      "url_portfolio": "null",
      "url_website": "null",
      "url_other": [
        {
          "text": "Facebook",
          "url": "facebook.com/user"
        },
        {
          "text": "Dribble",
          "url": "dribble.com/user"
        }
      ]
    },
    "summary": "to obtain employment in XYZ field.",
    "education": [
      {
        "degree_level": "bachelors",
        "degree_title": "B.A.",
        "completed": "true",
        "institution": "Earlham College",
        "major": "Computer Science",
        "minor": "null",
        "concentration": "null",
		"gpa": "3.99",
		"gpa_scale": "4.00",
        "institution_city": "Richmond",
        "institution_state": "IN",
        "institution_zip": "47374",
        "institution_country": "us",
        "start_day": 14,
        "start_month": 9,
        "start_year": 2014,
        "end_day": 6,
        "end_month": 5,
        "end_year": 2018
      },
      {
        "degree_level": "masters",
        "degree_title": "M.S.",
        "completed": "true",
        "institution": "North Carolina State University",
        "major": "Computer Engineering",
        "minor": "null",
        "concentration": "Computer Architecture & Systems",
		"gpa": "3.99",
		"gpa_scale": "4.00",
        "institution_city": "Raleigh",
        "institution_state": "NC",
        "institution_zip": "27607",
        "institution_country": "us",
        "start_day": 14,
        "start_month": 9,
        "start_year": 2021,
        "end_day": 6,
        "end_month": 5,
        "end_year": 2023
      }
    ],
    "experience": [
      {
        "title": "Software Developer",
        "employer": "XYZ Solutions, Inc",
        "employer_city": "Lake Villa",
        "employer_state": "IL",
        "employer_zip": "60046",
        "employer_country": "us",
        "employer_phone_number": "null",
        "description": [
		  "Led a major REST API from development to production. Scheduled tasks and sprint goals based on team needs following Agile methods.",
		  "Replaced 200+ database tables with a new authorization service, achieving greater developer efficiency, lower maintenance cost, and fewer security incidents",
		  "Reduced response times by 95% (backend: 5s - .5s, frontend: 2m - 0.3s) after detailed performance analysis. Planned and led the execution of an optimization sprint.",
		  "Reduced client onboarding time from days to hours after migrating to reproducible, version-controlled Infrastructure-as-code solutions.",
		  "Enabled faster error detection, bugfixes, and reduced downtime through detailed exception tracking, stack trace analysis, and infrastructure health monitoring."
        ]
      }
    ],
    "skill": [
      {
        "name": "c",
        "proficiency_level": "beginner",
        "catogory": "programmaing language"
      },
      {
        "name": "c++",
        "proficiency_level": "intermediate",
        "category": "programming language"
      }
    ],
    "publication": [
      {
        "title": "a groundbreaking research",
        "url": "https://nature.com/next-einstein",
        "year": 2018,
        "credits": "Doe, J., et al",
        "citation_format": "apa"
      },
      {
        "title": "Yet Another groundbreaking research",
        "url": "https://nature.com/next-einstein",
        "year": 2021,
        "credits": "Doe, J., et al",
        "citation_format": "apa"
      }
    ],
    "projects": [
      {
        "title": "Operating System Kernel Functionalities in XINU Microkernel",
        "sub_title": "null",
        "url": "https://github.com/salekinsirajus/realxinu",
        "description": [
			"Implemented scheduling algorithms (lottery, MLFQ), Locks (Spin, Active, Priority Inversion), and fork() system call.",
			"Used C and Assembly"
        ]
      },
      {
        "title": "Standard for Machine-Readable Resume",
        "sub_title": "null",
        "url": "https://github.com/TheOpenResumeProject/OpenResume",
        "description": [
          "Came up with a standard so that the data can be separated from formatting",
          "Built a proof-of-concept using Flask, Python, and JavaScript"
        ]
      }
    ]
  }
}

print(data['data']['education'][0]['degree_level'])
#print(data['meta']["name"])