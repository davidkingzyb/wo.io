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
        //console.log('input: ',wtf.$('#input').value)
    }
}