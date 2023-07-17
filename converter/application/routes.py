from flask import Flask, jsonify, Response, message_flashed 
import sys
from flask import jsonify
from flask import jsonify
import json
from flask import json
from datetime import datetime

app = Flask(__name__)

today = datetime.now()


@app.route('/date/<birthDate>', methods=['GET', 'POST'])
def birthDate(birthDate):
    try:
        birthDate = int(float(birthDate))
    except ValueError:
        return "ValueError: enter a number"
    year = datetime.utcnow().year
    ageInMonths = (int(year) - int(birthDate)) * 12
    if birthDate < 1:
        return 'value entered is less than one month'
    elif birthDate > year + 1:
        return 'value exceeds current birth year'
    else: 
        return str(ageInMonths)
    