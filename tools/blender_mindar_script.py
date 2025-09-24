#!/usr/bin/env python3
"""
Standalone Blender script for MindAR marker scaling
No addon installation required - just run this script in Blender
"""

import bpy
import bmesh
import json
import os
from mathutils import Vector, Euler

def create_marker_reference(size_cm=10.0):
    """Create a reference plane showing marker size"""
    # Convert cm to meters
    marker_size = size_cm / 100.0
    
    # Create reference plane
    bpy.ops.mesh.primitive_plane_add(size=marker_size)
    marker_ref = bpy.context.active_object
    marker_ref.name = "Marker_Reference"
    marker_ref.location = (0, 0, 0)
    
    # Create material for marker reference
    mat = bpy.data.materials.new(name="Marker_Reference_Material")
    mat.use_nodes = True
    mat.node_tree.nodes.clear()
    
    # Add emission node for visibility
    emission = mat.node_tree.nodes.new(type='ShaderNodeEmission')
    emission.inputs[0].default_value = (1, 0, 0, 1)  # Red color
    emission.inputs[1].default_value = 0.5
    
    output = mat.node_tree.nodes.new(type='ShaderNodeOutputMaterial')
    mat.node_tree.links.new(emission.outputs[0], output.inputs[0])
    
    marker_ref.data.materials.append(mat)
    
    # Add wireframe modifier for better visibility
    wireframe = marker_ref.modifiers.new(name="Wireframe", type='WIREFRAME')
    wireframe.thickness = 0.01
    
    print(f"✅ Created marker reference: {marker_size}m x {marker_size}m")
    return marker_ref

def scale_model_to_marker(scale_factor=0.8, marker_size_cm=10.0):
    """Scale selected model to fit marker size"""
    if not bpy.context.selected_objects:
        print("❌ No objects selected")
        return False
    
    marker_size = marker_size_cm / 100.0  # Convert cm to m
    
    for obj in bpy.context.selected_objects:
        if obj.type == 'MESH':
            # Calculate bounding box
            bbox = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
            bbox_x = max(bbox, key=lambda v: v.x).x - min(bbox, key=lambda v: v.x).x
            bbox_y = max(bbox, key=lambda v: v.y).y - min(bbox, key=lambda v: v.y).y
            bbox_z = max(bbox, key=lambda v: v.z).z - min(bbox, key=lambda v: v.z).z
            
            # Calculate scale needed to fit marker
            max_dimension = max(bbox_x, bbox_y, bbox_z)
            target_size = marker_size * scale_factor
            scale_factor_calc = target_size / max_dimension
            
            # Apply scale
            obj.scale = (scale_factor_calc, scale_factor_calc, scale_factor_calc)
            
            print(f"✅ Scaled {obj.name} by factor {scale_factor_calc:.3f}")
    
    return True

def export_settings(filepath=None):
    """Export MindAR settings to JSON file"""
    if not filepath:
        filepath = os.path.expanduser("~/Documents/mindar_settings.json")
    
    # Get current scene properties or use defaults
    settings = {
        "marker_size": 10.0,
        "marker_scale": 0.8,
        "model_scale": 1.0,
        "model_position": [0, 0, 0],
        "model_rotation": [0, 0, 0],
    }
    
    # Try to get from scene properties if they exist
    if hasattr(bpy.types.Scene, 'mindar_marker_size'):
        settings["marker_size"] = bpy.context.scene.mindar_marker_size
    if hasattr(bpy.types.Scene, 'mindar_marker_scale'):
        settings["marker_scale"] = bpy.context.scene.mindar_marker_scale
    if hasattr(bpy.types.Scene, 'mindar_model_scale'):
        settings["model_scale"] = bpy.context.scene.mindar_model_scale
    if hasattr(bpy.types.Scene, 'mindar_model_position'):
        settings["model_position"] = list(bpy.context.scene.mindar_model_position)
    if hasattr(bpy.types.Scene, 'mindar_model_rotation'):
        settings["model_rotation"] = list(bpy.context.scene.mindar_model_rotation)
    
    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        with open(filepath, 'w') as f:
            json.dump(settings, f, indent=2)
        print(f"✅ Settings exported to {filepath}")
        return True
    except Exception as e:
        print(f"❌ Export failed: {str(e)}")
        return False

def print_usage():
    """Print usage instructions"""
    print("\n🎯 MindAR Blender Script Usage:")
    print("=" * 50)
    print("1. Create marker reference:")
    print("   create_marker_reference(10.0)  # 10cm marker")
    print()
    print("2. Scale model to marker:")
    print("   # Select your model first, then:")
    print("   scale_model_to_marker(0.8, 10.0)  # 80% of marker size")
    print()
    print("3. Export settings:")
    print("   export_settings()  # Saves to ~/Documents/mindar_settings.json")
    print()
    print("4. Quick workflow:")
    print("   create_marker_reference(10.0)")
    print("   # Select your model")
    print("   scale_model_to_marker(0.8, 10.0)")
    print("   export_settings()")
    print("=" * 50)

# Main execution
if __name__ == "__main__":
    print("🎨 MindAR Blender Script Loaded!")
    print_usage()
    
    # Auto-create marker reference
    print("\n🔧 Auto-creating 10cm marker reference...")
    create_marker_reference(10.0)
    
    print("\n✅ Ready! Select your model and run:")
    print("   scale_model_to_marker(0.8, 10.0)")
    print("\n💡 Or use the debug tool at /debug for real-time adjustment!")
