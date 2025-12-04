import * as THREE from 'three';
import GUI from 'lil-gui';

export class Debugger {
    private gui: GUI;
    private target: THREE.Object3D;

    constructor(target: THREE.Object3D) {
        this.target = target;
        this.gui = new GUI({ container: document.getElementById('debug-panel') as HTMLElement });
        this.setupControls();
    }

    private setupControls() {
        const posFolder = this.gui.addFolder('Position');
        posFolder.add(this.target.position, 'x', -2, 2);
        posFolder.add(this.target.position, 'y', -2, 2);
        posFolder.add(this.target.position, 'z', -2, 2);

        const rotFolder = this.gui.addFolder('Rotation');
        rotFolder.add(this.target.rotation, 'x', -Math.PI, Math.PI);
        rotFolder.add(this.target.rotation, 'y', -Math.PI, Math.PI);
        rotFolder.add(this.target.rotation, 'z', -Math.PI, Math.PI);

        const scaleFolder = this.gui.addFolder('Scale');
        const scaleConfig = { s: 0.4 };
        scaleFolder.add(scaleConfig, 's', 0.1, 2).onChange((v: number) => {
            this.target.scale.set(v, v, v);
        });

        const exportFolder = this.gui.addFolder('Export');
        const exportObj = {
            copy: () => {
                const p = this.target.position;
                const r = this.target.rotation;
                const s = this.target.scale;

                const code = `
Position: ${p.x.toFixed(3)}, ${p.y.toFixed(3)}, ${p.z.toFixed(3)}
Rotation: ${r.x.toFixed(3)}, ${r.y.toFixed(3)}, ${r.z.toFixed(3)}
Scale: ${s.x.toFixed(3)}, ${s.y.toFixed(3)}, ${s.z.toFixed(3)}
        `.trim();

                navigator.clipboard.writeText(code);
                alert('Transform copied to clipboard!');
            }
        };
        exportFolder.add(exportObj, 'copy').name('Copy Transform');
    }
}
