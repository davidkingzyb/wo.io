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
import commentTitle


def dotty(tty):
    ttyarr=tty.split(' ')
    switch={
    'error':onError,
    'welcome':doWelcome,
    'help':doHelp,
    'contact':doContact,
    'ct':doCT,
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
===================== HELPS =======================
-welcome             :show welcome infomation
-help [command]      :show command help infomation
-lsproject           :show DKZ's Project list
-all                 :show ALL 
-ct [title]          :make a big comment title
--------------------------------------------------
-contact             :show contact infomation
--------------------------------------------------
-home                :DKZ's HOME
-blog [pageIndex]    :DKZ's BLOG 
--------------------------------------------------   
-cubex3              :CubeX3 a indie game by DKZ
-duibai [dialogue]   :search movie dialogue 
-zengxin             :DKZ's father paint page
--------------------------------------------------
-canvasTrigger       :a canvas lib
-wtf/webtoolfunction :useful web tool function lib
-commentTitle        :big comment title 
-egretInit           :egret tool lib
===================================================
""",
'welcome':'-welcome     :show welcome infomation',
'lsproject':'-lsproject     :show DKZ\'s Project list',
'ct':'-ct [commentTitle]   :make a big comment title (use commentTitle) \n arg:commentTitle',
'contact':'-contact [qq/email/weibo/github]  :show contact infomation',
'home':'-home     :DKZ\'s HOME \n <a href="http://davidkingzyb.github.io">https://davidkingzyb.github.io</a>',
'blog':'-blog     :DKZ\'s BLOG \n <a href="http://davidkingzyb.github.io/blog.html">http://davidkingzyb.github.io/blog.html</a>',
'cubex3':'-cubex3    :a indie game by DKZ \n <a href="http://cubex3.sinaapp.com">http://cubex3.sinaapp.com</a>',
'duibai':'-duibai [曾今]  :search movie dialogue from duibai \n <a href="http://dialogue.sinaapp.com">http://dialogue.sinaapp.com</a>',
'zengxin':'-zengxin   :my father\'s paint page \n <a href="http://zengxin.sinaapp.com">http://zengxin.sinaapp.com</a>',
'canvasTrigger':'-canvasTrigger    :a canvas lib \n <a href="https://github.com/davidkingzyb/canvasTrigger">https://github.com/davidkingzyb/canvasTrigger</a>',
'wtf':'-wtf    :useful web tool function lib \n <a href="https://github.com/davidkingzyb/WebToolFunction">https://github.com/davidkingzyb/WebToolFunction</a>',
'webtoolfunction':'-webtoolfunction    :useful web tool function lib \n <a href="https://github.com/davidkingzyb/WebToolFunction">https://github.com/davidkingzyb/WebToolFunction</a>',
'commentTitle':'-commentTitle    :big comment title you can use -ct [title] try it \n <a href="https://github.com/davidkingzyb/commentTitle">https://github.com/davidkingzyb/commentTitle</a>',
'egretInit':'-egretInit    :egret tool lib build egret project quickly \n <a href="https://github.com/davidkingzyb/egretInit>https://github.com/davidkingzyb/egretInit</a>',
'all':'-all     :show ALL'
    }
    return switch.get(ttyarg,switch['error'])

def doLsProject(ttyarg='default'):
    switch={
    'default':"""
================= Project List ====================
-home                :DKZ's HOME
-blog                :DKZ's BLOG 
*wo.io               :WO.IO
--------------------------------------------------   
-cubex3              :CubeX3 a indie game by DKZ
-duibai [dialogue]   :search movie dialogue 
-zengxin             :DKZ's father paint page
---------------------- github --------------------
-canvasTrigger       :a canvas lib
-wtf/webtoolfunction :useful web tool function lib
-commentTitle        :big comment title 
-egretInit           :egret tool lib
===================================================
""",
    }
    return switch.get(ttyarg,switch['default'])

def doCT(ttyarg='your input error'):
    s=''
    l=commentTitle.doComment(ttyarg)
    for x in l:
        s =s +x+'\n'
    return s

def doZengXin(ttyarg='default'):
    t=doCT('ZengXin')
    switch={
    'default':t+'\n --------------------------------- \n'+'my father\'s paint page'+'\n<a href="http://zengxin.sinaapp.com">http://zengxin.sinaapp.com</a>'
    }
    return switch.get(ttyarg,switch['default'])

def doBlog(ttyarg='default'):
    t=doCT('BLOG')
    switch={
    'default':t+'\n --------------------------------- \n'+'DKZ\'s BLOG  '+'\n<a href="http://davidkingzyb.github.io/blog.html">http://davidkingzyb.github.io/blog.html</a>',
    }
    return switch.get(ttyarg,switch['default'])

def doDuibai(ttyarg='default'):
    t=doCT('duibai')
    r=t+'\n --------------------------------- \n'+'search movie dialogue from duibai \ntry -duibai [dialogue] \n<a href="http://dialogue.sinaapp.com">http://dialogue.sinaapp.com</a>'
    if ttyarg=='default':
        return r
    else:
        return 'aa'#todo

def doCubex3(ttyarg='default'):
    t=doCT('CubeX3')
    switch={
    'default':t+'\n --------------------------------- \n'+'a indie game by DKZ \n* construct puzzle game'+'\n<a href="http://cubex3.sinaapp.com">http://cubex3.sinaapp.com</a>'
    }
    return switch.get(ttyarg,switch['default'])

def doEgretInit(ttyarg='default'):
    t=doCT('eI')
    switch={
    'default':t+'\n --------------------------------- \n'+'build egret project quickly \n* some useful function in egret game engine \n* automatic define resoure \n* time base animation controler \n* debug tool'+'\n<a href="https://github.com/davidkingzyb/egretInit>https://github.com/davidkingzyb/egretInit</a>'
    }
    return switch.get(ttyarg,switch['default'])

def doContact(ttyarg='default'):
    switch={
    'default':"""
DKZ
--------------------------
email  davidkingzyb@qq.com
qq     529166486
weibo  @__DKZ__
--------------------------
%(home)s
%(github)s
"""%{'home':wrapTag('a','home','href="https://davidkingzyb.github.io'),'github':wrapTag('a','github','href="https://github.com/davidkingzyb')}
    }
    return switch.get(ttyarg,switch['default'])

def doCanvasTrigger(ttyarg='default'):
    t=doCT('cT')
    switch={
    'default':t+'\n --------------------------------- \n'+'Canvas tools libary \n* For build canvas chart \n* define object and dispatch event to this object \n* Time-base animation controler \n'+wrapTag('a','https://github.com/davidkingzyb/canvasTrigger','href="https://github.com/davidkingzyb/canvasTrigger"')
    }
    return switch.get(ttyarg,switch['default'])

def doWebToolFunction(ttyarg='default'):
    t=doCT('wtf')
    switch={
    'default':t+'\n --------------------------------- \n'+'some useful web tool function \n* wtf.js a web tool function javascript lib \n* init.less css init \n* spiderman.py a simple web spider \n* runServer.py a simple web server \n* wtf some useful python web tool function\n'+wrapTag('a','https://github.com/davidkingzyb/WebToolFunction','href="https://github.com/davidkingzyb/WebToolFunction"')
    }
    return switch.get(ttyarg,switch['default'])

def doWelcome(ttyarg='default'):
    Welcome=doCT('Welcome')
    t=doCT('to wo.io')
    switch={
    'default':Welcome+t+'\n----------------------------------------- \n'+'date: '+commentTitle.date+'    &copy 2016 by DKZ'
    }
    return switch.get(ttyarg,switch['default'])

def doCommentTitle(ttyarg='default'):
    t=doCT('ct')
    switch={
    'default':t+'\n --------------------------------- \n'+'make big comment title \ntry -ct [title] use commentTitle\n'+wrapTag('a','https://github.com/davidkingzyb/commentTitle','href="https://github.com/davidkingzyb/commentTitle"')
    }
    return switch.get(ttyarg,switch['default'])

def doHome(ttyarg='default'):
    t=doCT('home')
    switch={
    'default':t+'\n --------------------------------- \n'+'DKZ\'s Home\n'+wrapTag('a','http://davidkingzyb.github.io/','href="http://davidkingzyb.github.io/"')
    }
    return switch.get(ttyarg,switch['default'])

def onError(ttyarg='default'):
    return """-wo.io: command not found 
use -help [arg] find useable command"""

def wrapTag(tag,value,attr):
    return '<'+tag+' '+attr+'>'+value+'</'+tag+'>' 

def test():
    tty=raw_input()
    print(dotty(tty))
    test()





if __name__ == '__main__':
    test()
