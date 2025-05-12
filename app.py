from flask import Flask, request, render_template, jsonify
from collections import Counter
import re
import json
from extract import extracted_email, extracted_phoneNumber, extracted_name, extracted_education, extracted_wrkexp, extracted_summary
import os
from pypdf import PdfReader

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/editor')
def editor():
    return render_template('editor.html')


UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        reader = PdfReader(file)
        for i in range(len(reader.pages)):
            page = reader.pages[i]
            print(page.extract_text())
        return jsonify({'message': 'File uploaded successfully', 'file_path': file_path})
    return jsonify({'error': 'Invalid file type. Only PDFs are allowed.'})


@app.route('/submit', methods=['POST'])
def submit_data():

    data = request.json
    #words = re.findall(r'\b\w+\b', data.lower())
    #word_counts = Counter(words)
    if isinstance(data, list):
        datastr = ' '.join(data)
    email = extracted_email(datastr)
    phoneNumber = extracted_phoneNumber(datastr)
    '''
    name = extracted_name(datastr)
    education = extracted_education(data)
    work = extracted_wrkexp(data)
    summary = extracted_summary(data)
    #print(f'Data: {data}: , Email:{email} , Phone:{phoneNumber} , Name: {name}, Education: {education}, Summary : {summary}, Work Experience : {work}')
    '''
    return jsonify({"received_data": data, "email": email, "phone": phoneNumber})



@app.route("/generate", methods=["GET"])
def generate_pdf():
    resume_data = None
    with open("example.json", "r") as file:
        resume_data = file.read()

    return render_template('generate.html', resume_json=resume_data)

@app.route("/template", methods=["GET"])
def template():
    resume_data = None
    with open("example.json", "r") as file:
        resume_data = json.load(file)

    return render_template('template.html', resume=resume_data)

if __name__ == '__main__':
    app.run(debug=True)
