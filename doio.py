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
#  2016/03/21 by DKZ https://davidkingzyb.github.io

def dotty(tty):
    ttyarr=tty.split(' ')
    switch={
    'error':onError,
    'welcome':doWelcome,
    'help':doHelp,
    'contact':doContact,
    'lsproject':doLsProject,
    'home':doHome,
    'blog':doBlog,
    'cubex3':doCubex3,
    'duibai':doDuibai,
    'zengxin':doZengXin,
    'egretInit':doEgretInit,
    'wtf':doWebToolFunction,
    'webtoolfunction':doWebToolFunction,
    'commentTitle':doCommentTitle,
    'canvasTrigger':doCanvasTrigger,
    }

    if len(ttyarr)>1:
        return switch.get(ttyarr[0],switch['error'])(ttyarr[1])
    else:
        return switch.get(ttyarr[0],switch['error'])()

def doHelp(ttyarg='default'):
    switch={
'error':"""-wo.io: argument error 
use -help find useable command""",
'default':"""
===================== help ==========================
-welcome             :show welcome infomation
-help [command]      :show command help infomation
-lsproject           :show DKZ's Project list
-----------------------------------------------------
-contact             :show contact infomation
-----------------------------------------------------
-home                :DKZ's HOME
-blog [page index]   :DKZ's BLOG 
-----------------------------------------------------   
-cubex3              :CubeX3 a indie game by DKZ
-duibai [dialogue]   :search dialogue from duibai
-zengxin             :DKZ's father paint page
-----------------------------------------------------
-canvasTrigger       :a canvas lib
-wtf/webtoolfunction :useful web tool function lib
-commentTitle        :big comment title 
-egretInit           :egret tool lib
=====================================================
""",
'welcome':'-welcome show welcome infomation'
    }
    return switch.get(ttyarg,switch['error'])

def doLsProject(ttyarg='default'):
    switch={
    'default':'todo default'
    }
    return switch.get(ttyarg,switch['default'])

def doZengXin(ttyarg='default'):
    switch={
    'default':'todo default'
    }
    return switch.get(ttyarg,switch['default'])

def doBlog(ttyarg='default'):
    switch={
    'default':'todo default'
    }
    return switch.get(ttyarg,switch['default'])

def doDuibai(ttyarg='default'):
    switch={
    'default':'todo default'
    }
    return switch.get(ttyarg,switch['default'])

def doCubex3(ttyarg='default'):
    switch={
    'default':'todo default'
    }
    return switch.get(ttyarg,switch['default'])

def doEgretInit(ttyarg='default'):
    switch={
    'default':'todo default'
    }
    return switch.get(ttyarg,switch['default'])

def doContact(ttyarg='default'):
    switch={
    'default':'todo default'
    }
    return switch.get(ttyarg,switch['default'])

def doCanvasTrigger(ttyarg='default'):
    switch={
    'default':'todo default'
    }
    return switch.get(ttyarg,switch['default'])

def doWebToolFunction(ttyarg='default'):
    switch={
    'default':'todo default'
    }
    return switch.get(ttyarg,switch['default'])

def doWelcome(ttyarg='default'):
    switch={
    'default':'todo default'
    }
    return switch.get(ttyarg,switch['default'])

def doCommentTitle(ttyarg='default'):
    switch={
    'default':'todo default'
    }
    return switch.get(ttyarg,switch['default'])

def doHome(ttyarg='default'):
    switch={
    'default':'todo default'
    }
    return switch.get(ttyarg,switch['default'])

def onError(ttyarg='default'):
    return """-wo.io: command not found 
use -help [arg] find useable command"""


def test():
    help=dotty('help')
    print(help)
    help_welcome=dotty('help welcome')
    print(help_welcome)
    xxx=dotty('xx fe')
    print(xxx)
    help_xxx=dotty('help fcc')
    print(help_xxx)



if __name__ == '__main__':
    test()
