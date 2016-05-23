# coding: utf-8
"""

=========================================
                                         
                             __          
 __    __   _____           |__|  _____  
|  |/\|  | /     \   ____   |  | /     \ 
|        ||   o   | |    |  |  ||   o   |
|___/\___| \_____/  |____|  |__| \_____/ 
=========================================
2016/05/06 by DKZ https://davidkingzyb.github.io

"""
def wrapTag(tag,value,attr):
    return '<'+tag+' '+attr+'>'+value+'</'+tag+'>' 

urlmap={
    'home':'http://davidkingzyb.github.io/home.html',
    'blog':'http://davidkingzyb.github.io/blog.html',
    'cubext':'http://cubex3.sinaapp.com',
    'duibai':'http://dialogue.sinaapp.com',
    'zengxin':'http://zengxin.sinaapp.com',
    'egretInit':'https://github.com/davidkingzyb/egretInit',
    'canvasTrigger':'https://github.com/davidkingzyb/canvasTrigger',
    'commentTitle':'https://github.com/davidkingzyb/commentTitle',
    'wtf':'https://github.com/davidkingzyb/WebToolFunction',
    'woio':'http://dkzhome.sinaapp.com',
    'clio':'https://github.com/davidkingzyb/CLIoutput',
}

help="""
===================== HELPS =======================
-welcome             :show welcome infomation
-help [command]      :show command help infomation
-lsproject           :show DKZ's Project list
-all                 :show ALL 
-ct [title]          :make a big comment title
-eval [script]       :execute script
-wo                  :WO show
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
-clio                :Command Line Interface Output
===================================================
"""

projls="""
================= Project List ====================
-%(home)s                :DKZ's HOME
-%(blog)s                :DKZ's BLOG 
*wo.io               :WO.IO
--------------------------------------------------   
-%(cubext)s              :CubeX3 a indie game by DKZ
-%(duibai)s [dialogue]   :search movie dialogue 
-%(zengxin)s             :DKZ's father paint page
---------------------- github --------------------
-%(canvasTrigger)s       :a canvas chart lib
-%(wtftwebtoolfunction)s :useful web tool function lib
-%(commentTitle)s        :big comment title 
-%(egretInit)s           :egret tool lib
-%(clio)s                :Command Line Interface Output
===================================================
"""%{
    'home':wrapTag('a','home','href="'+urlmap['home']+'"'),
    'blog':wrapTag('a','blog','href="'+urlmap['blog']+'"'),
    'cubext':wrapTag('a','cubex3','href="'+urlmap['cubext']+'"'),
    'duibai':wrapTag('a','duibai','href="'+urlmap['duibai']+'"'),
    'zengxin':wrapTag('a','zengxin','href="'+urlmap['zengxin']+'"'),
    'egretInit':wrapTag('a','egretInit','href="'+urlmap['egretInit']+'"'),
    'canvasTrigger':wrapTag('a','canvasTrigger','href="'+urlmap['canvasTrigger']+'"'),
    'commentTitle':wrapTag('a','commentTitle','href="'+urlmap['commentTitle']+'"'),
    'wtftwebtoolfunction':wrapTag('a','wtf/webtoolfunction','href="'+urlmap['wtf']+'"'),
    'clio':wrapTag('a','clio','href="'+urlmap['clio']+'"')
}

projls_zh="""
==================== 项目列表 ======================
-%(home)s                :我的主页
-%(blog)s                :我的博客 
*wo.io               :WO.IO
--------------------------------------------------   
-%(cubext)s              :一个独立游戏
-%(duibai)s [dialogue]   :台词查询分享 
-%(zengxin)s             :爸爸的主页
---------------------- github --------------------
-%(canvasTrigger)s       :一个canvas图表工具
-%(wtftwebtoolfunction)s :一个web方法库
-%(commentTitle)s        :用来添加证书和一个大标题 
-%(egretInit)s           :快速构建egret游戏
-%(clio)s                :命令行输出工具
===================================================
"""%{
    'home':wrapTag('a','home','href="'+urlmap['home']+'"'),
    'blog':wrapTag('a','blog','href="'+urlmap['blog']+'"'),
    'cubext':wrapTag('a','cubex3','href="'+urlmap['cubext']+'"'),
    'duibai':wrapTag('a','duibai','href="'+urlmap['duibai']+'"'),
    'zengxin':wrapTag('a','zengxin','href="'+urlmap['zengxin']+'"'),
    'egretInit':wrapTag('a','egretInit','href="'+urlmap['egretInit']+'"'),
    'canvasTrigger':wrapTag('a','canvasTrigger','href="'+urlmap['canvasTrigger']+'"'),
    'commentTitle':wrapTag('a','commentTitle','href="'+urlmap['commentTitle']+'"'),
    'wtftwebtoolfunction':wrapTag('a','wtf/webtoolfunction','href="'+urlmap['wtf']+'"'),
    'clio':wrapTag('a','clio','href="'+urlmap['clio']+'"')
}

contact="""
DKZ
--------------------------
email  davidkingzyb@qq.com
qq     529166486
weibo  %(weibo)s
--------------------------
%(home)s
%(github)s
"""

wo="""

    |%(EyeFragShader)s   |%(EyeFSRandom)s     |%(HeadFSRandom)s

    |%(popShow)s         |%(popWO)s           |%(asciiWO)s 

    |%(HeadUp)s          |%(rotateWO)s   


    |%(setWO)s           |%(resetWO)s

    |%(setBgColor)s      |%(setHeadMaterial)s |%(setEyeMaterial)s

    |%(showTitle)s       |%(hideTitle)s  


    |%(TBCtrlInit)s      |%(TBCtrlHalt)s

"""

resume="""
David K Zeng            `_______  `__   __  `_______  
----------------------  |   __  \ |  | /  / |___   /  
website.                |  |  \  \|  |/  /     /  /   
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

resume_zh="""
 曾 彦博                 `_______  `__   __  `_______  
----------------------  |   __  \ |  | /  / |___   /  
website.                |  |  \  \|  |/  /     /  /   
davidkingzyb.github.io  |  |  |  ||   _  \    /  /    
email.                  |  |__|  ||  | \  \  /  /____ 
davidkingzyb@qq.com     |________/|__|  \__\/________|
========================================================
  _____      ___  __  __ 
 /  _  \ ___|   ||  | | |   华南理工大学 
/  ____/|  ___  ||  |_| |     电子商务         2011-2015
\______/|_______||______|                     管理学学士
========================================================
  _____   __  __ _______  
 /  _  \ \  \/_/|   __  | 2011-2014
/  ____/ _\  \  |    ___| 百步梯 美工部 
\______//_/\__\ |___|      * 部长
                           - 海报设计                
-------------------------------------------------------
2015.4-12    每日Q游戏             * 前端开发工程师
              - HTML5 游戏主程
-------------------------------------------------------
2016.3-      速聘信息技术有限公司    * 前端开发工程师
              - 网页前端开发 架构                             
=========================================================
                             __                   
 _______  __  __  _____     |__|  输入 
|   __  ||  |/_/ /     \    |  |       -lsproject
|    ___||   |  |   o   |___|  | 
|___|    |___|   \_____/ \_____/          查看项目列表
=========================================================
                     &copy;2016 by DKZ
"""

All="""
    |%(home)s            |%(blog)s

    |%(cubext)s          |%(duibai)s          |%(zengxin)s

    |%(egretInit)s       |%(canvasTrigger)s   |%(commentTitle)s

    |%(WebToolFunction)s |%(CLIO)s

    |%(contact)s         |%(resume)s


    |%(welcome)s         |%(wo)s

    |%(lsproject)s       |%(all)s             |%(help)s         

"""

cvfail="""
==============================================================
- 2014/1-6          :ali baidu tencent 
                     china-unicom -mobile -telecom 
                     zhihu douban netease
                     4399 ... !accenture !youmi 
- 2015/11           :meiriQ
- 2016/3            :tencent douyu netease ... !alog
--------------------------------------------------------------
"""

why="""
==============================================
-why WO.IO ?

The development of user interface is
 from low dimension to high dimension

    Command Line --> GUI --> 3D

So webgl is the future, this project
is a attempt to build future website and
user interface.

try -help to find out how to use it.
----------------------------------------------
"""




