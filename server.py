#!/bin/python2
from flask import Flask, request, render_template, redirect, url_for, jsonify
import os, json, MySQLdb

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        db, c = connect_to_db()
        c.execute('''SELECT selishte.prefix, selishte.name, oblast.name, obshtina.name FROM oblast INNER JOIN selishte ON selishte.oblast_id = oblast.oblast_id INNER JOIN obshtina ON obshtina.obshtina_id = selishte.obshtina_id WHERE selishte.name LIKE %s''', ("%" + request.form['search'] + "%",))
        result = c.fetchall()
        return render_template('main.html', res = result)
    return render_template('main.html')

@app.route('/data/<filename>', methods=['GET'])
def get_geojson(filename=None):
    #check if filename is valid
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT,"data",filename)
    data = json.load(open(json_url))
    return jsonify(data)

@app.route('/<oblast>', methods=['GET'])
def get_oblast(oblast=None):
    print oblast
    pass

@app.route('/<oblast>/<obshtina>', methods=['GET'])
def get_obshtina(oblast=None,obshtina=None):
    pass

@app.route('/<oblast>/<obshtina>/<selishte>', methods=['GET'])
def get_selishte(oblast=None,obshtina=None,selishte=None):
    db, c = connect_to_db()
    c.execute('''SELECT oblast.name, oblast.oblast_id, obshtina.name, obshtina.obshtina_id, selishte.kmetstvo_id, selishte.name, selishte.ekatte, selishte.kind, selishte.altitude FROM selishte INNER JOIN obshtina ON selishte.obshtina_id = obshtina.obshtina_id INNER JOIN oblast ON oblast.oblast_id = selishte.oblast_id WHERE oblast.name=%s AND obshtina.name=%s AND selishte.name=%s;''',(oblast,obshtina,selishte))
    result = c.fetchone()
    return render_template('details.html', result = result)

MYSQL_USER='root'
MYSQL_PASSWORD='toor'
MYSQL_DB='ekatte'
MYSQL_HOST='localhost'

def connect_to_db():
    try:
        db = MySQLdb.connect(user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DB, host = MYSQL_HOST, charset="utf8")
        c = db.cursor()
        return db, c
    except(MySQLdb.Error, MySQLdb.Warning) as err:
        print err
        #Should log error to out
        return None, None

if __name__ == "__main__":
    app.run()

