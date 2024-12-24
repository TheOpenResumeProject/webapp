from flask import Flask, request, render_template, jsonify
from collections import Counter
import re
import json


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
    #words = re.findall(r'\b\w+\b', data.lower())  # Extract words
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
    ext_education = []
    starting_i = 0
    for i in data:
        if i == 'education':
            starting_i = data.index(i)
    for j in range(starting_i, (starting_i + 10), 1):
        ext_education.append(data[j])
    print(ext_education)
    return None
