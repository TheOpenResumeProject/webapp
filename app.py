from flask import Flask, request, render_template, jsonify
from collections import Counter
import re
import json

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/editor')
def editor():
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

@app.route("/generate", methods=["GET"])
def generate_pdf():
    resume_data = None
    with open("example.json", "r") as file:
        resume_data = file.read()

    return render_template('generate.html', resume_json=resume_data)

@app.route("/render", methods=["POST"])
def render():
    resume_data = request.get_json()

    return render_template('template2.html', resume=resume_data)

@app.route("/template", methods=["GET"])
def template():
    # this is the initial load.
    resume_data = None
    with open("example.json", "r") as file:
        resume_data = json.load(file)

    return render_template('template2.html', resume=resume_data)

if __name__ == '__main__':
    app.run(debug=True)
