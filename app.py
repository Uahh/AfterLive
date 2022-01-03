# -*- coding: utf-8 -*-
import time
import json
# import config
import sqlite3
from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__, template_folder='templates', static_folder='static')
print('Waiting......')


# 主要逻辑视图函数
@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    return render_template('test.html')

@app.route('/data', methods=["GET", "POST"])
def data():
    with open('./json/data.json', encoding='utf-8') as f:
        test_line = json.load(f)
        f.close()
    return test_line


@app.route('/error')
def error():
    return '404 not found'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=173)