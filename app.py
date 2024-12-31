from flask import Flask, request, render_template, jsonify
from collections import Counter
import re
import json
from extract import extracted_email, extracted_phoneNumber, extracted_name, extracted_education, extracted_wrkexp, extracted_summary

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/editor')
def editor():
    return render_template('editor.html')


@app.route('/submit', methods=['POST'])
def submit_data():

    data = request.json
    words = re.findall(r'\b\w+\b', data.lower())
    word_counts = Counter(words)
    email = extracted_email(data)
    phoneNumber = extracted_phoneNumber(data)
    name = extracted_name(data)
    education = extracted_education(data)
    work = extracted_wrkexp(data)
    summary = extracted_summary(data)
    print(f'Data: {data} , Email: {email}, Phone: {phoneNumber}, Name:{name}, Education: {education}, Summary : {summary}, Work Experience : {work}')
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
