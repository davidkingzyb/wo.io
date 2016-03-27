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

wtf.$('#input').onkeydown=function(e){
    if(e.keyCode===13||e.which===13){
        var tty=wtf.$('#input').value;
        wtf.$('#input').value='';
        wtf.$('#show').innerHTML+='\n-'+tty+'\n';
        wtf.post('io','tty='+tty,function(data){
            var d=JSON.parse(data);
            if(d.flag=='ok'){
                wtf.$('#show').innerHTML+=d.output;
            }
        })
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
