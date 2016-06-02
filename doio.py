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
import clio
import spiderman
import json
import datetime
import woiodata
import random


date=datetime.datetime.now().strftime('%Y/%m/%d')

urlmap=woiodata.urlmap

def dotty(tty):
    ttyarr=tty.split(' ')
    switch={
    'error':onError,
    'welcome':doWelcome,
    'help':doHelp,
    'contact':doContact,
    'ct':doCT,
    'lsproject':doLsProject,
    'lsproj':doLsProject,
    'proj':doLsProject,
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
    'wo':doWO,
    'cv':doResume,
    'clio':doClio,
    'cvfail':doCVFail,
    'why':doWhy,
    }

    if len(ttyarr)>1:
        return switch.get(ttyarr[0],switch['error'])(ttyarr[1])
    else:
        return switch.get(ttyarr[0],switch['error'])()

def doHelp(ttyarg='default'):
    switch={
'error':"""-wo.io: argument error 
use -help find useable command""",
'default':woiodata.help,
'welcome':'-welcome     :show welcome infomation',
'lsproject':'-lsproject     :show DKZ\'s Project list',
'lsproj':'-lsproj     :show DKZ\'s Project list',
'proj':'-proj     :show DKZ\'s Project list',
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
'wo':'-wo [showfunction]      :exec wo show',
'cv':'-cv       :DKZ\'s resume',
'resume':'-resume      :DKZ\'s resume',
'clio':'-clio      :Command Line Interface Output',
    }
    return switch.get(ttyarg,switch['error'])

def doLsProject(ttyarg='default'):
    switch={
    'default':woiodata.projls,
    'zh':woiodata.projls_zh,
    }
    return switch.get(ttyarg,switch['default'])

def doCT(ttyarg='your input error'):
    return clio.dotitle(ttyarg)

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
    r=t+'\n --------------------------------- \n'+'- Movie dialogue search and share website\n- Using spider collect subtitle files and add them to database\n'+'search movie dialogue from duibai \ntry -duibai [dialogue] \n<a href="'+urlmap['duibai']+'">'+urlmap['duibai']+'</a>'
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
    'default':t+'\n --------------------------------- \n'+'a indie game by DKZ \n- construct puzzle game'+'\n- 2015 Egret Engine development competition the Best Creative Award nominations'+'\n- Include a virtual goods payment system build in the third-party payment platform PayPal’s API'+'\n<a href="'+urlmap['cubext']+'">'+urlmap['cubext']+'</a>'
    }
    return switch.get(ttyarg,switch['default'])

def doEgretInit(ttyarg='default'):
    t=doCT('eI')
    switch={
    'default':t+'\n --------------------------------- \n'+'build egret project quickly \n- some useful function in egret game engine \n- automatic define resoure \n- time base animation controler \n- debug tool'+'\n<a href="'+urlmap['egretInit']+'">'+urlmap['egretInit']+'</a>'
    }
    return switch.get(ttyarg,switch['default'])

def doContact(ttyarg='default'):
    switch={
    'default':woiodata.contact%{'home':wrapTag('a','home','href="'+urlmap['home']+'"'),
'github':wrapTag('a','github','href="https://github.com/davidkingzyb"'),
'weibo':wrapTag('a','@__DKZ__','href="http://weibo.com/davidkingzyb"')
}
    }
    return switch.get(ttyarg,switch['default'])

def doCanvasTrigger(ttyarg='default'):
    t=doCT('cT')
    switch={
    'default':t+'\n --------------------------------- \n'+'Canvas tools libary \n- For build canvas chart \n- define object and dispatch event to this object \n- Time-base animation controler \n'+wrapTag('a',urlmap['canvasTrigger'],'href="'+urlmap['canvasTrigger']+'"')
    }
    return switch.get(ttyarg,switch['default'])

def doWebToolFunction(ttyarg='default'):
    t=doCT('wtf')
    switch={
    'default':t+'\n --------------------------------- \n'+'some useful web tool function \n- wtf.js a web tool function javascript lib \n- init.less css init \n- spiderman.py a simple web spider \n- runServer.py a simple web server \n- wtf some useful python web tool function\n- bd.js a simple MVVM web framework\n'+wrapTag('a',urlmap['wtf'],'href="'+urlmap['wtf']+'"')
    }
    return switch.get(ttyarg,switch['default'])

def doClio(ttyarg='default'):
    t=doCT('CLIoutput')
    switch={
    'default':t+'\n --------------------------------- \n'+'Command Line Interface Output\n- a python lib for making CUI\ntry -clio dotree(json)...\n'+wrapTag('a',urlmap['clio'],'href="'+urlmap['clio']+'"')
    }
    if ttyarg=='default':
        return switch.get(ttyarg,switch['default'])
    else:
        try:
            args=ttyarg.split('(')
            args[1]=args[1][:-1]
            print(args)
            switchargs={
            'dolist':clio.dolist,
            'dojson':clio.dojson,
            'dotree':clio.dotree,
            'dotabel':clio.dotabel,
            'dobar':clio.dobar
            }
            return switchargs.get(args[0])(json.loads(args[1]))
        except:  
            return 'clio error'
    

def doWelcome(ttyarg='default'):
    Welcome=doCT('Welcome')
    t=doCT('to wo.io')
    switch={
    'default':Welcome+t+'\n----------------------------------------- \n'+'date: '+date+'    &copy 2016 by DKZ'+'\ninput -help find help infomation'
    }
    return switch.get(ttyarg,switch['default'])

def doCommentTitle(ttyarg='default'):
    t=doCT('ct')
    switch={
    'default':t+'\n --------------------------------- \n'+'make big comment title \nand add open sources licenses \ntry -ct [title] use commentTitle\n'+wrapTag('a',urlmap['commentTitle'],'href="'+urlmap['commentTitle']+'"')
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
    'default':woiodata.All%{
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
    'wo':wrapTag('a','wo','href="javascript:onAClick(\'wo\')"'),
    'CLIO':wrapTag('a','CLIO','href="'+urlmap['clio']+'"')
}
    }
    return switch.get(ttyarg,switch['default'])

def doWO(ttyarg='default'):
    switch={
    'default':woiodata.wo%{
    'EyeFragShader':wrapTag('a','EyeFragShader','href="javascript:onAClick(\'wo EyeFragShader\')"'),
    'EyeFSRandom':wrapTag('a','EyeFSRandom','href="javascript:onAClick(\'wo EyeFSRandom\')"'),
    'HeadFSRandom':wrapTag('a','HeadFSRandom','href="javascript:onAClick(\'wo HeadFSRandom\')"'),
    'popShow':wrapTag('a','popShow','href="javascript:onAClick(\'wo popShow\')"'),
    'popWO':wrapTag('a','popWO','href="javascript:onAClick(\'wo popWO\')"'),
    'asciiWO':wrapTag('a','asciiWO','href="javascript:onAClick(\'wo asciiWO\')"'),
    'HeadUp':wrapTag('a','HeadUp','href="javascript:onAClick(\'wo HeadUp\')"'),
    'rotateWO':wrapTag('a','rotateWO','href="javascript:onAClick(\'wo rotateWO\')"'),
    'setWO':wrapTag('a','setWO','href="javascript:onAClick(\'wo setWO\')"'),
    'resetWO':wrapTag('a','resetWO','href="javascript:onAClick(\'wo resetWO\')"'),
    'setBgColor':wrapTag('a','setBgColor','href="javascript:onAClick(\'wo setBgColor\')"'),
    'setHeadMaterial':wrapTag('a','setHeadMaterial','href="javascript:onAClick(\'wo setHeadMaterial\')"'),
    'setEyeMaterial':wrapTag('a','setEyeMaterial','href="javascript:onAClick(\'wo setEyeMaterial\')"'),
    'showTitle':wrapTag('a','showTitle','href="javascript:onAClick(\'wo showTitle\')"'),
    'hideTitle':wrapTag('a','hideTitle','href="javascript:onAClick(\'wo hideTitle\')"'),
    'TBCtrlInit':wrapTag('a','TBCtrlInit','href="javascript:onAClick(\'wo TBCtrlInit\')"'),
    'TBCtrlHalt':wrapTag('a','TBCtrlHalt','href="javascript:onAClick(\'wo TBCtrlHalt\')"'),
},
    'EyeFragShader':'{{javascript:showing.setEyeFragShader(fs1);showing.fragShaderRender(showing.woiobg.eye.children[0].material);}}',
    'EyeFSRandom':'{{javascript:showing.setEyeFragShader(fs'+str(random.random()*6+1)[0:1]+');showing.fragShaderRender(showing.woiobg.eye.children[0].material);}}',
    'HeadFSRandom':'{{javascript:showing.setHeadFragShader(fs'+str(random.random()*6+1)[0:1]+');showing.fragShaderRender(showing.woiobg.head.children[0].material);}}',
    'popShow':'{{javascript:switchIO();showing.popShow();}}',
    'popWO':'{{javascript:switchIO();showing.popWO();}}',
    'asciiWO':'{{javascript:showing.asciiWO();}}',
    'HeadUp':'{{javascript:switchIO();showing.HeadUp();}}',
    'rotateWO':'{{javascript:switchIO();showing.rotateWO(0,show.degTorad(1),0);}}',
    'setWO':'{{javascript:switchIO();showing.setWO("rotation",0,0,0);}}',
    'resetWO':'{{javascript:switchIO();showing.resetWO();}}',
    'setBgColor':'{{javascript:switchIO();showing.setBgColor(show.randomColor());}}',
    'setHeadMaterial':'{{javascript:switchIO();showing.setHeadMaterial(show.randomColor());}}',
    'setEyeMaterial':'{{javascript:switchIO();showing.setEyeMaterial(show.randomColor());}}',
    'showTitle':'{{javascript:switchIO();show.showTitle("wo show");}}',
    'hideTitle':'{{javascript:switchIO();show.hideTitle();}}',
    'TBCtrlInit':'{{javascript:switchIO();show.TBCtrlInit();}}',
    'TBCtrlHalt':'{{javascript:switchIO();show.TBCtrlHalt();}}',

    }
    return switch.get(ttyarg,switch['default'])

def doEval(ttyarg='alert("try -eval alert(“hello”)")'):
    return 'click -> {{javascript:'+ttyarg+'}}'
    #return 'this is a test command'

def doResume(ttyarg=''):
    if ttyarg=='zh':
        resume=woiodata.resume_zh
    else:
        resume=woiodata.resume
    return resume

def doCVFail(ttyarg=''):
    return woiodata.cvfail

def doWhy(ttyarg=''):
    return woiodata.why


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
