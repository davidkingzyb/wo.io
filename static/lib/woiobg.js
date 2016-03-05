"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

/////////////////////////////////////////////////
//                                             // 
//                               __            // 
//   __    __   _____           |__|  _____    // 
//  |  |/\|  | /     \   ____   |  | /     \   // 
//  |        ||   o   | |    |  |  ||   o   |  // 
//  |___/\___| \_____/  |____|  |__| \_____/   // 
/////////////////////////////////////////////////
//  2016/03/05 by DKZ https://davidkingzyb.github.io

var woioBg = function () {
    function woioBg() {
        _classCallCheck(this, woioBg);

        this.scene = new THREE.Scene();
        this.camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
        this.renderer = new THREE.WebGLRenderer();
        this.axes = new THREE.AxisHelper(20);

        this.init();
    }

    _createClass(woioBg, [{
        key: "init",
        value: function init() {
            this.renderer.setClearColor(new THREE.Color(0xEEEEEE));
            this.renderer.setSize(window.innerWidth, window.innerHeight);
            this.scene.add(this.axes);

            this.camera.position.x = -30;
            this.camera.position.y = 40;
            this.camera.position.z = 30;
            this.camera.lookAt(this.scene.position);
            document.getElementById("WebGL-output").appendChild(this.renderer.domElement);

            this.renderer.render(this.scene, this.camera);
        }
    }]);

    return woioBg;
}();

window.onload = function () {
    var woiobg = new woioBg();
};