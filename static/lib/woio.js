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

setTimeout(function(){
    wtf.$('#terminal').setAttribute('class','');
    wtf.$('#input').focus();
},10000);

function doOutput(output){
    var script=/{{javascript:.*?}}/.exec(output);
    if(script.length>0){
        var s=script[0].replace(/"/g,"'");
        var outA=s.replace('{{','<a href="').replace('}}','">eval</a>')
        output=output.replace(script[0],outA);
        wtf.$id('scripts').innerHTML=s.replace('{{javascript:','<img src="null.png" onError="').replace('}}','">')
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
    wtf.$('#show').innerHTML+='\n-'+t+'\n';
    wtf.post('io','tty='+t,function(data){
        var d=JSON.parse(data);
        if(d.flag=='ok'){
                wtf.$('#show').innerHTML+=d.output;
            }
    });
}

onAClick('welcome');

var ISBG=false;
try{
    wtf.loadScript('../static/lib/three.js',function(){
        //console.log('load three.js');
        wtf.loadScript('../static/lib/OBJLoader.js',function(){
            //console.log('load OBJLoader.js');
            wtf.loadScript('../static/lib/tween.min.js',function(){
                //console.log('load tween.js');
                wtf.loadScript('../static/lib/TrackballControls.js',function(){
                    //console.log('load trackballcontrols.js');
                    wtf.loadScript('../static/lib/woiobg.js',function(){
                        console.log('woiobg ok');
                        ISBG=true;
                    });
                });
            });
        });
    });
}catch(e){
    console.log('woiobg fail');
}










