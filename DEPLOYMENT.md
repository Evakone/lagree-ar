# Lagree AR - Deployment Guide

## 🎉 V2 is Now Live!

Your project has been migrated from the old static HTML structure to a modern Vite + TypeScript setup.

## 📦 What Changed

**Old V1 (Archived to `v1-archive/`):**
- Static HTML files
- Manual TensorFlow.js loading
- A-Frame + MindAR

**New V2 (Now at root):**
- Vite build system
- TypeScript
- Modern Three.js
- Built-in debugger

## 🚀 Deploy to Vercel

### Option 1: Via CLI (Recommended)
```bash
# Install Vercel CLI if needed
npm i -g vercel

# Deploy
vercel --prod
```

### Option 2: Via Git Push
```bash
# Commit and push
git add .
git commit -m "Migrated to V2 architecture"
git push origin main

# Vercel will auto-deploy
```

## 🛠 Local Development

```bash
npm install
npm run dev
```

Opens at `https://localhost:3000` (or next available port)

## 📁 Project Structure

```
/
├── src/
│   ├── main.ts           # Entry point
│   ├── config.ts         # Centralized config
│   └── experience/
│       ├── ARScene.ts    # AR logic
│       └── Debugger.ts   # Debug UI
├── public/
│   └── assets/
│       ├── models/       # Your 3D models
│       └── markers/      # MindAR targets
├── index.html            # Main AR experience
├── plane-ar.html         # Plane detection
└── v1-archive/           # Old V1 backup
```

## ⚙️ Configuration

Edit `/src/config.ts` to change:
- Model paths
- Marker paths  
- Debug mode (set to `false` for production)
