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
    'shanhai':'http://davidkingzyb.tech/shanhai',
    'pccold':'https://github.com/davidkingzyb/pccold',
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
-shanhai             :indie game ShanHai
-duibai [dialogue]   :search movie dialogue 
-zengxin             :DKZ's father paint page
--------------------------------------------------
-canvasTrigger       :a canvas lib
-wtf/webtoolfunction :useful web tool function lib
-commentTitle        :big comment title 
-egretInit           :egret tool lib
-pccold              :douyutv script
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
-%(shanhai)s             :indie game ShanHai
-%(duibai)s [dialogue]   :search movie dialogue 
-%(zengxin)s             :DKZ's father paint page
---------------------- github --------------------
-%(canvasTrigger)s       :a canvas chart lib
-%(wtftwebtoolfunction)s :useful web tool function lib
-%(commentTitle)s        :big comment title 
-%(egretInit)s           :egret tool lib
-%(pccold)s              :douyutv script
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
    'clio':wrapTag('a','clio','href="'+urlmap['clio']+'"'),
    'shanhai':wrapTag('a','shanhai','href="'+urlmap['shanhai']+'"'),
    'pccold':wrapTag('a','pccold','href="'+urlmap['pccold']+'"'),
}

projls_zh="""
==================== 项目列表 ======================
-%(home)s                :我的主页
-%(blog)s                :我的博客 
*wo.io               :WO.IO
--------------------------------------------------   
-%(cubext)s              :一个独立游戏
-%(shanhai)s             :独立游戏 山海
-%(duibai)s [dialogue]   :台词查询分享 
-%(zengxin)s             :爸爸的主页
---------------------- github --------------------
-%(canvasTrigger)s       :一个canvas图表工具
-%(wtftwebtoolfunction)s :一个web方法库
-%(commentTitle)s        :用来添加证书和一个大标题 
-%(egretInit)s           :快速构建egret游戏
-%(pccold)s              :斗鱼录制脚本
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
    'clio':wrapTag('a','clio','href="'+urlmap['clio']+'"'),
    'shanhai':wrapTag('a','shanhai','href="'+urlmap['shanhai']+'"'),
    'pccold':wrapTag('a','pccold','href="'+urlmap['pccold']+'"')
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
              - HTML5 games develope use egret
-------------------------------------------------------
2016.3-12    Elitez               * Front-End Engineer
              - Website develope use avalon
              - chrome plugs                             
=========================================================
                             __                   
 _______  __  __  _____     |__|  input 
|   __  ||  |/_/ /     \    |  |       -lsproject
|    ___||   |  |   o   |___|  | 
|___|    |___|   \_____/ \_____/  to get project list
=========================================================
                     &copy;2017 by DKZ
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
 /  _  \ ___|   ||  | | |      华南理工大学     本科
/  ____/|  ___  ||  |_| |        电子商务      2011-2015
\______/|_______||______|                     
========================================================
  _____   __  __ _______  
 /  _  \ \  \/_/|   __  |      2011-2014
/  ____/ _\  \  |    ___|      百步梯学生创新中心 美工部
\______//_/\__\ |___|           - 海报设计 制作   
-------------------------------------------------------
2015.4-12    每日Q游戏             * 前端开发工程师
    - 使用 egret 引擎制作 HTML5 游戏
-------------------------------------------------------
2016.3-12    速聘信息技术有限公司    * 前端开发工程师
    - 基于 avalon 框架的web端业务逻辑页面开发与维护
    - 负责公司内部使用的chrome插件开发与架构，代替公司原有的
      简历抓取功能，提升公司顾问的工作效率，节约简历获取成本。
========================================================
                             __                   
 _______  __  __  _____     |__|  输入 
|   __  ||  |/_/ /     \    |  |       -lsproject
|    ___||   |  |   o   |___|  | 
|___|    |___|   \_____/ \_____/          查看项目列表
=========================================================
                     &copy;2017 by DKZ
"""

All="""
    |%(home)s            |%(blog)s

    |%(cubext)s          |%(shanhai)s         |%(zengxin)s

    |%(egretInit)s       |%(canvasTrigger)s   |%(commentTitle)s

    |%(WebToolFunction)s |%(CLIO)s            |%(pccold)s

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




