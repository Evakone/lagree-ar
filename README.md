# Lagree AR V2

This is the modernized version of the Lagree AR project, built with **Vite**, **TypeScript**, and **Three.js**.

## 🚀 Getting Started

1.  **Install Dependencies**:
    ```bash
    cd v2
    npm install
    ```

2.  **Run Development Server**:
    ```bash
    npm run dev
    ```
    This will start a local HTTPS server (usually at `https://localhost:3000`).

3.  **Build for Production**:
    ```bash
    npm run build
    ```

## 🏗️ Project Structure

*   `src/main.ts`: Entry point.
*   `src/experience/ARScene.ts`: Core AR logic (Three.js + MindAR).
*   `src/experience/Debugger.ts`: Visual debug tool (lil-gui).
*   `src/config.ts`: Centralized configuration (paths, settings).
*   `plane-ar.html`: Plane detection implementation (Model Viewer).

## 🛠️ Debugging

The project includes a built-in debugger enabled by default in `src/config.ts`.
*   When running in dev mode, you will see a control panel on the right.
*   Use it to adjust the model's Position, Rotation, and Scale.
*   Click "Copy Transform" to export the values.

## 📦 Tech Stack

*   **Vite**: Build tool & Dev server.
*   **TypeScript**: Type safety.
*   **Three.js**: 3D Engine.
*   **MindAR**: Image Tracking.
*   **lil-gui**: Debug UI.
