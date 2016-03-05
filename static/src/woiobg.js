/////////////////////////////////////////////////
//                                             //  
//                               __            //  
//   __    __   _____           |__|  _____    //  
//  |  |/\|  | /     \   ____   |  | /     \   //  
//  |        ||   o   | |    |  |  ||   o   |  //  
//  |___/\___| \_____/  |____|  |__| \_____/   //  
/////////////////////////////////////////////////
//  2016/03/05 by DKZ https://davidkingzyb.github.io


class woioBg{
    constructor(){
        this.scene=new THREE.Scene();
        this.camera=new THREE.PerspectiveCamera(45,window.innerWidth/window.innerHeight,0.1,1000);
        this.renderer=new THREE.WebGLRenderer();
        this.axes=new THREE.AxisHelper(20);

        this.init();
        
    }

    init(){
    
        this.renderer.setClearColor(new THREE.Color(0xEEEEEE));
        this.renderer.setSize(window.innerWidth,window.innerHeight);
        this.scene.add(this.axes);


        this.camera.position.x=-30;
        this.camera.position.y=40;
        this.camera.position.z=30;
        this.camera.lookAt(this.scene.position);
        document.getElementById("WebGL-output").appendChild(this.renderer.domElement);

        this.renderer.render(this.scene,this.camera);
    }
}

window.onload=function(){
    var woiobg=new woioBg();
}