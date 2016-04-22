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
    function show(woiobg){
        this.woiobg=woiobg;
        //@woiobg
        //@anmt
        //@isanmtstart
    };
    show.prototype.init=function(){
        var that=this.woiobg;

        var twRX=new TWEEN.Tween(that.wo.rotation)
            .delay(5000)
            .to({x:degTorad(-4)},2000)
            .start();
        var twZ=new TWEEN.Tween(that.wo.position)
            .delay(5000)
            .to({z:0,y:-37},2000)
            .onUpdate(function(){
                that.renderer.render(that.scene,that.camera);
            })
            .start()
            .onStop(show.TBCtrlInit)
        requestAnimationFrame(animate);
        function animate(time) {
            //stats.update();
            TWEEN.update(time);
            if(woiobg.wo.position.z!==0){
                requestAnimationFrame(animate);
            }else{
                twZ.stop();
            }
        }
    };
    show.TBCtrlInit=function(){
        var trackballcontrols=new THREE.TrackballControls(woiobg.camera);
            trackballcontrols.rotateSpeed=1;
            trackballcontrols.zoomSpeed=1;
            trackballcontrols.panSpeed=1;
        var clock=new THREE.Clock();
        function render(){
            var delta=clock.getDelta();
            trackballcontrols.update(delta);
            requestAnimationFrame(render);
            woiobg.renderer.render(woiobg.scene,woiobg.camera);
        }
        render();
    }
    show.prototype.HeadUp=function(){
        var that=this.woiobg;
        //todo resetWO
        that.wo.scale.set(2.7,2.7,2.7);
        that.wo.position.set(0,-35,-40);
        that.wo.rotation.x=degTorad(28);
        that.renderer.render(that.scene,that.camera);
        var twRX=new TWEEN.Tween(that.wo.rotation)
            .to({x:degTorad(-4)},2000)
            .start();
        var twZ=new TWEEN.Tween(that.wo.position)
            .to({z:0,y:-37},2000)
            .onUpdate(function(){
                that.renderer.render(that.scene,that.camera);
            })
            .start()
        requestAnimationFrame(animate);
        function animate(time) {
            //stats.update();
            TWEEN.update(time);
            if(woiobg.wo.position.z!==0){
                requestAnimationFrame(animate);
            }else{
                twZ.stop();
            }
        }

    }
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
    show.prototype.setBgColor=function(c){
        this.woiobg.renderer.setClearColor(new THREE.Color(c),1.0);
        this.woiobg.renderer.render(this.woiobg.scene,this.woiobg.camera);

    }
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
            //stats.update();
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