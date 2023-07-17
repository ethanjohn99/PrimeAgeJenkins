from flask import Flask, jsonify, Response 
from flask import jsonify
import sys
from flask import jsonify
import json
from flask import json

app = Flask(__name__)

@app.route('/date/<ageInMonths>', methods=['GET', 'POST'])
def prime(ageInMonths):
    try:
        ageMonths = int(float(ageInMonths))
    except ValueError:
        return "ValueError: please enter a number"
    if ageMonths > 1:
        for i in range(2, ageMonths):
            if ageMonths % i == 0:
                return 'composite'
            else:
                return 'prime'
    elif ageMonths == 1:
        return 'neither prime nor composite'
    else:
        prime = "You do not appear to exist"
    print(str(prime), file=sys.stderr)
    print(str(prime), file=sys.stdout)
    return prime