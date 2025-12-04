import { ARScene } from './experience/ARScene';

const startBtn = document.getElementById('start-btn');
const introOverlay = document.getElementById('intro');

if (startBtn && introOverlay) {
    startBtn.addEventListener('click', async () => {
        introOverlay.style.display = 'none';

        const scene = new ARScene();
        try {
            await scene.start();
        } catch (error) {
            console.error('Failed to start AR:', error);
            alert('Failed to start AR. Check console for details.');
            introOverlay.style.display = 'flex';
        }
    });
}
