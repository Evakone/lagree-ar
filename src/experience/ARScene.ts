import { MindARThree } from 'https://cdn.jsdelivr.net/npm/mind-ar@1.2.5/dist/mindar-image-three.prod.js';
import * as THREE from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { DRACOLoader } from 'three/examples/jsm/loaders/DRACOLoader.js';
import { CONFIG } from '../config';
import { Debugger } from './Debugger';

export class ARScene {
    private mindarThree: any;
    private renderer: THREE.WebGLRenderer;
    private scene: THREE.Scene;
    private camera: THREE.PerspectiveCamera;
    private anchor: any;
    private modelGroup: THREE.Group;
    private mixer: THREE.AnimationMixer | null = null;
    private clock: THREE.Clock;
    private _debugPanel: Debugger | null = null;

    constructor() {
        this.mindarThree = new MindARThree({
            container: document.querySelector('#ar-container'),
            imageTargetSrc: CONFIG.MARKER_PATH,
            filterMinCF: 0.0005,
            filterBeta: 0.02,
            warmupTolerance: 4,
            missTolerance: 10
        });

        this.renderer = this.mindarThree.renderer;
        this.scene = this.mindarThree.scene;
        this.camera = this.mindarThree.camera;

        this.modelGroup = new THREE.Group();
        this.clock = new THREE.Clock();

        this.setupRendering();
        this.setupLighting();

        if (CONFIG.DEBUG) {
            this._debugPanel = new Debugger(this.modelGroup);
        }
    }

    private setupRendering() {
        this.renderer.outputColorSpace = THREE.SRGBColorSpace;
        this.renderer.setPixelRatio(window.devicePixelRatio);
    }

    private setupLighting() {
        const light = new THREE.HemisphereLight(0xffffff, 0x333344, 1.1);
        light.position.set(0.2, 1.2, 0.5);
        this.scene.add(light);
    }

    async start() {
        this.anchor = this.mindarThree.addAnchor(0);
        this.anchor.group.add(this.modelGroup);

        await this.loadModel();
        await this.mindarThree.start();

        this.renderer.setAnimationLoop(() => {
            const delta = this.clock.getDelta();
            if (this.mixer) {
                this.mixer.update(delta);
            }
            this.renderer.render(this.scene, this.camera);
        });

        this.setupEvents();
    }

    private async loadModel() {
        const loader = new GLTFLoader();
        const dracoLoader = new DRACOLoader();
        dracoLoader.setDecoderPath('https://www.gstatic.com/draco/versioned/decoders/1.5.6/');
        loader.setDRACOLoader(dracoLoader);

        try {
            const gltf = await loader.loadAsync(CONFIG.MODEL_PATH);

            // Initial transform
            this.modelGroup.add(gltf.scene);
            this.modelGroup.scale.set(0.4, 0.4, 0.4);

            if (gltf.animations.length > 0) {
                this.mixer = new THREE.AnimationMixer(gltf.scene);
                const action = this.mixer.clipAction(gltf.animations[0]);
                action.play();
            }

            console.log('Model loaded successfully');
        } catch (error) {
            console.error('Error loading model:', error);
            throw error;
        }
    }

    private setupEvents() {
        const statusEl = document.getElementById('status');

        this.anchor.onTargetFound = () => {
            console.log('Target Found');
            if (statusEl) statusEl.textContent = 'Target Found';
        };

        this.anchor.onTargetLost = () => {
            console.log('Target Lost');
            if (statusEl) statusEl.textContent = 'Target Lost';
        };
    }
}
