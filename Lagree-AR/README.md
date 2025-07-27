# AR Mural Demo

## Overview
The AR Mural Demo project showcases an augmented reality experience using A-Frame and MindAR. It allows users to view a 3D model in an AR environment by scanning a specific image target.

## Project Structure
```
Lagree-AR
├── assets
│   ├── targets.mind          # Image target data for AR tracking
│   └── test_fun_shape_animated.glb  # 3D model in GLB format
├── js
│   └── mindar-image-aframe.prod.js  # JavaScript library for MindAR integration
├── index.html                # Main HTML document for the AR scene
└── README.md                 # Documentation for the project
```

## Setup Instructions
1. Clone the repository to your local machine.
2. Ensure you have a local server running to serve the files (e.g., using Python's `http.server` or any other local server).
3. Open `index.html` in your web browser to view the AR experience.

## Usage
- Point your device's camera at the image target defined in `assets/targets.mind`.
- The 3D model specified in `assets/test_fun_shape_animated.glb` will appear in the AR scene.

## Dependencies
- A-Frame (version 1.4.0)
- MindAR library for A-Frame

## License
This project is licensed under the MIT License.