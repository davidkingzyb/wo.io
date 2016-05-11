
/////////////////////////////////////////////////
//                                             // 
//                               __            // 
//   __    __   _____           |__|  _____    // 
//  |  |/\|  | /     \   ____   |  | /     \   // 
//  |        ||   o   | |    |  |  ||   o   |  // 
//  |___/\___| \_____/  |____|  |__| \_____/   // 
/////////////////////////////////////////////////
//  2016/03/05 by DKZ https://davidkingzyb.github.io
var ISEYELOAD=false;
var ISHEADLOAD=false;

var woioBg=function(){
    this.scene=new THREE.Scene();
    this.camera=new THREE.PerspectiveCamera(40,window.innerWidth/window.innerHeight,0.1,1000);
    this.renderer=new THREE.WebGLRenderer();
    this.axes=new THREE.AxisHelper(20);
    this.ambientlight=new THREE.AmbientLight(0x0c0c0c);
    this.spotlightF=new THREE.SpotLight(0xcccccc);
    this.spotlightB=new THREE.SpotLight(0x777777);
    this.spotlightL=new THREE.SpotLight(0x999999);
    this.spotlightR=new THREE.SpotLight(0x888888);
    this.spotlightX=new THREE.SpotLight(0x555555);
    this.spotlightT=new THREE.SpotLight(0x999999);
    this.wo=new THREE.Object3D();

}
woioBg.prototype={
    init:function(){
        this.renderer.setClearColor(new THREE.Color(0xcccccc),1.0);
        this.renderer.setSize(window.innerWidth,window.innerHeight);
        this.renderer.shadowMapEnabled=true;

        //this.scene.add(this.axes);

        this.camera.position.set(0,10,60);
        this.camera.lookAt(this.scene.position);

        this.scene.add(this.ambientlight);

        this.spotlightX.position.set(0,-200,150);
        this.spotlightX.castShadow=true;
        this.scene.add(this.spotlightX);

        this.spotlightB.position.set(0,0,-200);
        this.spotlightB.castShadow=true;
        this.scene.add(this.spotlightB);

        this.spotlightL.position.set(-200,10,0);
        this.spotlightL.castShadow=true;
        this.scene.add(this.spotlightL);

        this.spotlightR.position.set(200,10,0);
        this.spotlightR.castShadow=true;
        this.scene.add(this.spotlightR);

        this.spotlightT.position.set(0,100,-50);
        this.spotlightT.castShadow=true;
        this.scene.add(this.spotlightT);

        this.spotlightF.position.set(0,100,200);
        this.spotlightF.castShadow=true;
        this.scene.add(this.spotlightF);



        document.getElementById("WebGL-output").appendChild(this.renderer.domElement);

        this.renderer.render(this.scene,this.camera);
    },
    loadHead:function(filename,cb){
        var loader=new THREE.OBJLoader();
        var that=this;
        loader.load('../static/res/'+filename+'.obj',function(o){ 
            wtf.$('#loading').setAttribute('class','hidden');
            var materials=[new THREE.MeshLambertMaterial({color:0x999999})];
            var geom=o.children[0].geometry
            that['head_geom']=geom;
            var mesh=THREE.SceneUtils.createMultiMaterialObject(geom,materials);
            mesh.castShadow=true;
            that['head']=mesh;
            ISHEADLOAD=true;
            that.onloaded(cb);
        },function(e){
            //console.log(e.loaded+'/'+e.total);
            wtf.$('#loading').innerHTML='WO loading '+e.loaded+'/'+e.total;
        },function(e){
            wtf.$('#loading').innerHTML='WO loading fail';
        })
    },
    loadEye:function(){
        var loader=new THREE.OBJLoader();
        var that=this;
        loader.load('../static/res/woioEye.obj',function(o){
            var materials=[new THREE.MeshLambertMaterial({color:0x666666})];
            var geom=o.children[0].geometry
            that['eye_geom']=geom;
            var mesh=THREE.SceneUtils.createMultiMaterialObject(geom,materials);
            mesh.castShadow=true;
            that['eye']=mesh;
            ISEYELOAD=true;
        })
    },
    onloaded:function(cb){
        this.wo.scale.set(2.7,2.7,2.7);
        this.wo.position.set(0,-35,-40);
        this.wo.rotation.x=THREE.Math.degToRad(28);
        this.wo.add(this.head);
        this.wo.add(this.eye);
        this.scene.add(this.wo);
        this.renderer.render(this.scene,this.camera);
        if(cb){
            cb.call(window);
        }
        
    }
}

