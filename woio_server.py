#!/usr/bin/python3
# -*- coding: UTF-8 -*-
###############################################
#                                             #  
#                               __            #  
#   __    __   _____           |__|  _____    #  
#  |  |/\|  | /     \   ____   |  | /     \   #  
#  |        ||   o   | |    |  |  ||   o   |  #  
#  |___/\___| \_____/  |____|  |__| \_____/   #  
###############################################
#  2016/01/26 by DKZ https://davidkingzyb.github.io

import doio
import json
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import jsonify
#from flask import abort
#from flask import url_for
#from flask import Markup
from functools import wraps
from flask import make_response


def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst
    return wrapper_fun

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/io',methods=['POST','GET'])
def io():
    tty=request.values.get('tty','')
    output=doio.dotty(tty)
    resp={'flag':'ok','output':output}
    return jsonify(resp)

@app.route('/clio',methods=['POST','GET'])
@allow_cross_domain
def clio():
    obj=request.values.get('obj','')
    func=request.values.get('func','')
    ttyarg=func+'('+obj+')'
    output=doio.doClio(ttyarg)
    resp={'flag':'ok','output':output}
    return jsonify(resp)


@app.route('/home')
def home():
    return redirect('https://davidkingzyb.github.io/home.html')

@app.route('/blog')
def blog():
    return redirect('https://davidkingzyb.github.io/blog.html')

if __name__=='__main__':
    app.debug=True
    app.run()
