import { defineConfig } from 'vite';
import basicSsl from '@vitejs/plugin-basic-ssl';
import path from 'path';

export default defineConfig({
    plugins: [
        basicSsl()
    ],
    server: {
        host: true, // Listen on all addresses
        port: 3000
    },
    resolve: {
        alias: {
            '@': path.resolve(__dirname, './src')
        }
    },
    // Serve assets from the parent public folder as well if needed, 
    // but for V2 we will try to be self-contained or use a publicDir config
    publicDir: './public'
});
