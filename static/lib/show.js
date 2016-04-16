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
        //@woiobg
        //@anmt
        //@isanmtstart
    };
    show.prototype.init=function(woiobg){
        this.woiobg=woiobg;
        var that=this;
        wtf.loadScript('../static/lib/animationsCtrl.js',function(){
            console.log('animationsCtrl ok')
        })
    };
    show.prototype.anmtInit=function(){
        aC_startMainLoop();
        this.anmt=new animationCtrl();
        this.anmt.start();
        this.isanmtstart=true;
    };
    show.prototype.anmtHalt=function(){
        this.anmt.stop();
        this.isanmtstart=false;
        aC_stopMainLoop();
        this.anmt=undefined;
    }
    show.randomColor=function(){
        return parseInt(Math.random()*0xFFFFFF,16);
    };
    show.degTorad=function(deg){
        return deg*Math.PI/180;
    };
    show.prototype.setEyeColor=function(c){
        var materials=[new THREE.MeshLambertMaterial({color:c})];
        var mesh=THREE.SceneUtils.createMultiMaterialObject(this.woiobg.eye_geom,materials);
        mesh.castShadow=true;
        this.woiobg.wo.remove(this.woiobg.eye)
        this.woiobg.eye=mesh;
        this.woiobg.wo.add(this.woiobg.eye);
        this.woiobg.renderer.render(this.woiobg.scene,this.woiobg.camera);
    };
    show.prototype.setHeadColor=function(c){
        var materials=[new THREE.MeshLambertMaterial({color:c})];
        var mesh=THREE.SceneUtils.createMultiMaterialObject(this.woiobg.head_geom,materials);
        mesh.castShadow=true;
        this.woiobg.wo.remove(this.woiobg.head)
        this.woiobg.head=mesh;
        this.woiobg.wo.add(this.woiobg.head);
        this.woiobg.renderer.render(this.woiobg.scene,this.woiobg.camera);
    };
    //@attr:str 'position'||'rotation'||'scale'
    show.prototype.setWO=function(attr,x,y,z){
        this.woiobg.wo[attr].set(x,y,z);
        this.woiobg.renderer.render(this.woiobg.scene,this.woiobg.camera);
    };
    show.prototype.rotateWO=function(stepx,stepy,stepz){
        if(!this.anmt){
            this.anmtInit();
        }
        if(!this.isanmtstart){
            this.anmt.start();
            this.isanmtstart=true;
        }
        var i=0;
        var rotateloop=function(){
            stats.update();
            i++;
            this.woiobg.wo.rotation.x+=stepx;
            this.woiobg.wo.rotation.y+=stepy;
            this.woiobg.wo.rotation.z+=stepz;
            this.woiobg.renderer.render(this.woiobg.scene,this.woiobg.camera);
            if(i>400){
                this.anmt.off(rotateloop,this);
                this.anmt.stop();
                this.isanmtstart=false;
                //this.anmtHalt();
            }
        }
        this.anmt.on(rotateloop,this);

    }
    return show;
})();