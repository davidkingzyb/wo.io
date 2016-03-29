/////////////////////////////////////////////////
//                                             //  
//                               __            //  
//   __    __   _____           |__|  _____    //  
//  |  |/\|  | /     \   ____   |  | /     \   //  
//  |        ||   o   | |    |  |  ||   o   |  //  
//  |___/\___| \_____/  |____|  |__| \_____/   //  
/////////////////////////////////////////////////
//  2016/03/20 by DKZ https://davidkingzyb.github.io

wtf.loadScript('../static/lib/woiobg.js',function(){
    console.log('woiobg load');
});

wtf.$('#title').setAttribute('class','animated fadeOut');

setTimeout(function(){
    wtf.$('#terminal').setAttribute('class','');
    wtf.$('#input').focus();
},10000);

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
                wtf.$('#show').innerHTML+=d.output;
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
