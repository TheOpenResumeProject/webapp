from flask import Flask, request, render_template, jsonify
from collections import Counter
import re

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



if __name__ == '__main__':
    app.run(debug=True)
