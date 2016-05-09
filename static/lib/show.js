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
    show.prototype.fragShaderRender=function(shadermaterial){
        if(!this.anmt){
            this.anmtInit();
        }
        else{
            this.anmtHalt();
            this.anmtInit();
        }
        if(!this.isanmtstart){
            this.anmt.start();
            this.isanmtstart=true;
        }
        var rd=function(){
            //stats&&stats.update();
            shadermaterial.uniforms.time.value+=0.01;
            this.woiobg.renderer.render(this.woiobg.scene,this.woiobg.camera);
        }
        this.anmt.on(rd,this);
        
    }
    show.prototype.setEyeFragShader=function(fs){
        var materials=[show.createFragShader(fs)];
        var mesh=THREE.SceneUtils.createMultiMaterialObject(this.woiobg.eye_geom,materials);
        this.woiobg.wo.remove(this.woiobg.eye);
        this.woiobg.eye=mesh;
        this.woiobg.wo.add(this.woiobg.eye);
        this.woiobg.renderer.render(this.woiobg.scene,this.woiobg.camera);
        //console.log(this.woiobg.eye)
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

fs1=`
    precision highp float;
    uniform float time;
    uniform float alpha;
    uniform vec2 resolution;
    varying vec2 vUv;

    void main2(void)
    {
    vec2 position = vUv;
    float red = 1.0;
    float green = 0.25 + sin(time) * 0.25;
    float blue = 0.0;
    vec3 rgb = vec3(red, green, blue);
    vec4 color = vec4(rgb, alpha);
    gl_FragColor = color;
    }

    #define PI 3.14159
    #define TWO_PI (PI*2.0)
    #define N 68.5

    void main(void)
    {
    vec2 center = (gl_FragCoord.xy);
    center.x=-10.12*sin(time/200.0);
    center.y=-10.12*cos(time/200.0);

    vec2 v = (gl_FragCoord.xy - resolution/20.0) / min(resolution.y,resolution.x) * 15.0;
    v.x=v.x-10.0;
    v.y=v.y-200.0;
    float col = 0.0;

    for(float i = 0.0; i < N; i++)
    {
    float a = i * (TWO_PI/N) * 61.95;
    col += cos(TWO_PI*(v.y * cos(a) + v.x * sin(a) + sin(time*0.004)*100.0 ));
    }

    col /= 5.0;

    gl_FragColor = vec4(col*1.0, -col*1.0,-col*4.0, 1.0);
    }

`

fs2=`
    uniform float time;
    uniform vec2 resolution;

    // 2013-03-30 by @hintz

    #define CGFloat float
    #define M_PI 3.14159265359

    vec3 hsvtorgb(float h, float s, float v)
    {
    float c = v * s;
    h = mod((h * 6.0), 6.0);
    float x = c * (1.0 - abs(mod(h, 2.0) - 1.0));
    vec3 color;

    if (0.0 <= h && h < 1.0)
    {
    color = vec3(c, x, 0.0);
    }
    else if (1.0 <= h && h < 2.0)
    {
    color = vec3(x, c, 0.0);
    }
    else if (2.0 <= h && h < 3.0)
    {
    color = vec3(0.0, c, x);
    }
    else if (3.0 <= h && h < 4.0)
    {
    color = vec3(0.0, x, c);
    }
    else if (4.0 <= h && h < 5.0)
    {
    color = vec3(x, 0.0, c);
    }
    else if (5.0 <= h && h < 6.0)
    {
    color = vec3(c, 0.0, x);
    }
    else
    {
    color = vec3(0.0);
    }

    color += v - c;

    return color;
    }

    void main(void)
    {

    vec2 position = (gl_FragCoord.xy - 0.5 * resolution) / resolution.y;
    float x = position.x;
    float y = position.y;

    CGFloat a = atan(x, y);

    CGFloat d = sqrt(x*x+y*y);
    CGFloat d0 = 0.5*(sin(d-time)+1.5)*d;
    CGFloat d1 = 5.0;

    CGFloat u = mod(a*d1+sin(d*10.0+time), M_PI*2.0)/M_PI*0.5 - 0.5;
    CGFloat v = mod(pow(d0*4.0, 0.75),1.0) - 0.5;

    CGFloat dd = sqrt(u*u+v*v);

    CGFloat aa = atan(u, v);

    CGFloat uu = mod(aa*3.0+3.0*cos(dd*30.0-time), M_PI*2.0)/M_PI*0.5 - 0.5;
    // CGFloat vv = mod(dd*4.0,1.0) - 0.5;

    CGFloat d2 = sqrt(uu*uu+v*v)*1.5;

    gl_FragColor = vec4( hsvtorgb(dd+time*0.5/d1, sin(dd*time), d2), 1.0 );
    }
`

fs3=`
    uniform vec2 resolution;
    uniform float time;

    vec2 rand(vec2 pos)
    {
    return fract( 0.00005 * (pow(pos+2.0, pos.yx + 1.0) * 22222.0));
    }
    vec2 rand2(vec2 pos)
    {
    return rand(rand(pos));
    }

    float softnoise(vec2 pos, float scale)
    {
    vec2 smplpos = pos * scale;
    float c0 = rand2((floor(smplpos) + vec2(0.0, 0.0)) / scale).x;
    float c1 = rand2((floor(smplpos) + vec2(1.0, 0.0)) / scale).x;
    float c2 = rand2((floor(smplpos) + vec2(0.0, 1.0)) / scale).x;
    float c3 = rand2((floor(smplpos) + vec2(1.0, 1.0)) / scale).x;

    vec2 a = fract(smplpos);
    return mix(
    mix(c0, c1, smoothstep(0.0, 1.0, a.x)),
    mix(c2, c3, smoothstep(0.0, 1.0, a.x)),
    smoothstep(0.0, 1.0, a.y));
    }

    void main(void)
    {
    vec2 pos = gl_FragCoord.xy / resolution.y;
    pos.x += time * 0.1;
    float color = 0.0;
    float s = 1.0;
    for(int i = 0; i < 8; i++)
    {
    color += softnoise(pos+vec2(i)*0.02, s * 4.0) / s / 2.0;
    s *= 2.0;
    }
    gl_FragColor = vec4(color);
    }

`
fs4=`


    uniform float time;
    uniform vec2 resolution;

    vec2 rand(vec2 pos)
    {
    return
    fract(
    (
    pow(
    pos+2.0,
    pos.yx+2.0
    )*555555.0
    )
    );
    }

    vec2 rand2(vec2 pos)
    {
    return rand(rand(pos));
    }

    float softnoise(vec2 pos, float scale) {
    vec2 smplpos = pos * scale;
    float c0 = rand2((floor(smplpos) + vec2(0.0, 0.0)) / scale).x;
    float c1 = rand2((floor(smplpos) + vec2(1.0, 0.0)) / scale).x;
    float c2 = rand2((floor(smplpos) + vec2(0.0, 1.0)) / scale).x;
    float c3 = rand2((floor(smplpos) + vec2(1.0, 1.0)) / scale).x;

    vec2 a = fract(smplpos);
    return mix(mix(c0, c1, smoothstep(0.0, 1.0, a.x)),
    mix(c2, c3, smoothstep(0.0, 1.0, a.x)),
    smoothstep(0.0, 1.0, a.x));
    }

    void main( void ) {
    vec2 pos = gl_FragCoord.xy / resolution.y - time * 0.4;

    float color = 0.0;
    float s = 1.0;
    for (int i = 0; i < 6; ++i) {
    color += softnoise(pos + vec2(0.01 * float(i)), s * 4.0) / s / 2.0;
    s *= 2.0;
    }
    gl_FragColor = vec4(color,mix(color,cos(color),sin(color)),color,1);
    }

`

fs5=`

    uniform float time;
    uniform vec2 resolution;

    // tie nd die by Snoep Games.

    void main( void ) {

    vec3 color = vec3(1.0, 0., 0.);
    vec2 pos = (( 1.4 * gl_FragCoord.xy - resolution.xy) / resolution.xx)*1.5;
    float r=sqrt(pos.x*pos.x+pos.y*pos.y)/15.0;
    float size1=2.0*cos(time/60.0);
    float size2=2.5*sin(time/12.1);

    float rot1=13.00; //82.0+16.0*sin(time/4.0);
    float rot2=-50.00; //82.0+16.0*sin(time/8.0);
    float t=sin(time);
    float a = (60.0)*sin(rot1*atan(pos.x-size1*pos.y/r,pos.y+size1*pos.x/r)+time);
    a += 200.0*acos(pos.x*2.0+cos(time/2.0))+asin(pos.y*5.0+sin(time/2.0));
    a=a*(r/50.0);
    a=200.0*sin(a*5.0)*(r/30.0);
    if(a>5.0) a=a/200.0;
    if(a<0.5) a=a*22.5;
    gl_FragColor = vec4( cos(a/20.0),a*cos(a/200.0),sin(a/8.0), 1.0 );
    }
`

fs6=`


    uniform float time;
    uniform vec2 resolution;


    void main( void )
    {

    vec2 uPos = ( gl_FragCoord.xy / resolution.xy );//normalize wrt y axis
    //suPos -= vec2((resolution.x/resolution.y)/2.0, 0.0);//shift origin to center

    uPos.x -= 1.0;
    uPos.y -= 0.5;

    vec3 color = vec3(0.0);
    float vertColor = 2.0;
    for( float i = 0.0; i < 15.0; ++i )
    {
    float t = time * (0.9);

    uPos.y += sin( uPos.x*i + t+i/2.0 ) * 0.1;
    float fTemp = abs(1.0 / uPos.y / 100.0);
    vertColor += fTemp;
    color += vec3( fTemp*(10.0-i)/10.0, fTemp*i/10.0, pow(fTemp,1.5)*1.5 );
    }

    vec4 color_final = vec4(color, 1.0);
    gl_FragColor = color_final;
    }

`