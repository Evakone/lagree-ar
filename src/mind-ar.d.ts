declare module 'mind-ar/dist/mindar-image-three.prod.js' {
    export class MindARThree {
        constructor(config: any);
        renderer: any;
        scene: any;
        camera: any;
        addAnchor(index: number): any;
        start(): Promise<void>;
    }
}
