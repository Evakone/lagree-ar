# 🎨 Blender MindAR Addon Installation Guide

## ✅ Fixed Issues

The addon has been updated to fix the path error you encountered. The new version:
- Uses safe default paths in your Documents folder
- Creates directories automatically if they don't exist
- Provides better error handling

## 📥 Installation Steps

### **Method 1: Install from File (Recommended)**

1. **Open Blender**
2. **Go to Edit → Preferences**
3. **Click "Add-ons" tab**
4. **Click "Install..." button**
5. **Navigate to:** `/Users/joshjacobson/Documents/GitHub/lagree-ar/tools/`
6. **Select:** `blender_mindar_addon.py`
7. **Click "Install Add-on"**
8. **Enable the addon** by checking the box next to "MindAR Marker Tools"

### **Method 2: Manual Installation**

1. **Copy the file:**
   ```bash
   cp /Users/joshjacobson/Documents/GitHub/lagree-ar/tools/blender_mindar_addon.py \
      "/Users/joshjacobson/Library/Application Support/Blender/4.5/scripts/addons/"
   ```

2. **Rename the file:**
   ```bash
   cd "/Users/joshjacobson/Library/Application Support/Blender/4.5/scripts/addons/"
   mv blender_mindar_addon.py mindar_marker_tools.py
   ```

3. **Restart Blender**
4. **Enable the addon** in Preferences → Add-ons

## 🎯 Using the Addon

### **Access the Panel**
1. **Open Blender**
2. **Switch to 3D Viewport**
3. **Press N** to open the sidebar
4. **Look for "MindAR" tab**

### **Basic Workflow**
1. **Set Marker Size** (e.g., 10cm)
2. **Import your 3D model**
3. **Select the model**
4. **Click "Scale Model to Marker"**
5. **Fine-tune position/rotation**
6. **Export settings**

### **Export/Import Settings**
- **Default path:** `~/Documents/mindar_settings.json`
- **Export:** Saves your scaling settings
- **Import:** Loads previously saved settings

## 🔧 Troubleshooting

### **If you get path errors:**
- The addon now uses safe default paths
- Settings will be saved to your Documents folder
- No more "No such file or directory" errors

### **If the addon doesn't appear:**
1. **Check if it's enabled** in Preferences → Add-ons
2. **Restart Blender** after installation
3. **Look for "MindAR" tab** in the 3D Viewport sidebar (press N)

### **If you get import errors:**
- Make sure you're using Blender 3.0 or newer
- Check the Blender console for detailed error messages

## 🚀 Quick Start

1. **Install the addon** (see steps above)
2. **Open the MindAR panel** (N key in 3D Viewport)
3. **Set marker size** to 10cm
4. **Import your mural model**
5. **Select the model**
6. **Click "Scale Model to Marker"**
7. **Adjust position/rotation as needed**
8. **Export settings**
9. **Copy the values to your MindAR code**

## 📁 File Locations

- **Addon file:** `/Users/joshjacobson/Documents/GitHub/lagree-ar/tools/blender_mindar_addon.py`
- **Settings file:** `~/Documents/mindar_settings.json`
- **Blender addons:** `~/Library/Application Support/Blender/4.5/scripts/addons/`

## 💡 Pro Tips

- **Use the debug tool first** (`/debug`) for quick adjustments
- **Use Blender addon** for complex models and professional workflows
- **Export settings** to save your work
- **Test on actual devices** after scaling

The addon should now install without any path errors! 🎉
