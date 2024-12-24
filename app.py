from flask import Flask, request, render_template, jsonify
from flask import make_response
from collections import Counter
import re
import json
import os

import pdfkit

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/editor1')
def editor1():
    return render_template('editor.html')


@app.route('/submit', methods=['Post'])
def submit_data():
    data = request.json
    words = re.findall(r'\b\w+\b', data.lower())
    word_counts = Counter(words)
    # print(f'Word count: {word_counts}')
    email = extracted_email(data)
    phoneNumber = extracted_phoneNumber(data)
    print(f'Data: {data}, Email: {email}, Phone: {phoneNumber}')
    return jsonify({"received_data": data, "email": email, "phone": phoneNumber})


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

@app.route("/validate", methods=["POST"])
def validate():
    data = request.get_json();

    #TODO: validate
    return json.dumps(data)

@app.route("/editor", methods=["GET"])
def editor():
    resume_data = None
    with open("example.json", "r") as file:
        resume_data = file.read()

    return render_template('generate.html', resume_json=resume_data)


@app.route("/render/pdf", methods=["POST"])
def render_pdf():
    resume_data = request.get_json()

    css_path = 'static/css/styles.css'
    css_path_abs = os.path.abspath(css_path)

    rendered_resume = render_template('template.html', resume=resume_data, css_path=css_path_abs)
    path_to_pdf =  "generated_resume.pdf"

    options = {
        'no-images': '',
        'javascript-delay': '2000',
        'enable-local-file-access': '',
        'load-error-handling': 'ignore',
        'enable-external-links': '',  # Allow external CSS links to be loaded
    }

    pdf = pdfkit.from_string(rendered_resume, False, options=options)
    # Create a response object
    response = make_response(pdf)
    
    # Set content-type to application/pdf for the browser to interpret the response as a PDF
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=generated_resume.pdf'
    
    return response

@app.route("/render", methods=["POST"])
def render():
    request_data = request.get_json()
    template_id = request_data.get("template_id", 1)
    resume_data = request_data["content"]

    template = "template.html"
    if template_id == "2":
        template = "template2.html"
    
    return render_template(template, resume=resume_data)

@app.route("/template", methods=["GET"])
def template():
    # this is the initial load.
    resume_data = None
    with open("example.json", "r") as file:
        resume_data = json.load(file)
    
    return render_template('template2.html', resume=resume_data)

if __name__ == '__main__':
    app.run(debug=True)
