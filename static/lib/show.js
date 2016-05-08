/////////////////////////////////////////////////
//                                             //  
//                               __            //  
//   __    __   _____           |__|  _____    //  
//  |  |/\|  | /     \   ____   |  | /     \   //  
//  |        ||   o   | |    |  |  ||   o   |  //  
//  |___/\___| \_____/  |____|  |__| \_____/   //  
/////////////////////////////////////////////////
//  2016/04/15 by DKZ https://davidkingzyb.github.io
var ISTBCTRLRUN=false;
var stats;
var show=(function(){
    function show(woiobg){
        this.woiobg=woiobg;
        //stats=show.StatsInit();
        //@woiobg
        //@anmt
        //@isanmtstart
    };
    show.prototype.init=function(){
        var that=this.woiobg;

        var twRX=new TWEEN.Tween(that.wo.rotation)
            .delay(5000)
            .to({x:show.degTorad(-4)},2000)
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
            // stats.update();
            TWEEN.update(time);
            if(woiobg.wo.position.z!==0){
                requestAnimationFrame(animate);
            }else{
                twZ.stop();
            }
        }
    };
    show.StatsInit=function(){
        wtf.loadScript('../static/lib/stats.js',function(){
            stats=new Stats();
            stats.setMode(0);
            var Statsoutput=document.createElement('div');
            Statsoutput.id='Stats-output';
            Statsoutput.style.position='fixed';
            Statsoutput.style.zIndex='99';
            document.body.appendChild(Statsoutput);
            document.getElementById('Stats-output').appendChild(stats.domElement);
        })
        
    }
    show.TBCtrlInit=function(){
        if(!ISTBCTRLRUN){
            ISTBCTRLRUN=true;
            var trackballcontrols=new THREE.TrackballControls(woiobg.camera);
                trackballcontrols.rotateSpeed=1;
                trackballcontrols.zoomSpeed=1;
                trackballcontrols.panSpeed=1;
            var clock=new THREE.Clock();
            function render(){
                // stats.update();
                var delta=clock.getDelta();
                trackballcontrols.update(delta);
                if(ISTBCTRLRUN){
                    requestAnimationFrame(render);
                }
                woiobg.renderer.render(woiobg.scene,woiobg.camera);
            }
            render();
        }
        
    };
    show.TBCtrlHalt=function(){
        ISTBCTRLRUN=false;
    }
    show.prototype.resetWO=function(){
        this.woiobg.wo.position.set(0,-37,0);
        this.woiobg.wo.rotation.set(show.degTorad(-4),0,0)
        this.woiobg.renderer.render(this.woiobg.scene,this.woiobg.camera);
    };
    show.prototype.resetMaterial=function(){
        this.setEyeMaterial(0x666666);
        this.setHeadMaterial(0x999999);
        this.setBgColor(0xcccccc);
    };
    show.prototype.HeadUp=function(){
        var that=this.woiobg;
        that.wo.scale.set(2.7,2.7,2.7);
        that.wo.position.set(0,-35,-40);
        that.wo.rotation.x=show.degTorad(28);
        that.renderer.render(that.scene,that.camera);
        var twRX=new TWEEN.Tween(that.wo.rotation)
            .to({x:show.degTorad(-4)},2000)
            .start();
        var twZ=new TWEEN.Tween(that.wo.position)
            .to({z:0,y:-37},2000)
            .onUpdate(function(){
                that.renderer.render(that.scene,that.camera);
            })
            .start()
        requestAnimationFrame(animate);
        function animate(time) {
            // stats.update();
            TWEEN.update(time);
            if(woiobg.wo.position.z!==0){
                requestAnimationFrame(animate);
            }else{
                twZ.stop();
            }
        }

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
    };
    show.createFragShader=function(fs){
        var attributes = {};
        var uniforms = {
            time: {type: 'f', value: 0.2},
            scale: {type: 'f', value: 0.2},
            alpha: {type: 'f', value: 0.6},
            resolution: {type: "v2", value: new THREE.Vector2()}
        };

        uniforms.resolution.value.x = window.innerWidth;
        uniforms.resolution.value.y = window.innerHeight;
        var meshMaterial = new THREE.ShaderMaterial({
            uniforms: uniforms,
            attributes: attributes,
            fragmentShader: fs,
            transparent: true

        });
        return meshMaterial;
    };

    show.prototype.setEyeFragShader=function(fs){
        var materials=[show.createFragShader(fs)];
        var mesh=THREE.SceneUtils.createMultiMaterialObject(this.woiobg.eye_geom,materials);
        this.woiobg.wo.remove(this.woiobg.eye);
        this.woiobg.eye=mesh;
        this.woiobg.wo.add(this.woiobg.eye);
        this.woiobg.renderer.render(this.woiobg.scene,this.woiobg.camera);
    };
    show.prototype.setHeadFragShader=function(fs){
        var materials=[show.createFragShader(fs)];
        var mesh=THREE.SceneUtils.createMultiMaterialObject(this.woiobg.head_geom,materials);
        this.woiobg.wo.remove(this.woiobg.head);
        this.woiobg.head=mesh;
        this.woiobg.wo.add(this.woiobg.head);
        this.woiobg.renderer.render(this.woiobg.scene,this.woiobg.camera);
    }
    show.showTitle=function(title){
        wtf.$('#title').innerHTML=title;
        wtf.$('#title').setAttribute('class','');
        //wtf.$('#title').setAttribute('class','animated fadeOut');
    };
    show.hideTitle=function(){
        wtf.$('#title').innerHTML='W O . I O';
        wtf.$('#title').setAttribute('class','hidden');
    }
    show.randomColor=function(){
        return parseInt(Math.random()*0xFFFFFF,16);
    };
    show.degTorad=function(deg){
        return deg*Math.PI/180;
    };
    show.prototype.setEyeMaterial=function(c,material){
        var material=material||'Lambert';//Basic,Phong
        var materials=[new THREE['Mesh'+material+'Material']({color:c})];
        var mesh=THREE.SceneUtils.createMultiMaterialObject(this.woiobg.eye_geom,materials);
        mesh.castShadow=true;
        this.woiobg.wo.remove(this.woiobg.eye)
        this.woiobg.eye=mesh;
        this.woiobg.wo.add(this.woiobg.eye);
        this.woiobg.renderer.render(this.woiobg.scene,this.woiobg.camera);
    };
    show.prototype.setHeadMaterial=function(c,material){
        var material=material||'Lambert';//Basic,Phong
        var materials=[new THREE['Mesh'+material+'Material']({color:c})];
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
            // stats.update();
            i++;
            this.woiobg.wo.rotation.x+=stepx;
            this.woiobg.wo.rotation.y+=stepy;
            this.woiobg.wo.rotation.z+=stepz;
            this.woiobg.renderer.render(this.woiobg.scene,this.woiobg.camera);
            if(i>400){
                this.anmt.off(rotateloop,this);
                this.anmt.stop();
                this.isanmtstart=false;
                
            }
        }
        this.anmt.on(rotateloop,this);

    };
    show.prototype.popWO=function(eyecolor,headcolor,bgcolor){
        this.setEyeMaterial(eyecolor||show.randomColor());
        this.setHeadMaterial(headcolor||show.randomColor());
        this.setBgColor(bgcolor||show.randomColor());
        this.setWO('position',-2+Math.random()*4,-39+Math.random()*4,-2+Math.random()*4);
        this.setWO('rotation',show.degTorad(-4-10+20*Math.random()),show.degTorad(-10+20*Math.random()),show.degTorad(-10+20*Math.random()))
        //show.showTitle('Pop.wo');
    };
    show.prototype.popShow=function(times){
        var times=times||40;
        var i=1;
        var that=this;
        show.showTitle('Pop.wo');
        function popLoop(){
            that.popWO();
            i++;
            if(i<=times){
                setTimeout(popLoop,400)
            }else{
                show.hideTitle();
                that.resetMaterial();
                that.resetWO();
            }
        }
        setTimeout(popLoop,400);
    }
    return show;
})();