import json
import time
import os.path as osp

import sqlite3
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

if not osp.exists("count.sqlite"):
	conn = sqlite3.connect('count.sqlite')
	conn.execute('''CREATE TABLE "view" (
		"id"	INTEGER NOT NULL UNIQUE,
		"time"	INTEGER NOT NULL,
		PRIMARY KEY("id" AUTOINCREMENT)
	    );''')


@cross_origin()
@app.route("/", methods=['POST'])
def get_view():
	conn = sqlite3.connect('count.sqlite')
	cmd = f"""INSERT INTO view (time) VALUES ({int(time.time())})"""
	conn.execute(cmd)
	conn.commit()
	cursor = conn.cursor()
	cursor.execute("""SELECT COUNT(*) FROM view""")
	rets = cursor.fetchall()
	return str(rets[0][0])


@cross_origin()
@app.route("/", methods=['GET'])
def add_view():
	conn = sqlite3.connect('count.sqlite')
	cursor = conn.cursor()
	cursor.execute("""SELECT COUNT(*) FROM view""")
	rets = cursor.fetchall()
	return str(rets[0][0])
