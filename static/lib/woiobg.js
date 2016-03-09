
/////////////////////////////////////////////////
//                                             // 
//                               __            // 
//   __    __   _____           |__|  _____    // 
//  |  |/\|  | /     \   ____   |  | /     \   // 
//  |        ||   o   | |    |  |  ||   o   |  // 
//  |___/\___| \_____/  |____|  |__| \_____/   // 
/////////////////////////////////////////////////
//  2016/03/05 by DKZ https://davidkingzyb.github.io

var woioBg=function(){
    this.scene=new THREE.Scene(),
    this.camera=new THREE.PerspectiveCamera(45,window.innerWidth/window.innerHeight,0.1,1000),
    this.renderer=new THREE.WebGLRenderer(),
    this.axes=new THREE.AxisHelper(20),
    this.ambientlight=new THREE.AmbientLight(0x0c0c0c)
}
woioBg.prototype={
    init:function(){
        this.renderer.setClearColor(new THREE.Color(0xEEEEEE));
        this.renderer.setSize(window.innerWidth,window.innerHeight);
        this.scene.add(this.axes);

        this.camera.position.x=-30;
        this.camera.position.y=40;
        this.camera.position.z=30;
        this.camera.lookAt(this.scene.position);

        this.scene.add(this.ambientlight);

        document.getElementById("WebGL-output").appendChild(this.renderer.domElement);

        this.renderer.render(this.scene,this.camera);
    },
    loadHead:function(){
        var loader=new THREE.OBJLoader();
        var scene=this.scene;
        var renderer=this.renderer;
        var camera=this.camera;
        loader.load('../static/res/woioLow.obj',function(geometry){ 
            var material=new THREE.MeshBasicMaterial({color:0x666666});
            geometry.children[0].material=material;
            scene.add(geometry);
            renderer.render(scene,camera);

        })
    }
}
window.onload=function(){
    var woiobg=new woioBg();
    woiobg.init();
    woiobg.loadHead();

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