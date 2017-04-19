#!/bin/python2
from flask import Flask, request, render_template, redirect, url_for, jsonify
import os, json, MySQLdb

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        db = MySQLdb.connect(user="root", passwd="toor", db="ekatte", host="127.0.0.1", charset="utf8")
        c=db.cursor()
        c.execute('''SELECT selishte.prefix, selishte.name, oblast.name, obshtina.name FROM oblast INNER JOIN selishte ON selishte.oblast_id = oblast.oblast_id INNER JOIN obshtina ON obshtina.obshtina_id = selishte.obshtina_id WHERE selishte.name LIKE %s''', ("%" + request.form['search'] + "%",))
        results = c.fetchall()
        return render_template('main.html', res = results)
    return render_template('main.html')

@app.route('/data/<filename>', methods=['GET'])
def get_geojson(filename=None):
    #check if filename is valid
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT,"data",filename)
    data = json.load(open(json_url))
    return jsonify(data)


if __name__ == "__main__":
    app.run()

