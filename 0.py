#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask,render_template
from flask import request
from flask_bootstrap import Bootstrap



app=Flask(__name__)
bootstrap=Bootstrap(app);

@app.route('/')
def index():
    user_agent=request.headers.get("User-Agent")
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)



if __name__ == '__main__':
    app.run(port='1234')