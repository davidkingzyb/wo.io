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
#from flask import make_response

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

@app.route('/home')
def home():
    return redirect('https://davidkingzyb.github.io/home.html')

@app.route('/blog')
def blog():
    return redirect('https://davidkingzyb.github.io/blog.html')

if __name__=='__main__':
    app.debug=True
    app.run()
