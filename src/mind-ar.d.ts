declare module 'https://cdn.jsdelivr.net/npm/mind-ar@1.2.5/dist/mindar-image-three.prod.js' {
    export class MindARThree {
        constructor(config: any);
        renderer: any;
        scene: any;
        camera: any;
        addAnchor(index: number): any;
        start(): Promise<void>;
    }
}
