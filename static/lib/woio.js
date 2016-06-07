/////////////////////////////////////////////////
//                                             //  
//                               __            //  
//   __    __   _____           |__|  _____    //  
//  |  |/\|  | /     \   ____   |  | /     \   //  
//  |        ||   o   | |    |  |  ||   o   |  //  
//  |___/\___| \_____/  |____|  |__| \_____/   //  
/////////////////////////////////////////////////
//  2016/03/20 by DKZ https://davidkingzyb.github.io

wtf.$('#title').setAttribute('class','animated fadeOut');

var isIOshow=false;
function switchIO(){
    if(isIOshow){
        wtf.$('#woioterminal').setAttribute('class','hidden');
        isIOshow=false;
    }else{
        wtf.$('#woioterminal').setAttribute('class','');
        wtf.$('#input').focus();
        isIOshow=true;
    }  
}

setTimeout(function(){
    if(!isIOshow){
        switchIO();
    }

},10000);

function showTitle(title){
    wtf.$('#title').innerHTML=title;
    wtf.$('#title').setAttribute('class','');
}

function hideTitle(){
    wtf.$('#title').innerHTML='W O . I O';
    wtf.$('#title').setAttribute('class','hidden');
}

var alerttimer;
function showAlert(alert,hidetime){
    wtf.$('#loading').innerHTML=alert;
    var hidetime=hidetime||3000;
    if(alerttimer){
        clearTimeout(alerttimer);
    }
    wtf.$('#loading').setAttribute('class','');
    alerttimer=setTimeout(function(){
        wtf.$('#loading').setAttribute('class','hidden');
    },hidetime);
}

function doOutput(output){
    var script=/{{javascript:.*?}}/.exec(output);
    if(script){
        if(script.length>0){
            var s=script[0].replace(/"/g,"'");
            var outA=s.replace('{{','<a href="').replace('}}','">eval</a>')
            output=output.replace(script[0],outA);
            wtf.$id('scripts').innerHTML=s.replace('{{javascript:','<img src="null.png" onError="').replace('}}','">')
        } 
    }
    wtf.$('#show').innerHTML+=output;
}

var TTYARR=[];

wtf.$('#input').onkeydown=function(e){
    //console.log(e.keyCode)
    if(e.keyCode===13||e.which===13){
        var tty=wtf.$('#input').value;
        TTYARR.push(tty);
        wtf.$('#input').value='';
        wtf.$('#show').innerHTML+='\n-'+tty+'\n';
        wtf.post('io','tty='+tty,function(data){
            var d=JSON.parse(data);
            if(d.flag=='ok'){
                doOutput(d.output);
            }
        })
    }
    if(e.keyCode===38||e.which===38){
        if(TTYARR.length>=1){
            TTYARR.unshift(wtf.$('#input').value);
            var tty=TTYARR.pop();
            wtf.$('#input').value=tty;
        }
    }
    if(e.keyCode===40||e.which===40){
        if(TTYARR.length>=1){
            TTYARR.push(wtf.$('#input').value);
            var tty=TTYARR.shift();
            wtf.$('#input').value=tty;
        }
    }
}

function onAClick(t){
    if(!isIOshow){
        switchIO();
    }
    wtf.$('#show').innerHTML+='\n-'+t+'\n';
    wtf.post('io','tty='+t,function(data){
        var d=JSON.parse(data);
        if(d.flag=='ok'){
            //wtf.$('#show').innerHTML+=d.output;
            doOutput(d.output);
        }
    });
}

onAClick('welcome');
switchIO();

var ISTHREELOAD=false;
var ISOBJLOADERLOAD=false;
var ISTBCTRLLOAD=false;
var ISTWEENLOAD=false;
var ISACLOAD=false;
var ISBGLOAD=false;

var woiobg;
try{
    wtf.$('#loading').setAttribute('class','');
    wtf.loadScript('../static/lib/three.js',function(){
        ISTWEENLOAD=true;
        wtf.loadScript('../static/lib/OBJLoader.js',function(){
            ISOBJLOADERLOAD=true;
            wtf.loadScript('../static/lib/woiobg.js',function(){
                ISBGLOAD=true;

//main
woiobg=new woioBg();
woiobg.init();
woiobg.loadEye();
woiobg.loadHead('woioHigh',showOn);


            })
        })
        wtf.loadScript('../static/lib/TrackballControls.js',function(){
            ISTBCTRLLOAD=true;
        })
        wtf.loadScript('../static/lib/tween.min.js',function(){
            ISTWEENLOAD=true;
        })
        wtf.loadScript('../static/lib/animationCtrl.js',function(){
            ISACLOAD=true;
        })
    })
}catch(e){
    console.log('woiobg fail');
}

var showing;
function showOn(){
    //console.log('show on')
    wtf.loadScript('../static/lib/show.js',function(){
        if(ISBGLOAD){
            showing=new show(woiobg);
            if(ISTWEENLOAD&&ISTBCTRLLOAD){
                showing.init();
            }
        }
    })
}


window.onkeydown=function(e){
    if (e.keyCode === 120 || e.which === 120) {
        switchIO();
    }
}







