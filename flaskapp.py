from flask import Flask, jsonify, request
import csv 
import json

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        jsonArray = []
    c = r'/home/ubuntu/anand.csv'

    with open(c) as csvf:
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            jsonArray.append(row)
        return jsonify(jsonArray)

if __name__ == '__main__':

	app.run(debug = True)

