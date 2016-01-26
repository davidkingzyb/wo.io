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


from flask import Flask
#from flask import request
#from flask import render_template
from flask import redirect
#from flask import abort
#from flask import url_for
#from flask import Markup
#from flask import make_response

app=Flask(__name__)

@app.route('/')
def index():
    return redirect('https://davidkingzyb.github.io')


if __name__=='__main__':
    app.debug=True
    app.run()
