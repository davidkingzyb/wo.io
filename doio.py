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
import spiderman
import json

urlmap={
    'home':'http://davidkingzyb.github.io',
    'blog':'http://davidkingzyb.github.io/blog.html',
    'cubext':'http://cubex3.sinaapp.com',
    'duibai':'http://dialogue.sinaapp.com',
    'zengxin':'http://zengxin.sinaapp.com',
    'egretInit':'https://github.com/davidkingzyb/egretInit',
    'canvasTrigger':'https://github.com/davidkingzyb/canvasTrigger',
    'commentTitle':'https://github.com/davidkingzyb/commentTitle',
    'wtf':'https://github.com/davidkingzyb/WebToolFunction',
    'woio':'http://dkzhome.sinaapp.com',
}

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
    'all':doAll,
    'eval':doEval,
    'resume':doResume,
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
-blog                :DKZ's BLOG 
-resume              :DKZ's Resume
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
'home':'-home     :DKZ\'s HOME \n <a href="'+urlmap['home']+'">'+urlmap['home']+'</a>',
'blog':'-blog     :DKZ\'s BLOG \n <a href="'+urlmap['blog']+'">'+urlmap['blog']+'</a>',
'cubex3':'-cubex3    :a indie game by DKZ \n <a href="'+urlmap['cubext']+'">'+urlmap['cubext']+'</a>',
'duibai':'-duibai [曾今]  :search movie dialogue from duibai \n <a href="'+urlmap['duibai']+'">'+urlmap['duibai']+'</a>',
'zengxin':'-zengxin   :my father\'s paint page \n <a href="'+urlmap['zengxin']+'">'+urlmap['zengxin']+'</a>',
'canvasTrigger':'-canvasTrigger    :a canvas lib \n <a href="'+urlmap['canvasTrigger']+'">'+urlmap['canvasTrigger']+'</a>',
'wtf':'-wtf    :useful web tool function lib \n <a href="'+urlmap['wtf']+'">'+urlmap['wtf']+'</a>',
'webtoolfunction':'-webtoolfunction    :useful web tool function lib \n <a href="'+urlmap['wtf']+'">'+urlmap['wtf']+'</a>',
'commentTitle':'-commentTitle    :big comment title you can use -ct [title] try it \n <a href="'+urlmap['commentTitle']+'">'+urlmap['commentTitle']+'</a>',
'egretInit':'-egretInit    :egret tool lib build egret project quickly \n <a href="'+urlmap['egretInit']+'">'+urlmap['egretInit']+'</a>',
'all':'-all     :show ALL',
'eval':'-eval      :execute script',
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
-canvasTrigger       :a canvas chart lib
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
    'default':t+'\n --------------------------------- \n'+'my father\'s paint page'+'\n<a href="'+urlmap['zengxin']+'">'+urlmap['zengxin']+'</a>'
    }
    return switch.get(ttyarg,switch['default'])

def doBlog(ttyarg='default'):
    t=doCT('BLOG')
    switch={
    'default':t+'\n --------------------------------- \n'+'DKZ\'s BLOG  '+'\n<a href="'+urlmap['blog']+'">'+urlmap['blog']+'</a>',
    }
    return switch.get(ttyarg,switch['default'])

def doDuibai(ttyarg='default'):
    t=doCT('duibai')
    r=t+'\n --------------------------------- \n'+'search movie dialogue from duibai \ntry -duibai [dialogue] \n<a href="'+urlmap['duibai']+'">'+urlmap['duibai']+'</a>'
    if ttyarg=='default':
        return r
    else:
        duibai=spiderman.post('http://dialogue.sinaapp.com/io',{'dialogue':ttyarg.encode('UTF-8')})
        d=json.loads(duibai)
        if d['flag']=='ok':
            output="""
name:%(name)s
director:%(director)s
actor:%(actor)s 
---------------------------"""%d
            for x in d['dialogue']:
                output=output+'\n'+x
            return output
        else:
            return 'cant find dialogue please try other key word or visit '+wrapTag('a','duibai','href="'+urlmap['duibai']+'"')


def doCubex3(ttyarg='default'):
    t=doCT('CubeX3')
    switch={
    'default':t+'\n --------------------------------- \n'+'a indie game by DKZ \n* construct puzzle game'+'\n<a href="'+urlmap['cubext']+'">'+urlmap['cubext']+'</a>'
    }
    return switch.get(ttyarg,switch['default'])

def doEgretInit(ttyarg='default'):
    t=doCT('eI')
    switch={
    'default':t+'\n --------------------------------- \n'+'build egret project quickly \n* some useful function in egret game engine \n* automatic define resoure \n* time base animation controler \n* debug tool'+'\n<a href="'+urlmap['egretInit']+'">'+urlmap['egretInit']+'</a>'
    }
    return switch.get(ttyarg,switch['default'])

def doContact(ttyarg='default'):
    switch={
    'default':"""
DKZ
--------------------------
email  davidkingzyb@qq.com
qq     529166486
weibo  %(weibo)s
--------------------------
%(home)s
%(github)s
"""%{'home':wrapTag('a','home','href="'+urlmap['home']+'"'),
'github':wrapTag('a','github','href="https://github.com/davidkingzyb"'),
'weibo':wrapTag('a','@__DKZ__','href="http://weibo.com/davidkingzyb"')
}
    }
    return switch.get(ttyarg,switch['default'])

def doCanvasTrigger(ttyarg='default'):
    t=doCT('cT')
    switch={
    'default':t+'\n --------------------------------- \n'+'Canvas tools libary \n* For build canvas chart \n* define object and dispatch event to this object \n* Time-base animation controler \n'+wrapTag('a',urlmap['canvasTrigger'],'href="'+urlmap['canvasTrigger']+'"')
    }
    return switch.get(ttyarg,switch['default'])

def doWebToolFunction(ttyarg='default'):
    t=doCT('wtf')
    switch={
    'default':t+'\n --------------------------------- \n'+'some useful web tool function \n* wtf.js a web tool function javascript lib \n* init.less css init \n* spiderman.py a simple web spider \n* runServer.py a simple web server \n* wtf some useful python web tool function\n'+wrapTag('a',urlmap['wtf'],'href="'+urlmap['wtf']+'"')
    }
    return switch.get(ttyarg,switch['default'])

def doWelcome(ttyarg='default'):
    Welcome=doCT('Welcome')
    t=doCT('to wo.io')
    switch={
    'default':Welcome+t+'\n----------------------------------------- \n'+'date: '+commentTitle.date+'    &copy 2016 by DKZ'+'\ninput -help find help infomation'
    }
    return switch.get(ttyarg,switch['default'])

def doCommentTitle(ttyarg='default'):
    t=doCT('ct')
    switch={
    'default':t+'\n --------------------------------- \n'+'make big comment title \ntry -ct [title] use commentTitle\n'+wrapTag('a',urlmap['commentTitle'],'href="'+urlmap['commentTitle']+'"')
    }
    return switch.get(ttyarg,switch['default'])

def doHome(ttyarg='default'):
    t=doCT('home')
    switch={
    'default':t+'\n --------------------------------- \n'+'DKZ\'s Home\n'+wrapTag('a',urlmap['home'],'href="'+urlmap['home']+'"')
    }
    return switch.get(ttyarg,switch['default'])



def doAll(ttyarg='default'):
    switch={
    'default':"""
    |%(home)s           |%(blog)s

    |%(cubext)s         |%(duibai)s         |%(zengxin)s

    |%(egretInit)s      |%(canvasTrigger)s  |%(commentTitle)s

    |%(WebToolFunction)s

    |%(contact)s        |%(resume)s


    |%(welcome)s

    |%(lsproject)s      |%(all)s            |%(help)s         

"""%{
    'home':wrapTag('a','home','href="'+urlmap['home']+'"'),
    'blog':wrapTag('a','blog','href="'+urlmap['blog']+'"'),
    'cubext':wrapTag('a','cubex3','href="'+urlmap['cubext']+'"'),
    'duibai':wrapTag('a','duibai','href="'+urlmap['duibai']+'"'),
    'zengxin':wrapTag('a','zengxin','href="'+urlmap['zengxin']+'"'),
    'egretInit':wrapTag('a','egretInit','href="'+urlmap['egretInit']+'"'),
    'canvasTrigger':wrapTag('a','canvasTrigger','href="'+urlmap['canvasTrigger']+'"'),
    'commentTitle':wrapTag('a','commentTitle','href="'+urlmap['commentTitle']+'"'),
    'WebToolFunction':wrapTag('a','WebToolFunction','href="'+urlmap['wtf']+'"'),
    'contact':wrapTag('a','contact','href="javascript:onAClick(\'contact\')"'),
    'resume':wrapTag('a','resume','href="javascript:onAClick(\'resume\')"'),
    'welcome':wrapTag('a','welcome','href="javascript:onAClick(\'welcome\')"'),
    'lsproject':wrapTag('a','lsproject','href="javascript:onAClick(\'lsproject\')"'),
    'all':wrapTag('a','all','href="javascript:onAClick(\'all\')"'),
    'help':wrapTag('a','help','href="javascript:onAClick(\'help\')"'),
}
    }
    return switch.get(ttyarg,switch['default'])

def doEval(ttyarg='alert("try -eval alert(\"hello\")")'):
    #return '<img src="null.gif" class="nullimg" onerror="'+ttyarg+'"/>'
    return 'this is a test command'

def doResume(ttyarg=''):
    resume="""
David K Zeng            `_______  `__   __  `_______  
----------------------  |   __  \ |  | /  / |___   /  
home.                   |  |  \  \|  |/  /     /  /   
davidkingzyb.github.io  |  |  |  ||   _  \    /  /    
email.                  |  |__|  ||  | \  \  /  /____ 
davidkingzyb@qq.com     |________/|__|  \__\/________|
========================================================
  _____      ___  __  __ 
 /  _  \ ___|   ||  | | | South China University 
/  ____/|  ___  ||  |_| | of Technology      2011-2015
\______/|_______||______|         B.Admin E-Commerce
========================================================
  _____   __  __ _______  
 /  _  \ \  \/_/|   __  | 2011-2014
/  ____/ _\  \  |    ___| BBT Art Design Department 
\______//_/\__\ |___|      * Leader
                           - post & web design                
-------------------------------------------------------
2015.4-12    MeiriQ Game          * Front-End Engineer
              - HTML5 games develope
-------------------------------------------------------
2016.3-      Elitez               * Front-End Engineer
              - Website develope                             
=========================================================
                             __                   
 _______  __  __  _____     |__|  input 
|   __  ||  |/_/ /     \    |  |       -lsproject
|    ___||   |  |   o   |___|  | 
|___|    |___|   \_____/ \_____/  to get project list
=========================================================
                     &copy;2016 by DKZ
"""
    return resume


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
