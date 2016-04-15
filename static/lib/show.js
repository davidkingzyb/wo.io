/////////////////////////////////////////////////
//                                             //  
//                               __            //  
//   __    __   _____           |__|  _____    //  
//  |  |/\|  | /     \   ____   |  | /     \   //  
//  |        ||   o   | |    |  |  ||   o   |  //  
//  |___/\___| \_____/  |____|  |__| \_____/   //  
/////////////////////////////////////////////////
//  2016/04/15 by DKZ https://davidkingzyb.github.io
var show=(function(){
    function show(){

    };
    show.init=function(woiobg){
        this.woiobg=woiobg;
        console.log(woiobg)
    }
    show.randomColor=function(){
        return parseInt(Math.random()*0xFFFFFF,16);
    };
    show.changeEyeColor=function(color){
        console.log(this.woiobg)
    }
    return show;
})();