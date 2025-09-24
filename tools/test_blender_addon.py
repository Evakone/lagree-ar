#!/usr/bin/env python3
"""
Test script to verify Blender MindAR addon functionality
Run this in Blender's Text Editor or Python console
"""

import bpy
import sys
import os

def test_addon():
    """Test if the MindAR addon is properly installed and working"""
    
    print("🔍 Testing MindAR Blender Addon...")
    
    # Check if addon is enabled
    addon_name = "mindar_marker_tools"
    if addon_name in bpy.context.preferences.addons:
        print("✅ Addon is enabled")
    else:
        print("❌ Addon is not enabled")
        print("   Go to Edit → Preferences → Add-ons")
        print("   Search for 'MindAR' and enable it")
        return False
    
    # Check if panel exists
    try:
        panel_class = getattr(bpy.types, "MINDAR_PT_panel")
        print("✅ Panel class found")
    except AttributeError:
        print("❌ Panel class not found")
        return False
    
    # Check if operators exist
    operators = [
        "MINDAR_OT_create_marker_reference",
        "MINDAR_OT_scale_to_marker", 
        "MINDAR_OT_export_settings",
        "MINDAR_OT_import_settings"
    ]
    
    for op_name in operators:
        try:
            op_class = getattr(bpy.types, op_name)
            print(f"✅ {op_name} found")
        except AttributeError:
            print(f"❌ {op_name} not found")
            return False
    
    # Check if properties exist
    properties = [
        "mindar_marker_size",
        "mindar_marker_scale",
        "mindar_model_scale",
        "mindar_model_position",
        "mindar_model_rotation",
        "mindar_export_path"
    ]
    
    for prop_name in properties:
        if hasattr(bpy.types.Scene, prop_name):
            print(f"✅ {prop_name} property found")
        else:
            print(f"❌ {prop_name} property not found")
            return False
    
    print("\n🎉 All tests passed! The addon is working correctly.")
    print("\n📋 How to use:")
    print("1. Press N in the 3D Viewport to open the sidebar")
    print("2. Look for the 'MindAR' tab")
    print("3. Set your marker size and scale your model")
    
    return True

def install_addon_instructions():
    """Print installation instructions"""
    print("\n📥 Installation Instructions:")
    print("1. Open Blender")
    print("2. Go to Edit → Preferences → Add-ons")
    print("3. Click 'Install...'")
    print("4. Navigate to: /Users/joshjacobson/Documents/GitHub/lagree-ar/tools/")
    print("5. Select: blender_mindar_addon.py")
    print("6. Click 'Install Add-on'")
    print("7. Enable the addon by checking the box")
    print("8. Restart Blender")

if __name__ == "__main__":
    if not test_addon():
        install_addon_instructions()
