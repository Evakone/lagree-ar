"""
Blender Addon: MindAR Marker Scaling & Positioning Tool
Install: Copy to Blender's addons folder or install as addon
"""

bl_info = {
    "name": "MindAR Marker Tools",
    "author": "LCS+E AR Team",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > MindAR",
    "description": "Tools for scaling and positioning models for MindAR marker tracking",
    "category": "AR",
}

import bpy
import bmesh
from mathutils import Vector, Euler
import json
import os

class MINDAR_PT_panel(bpy.types.Panel):
    bl_label = "MindAR Marker Tools"
    bl_idname = "MINDAR_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "MindAR"

    def draw(self, context):
        layout = self.layout
        
        # Marker size reference
        box = layout.box()
        box.label(text="Marker Reference", icon='IMAGE')
        box.prop(context.scene, "mindar_marker_size", text="Marker Size (cm)")
        box.prop(context.scene, "mindar_marker_scale", text="Scale Factor")
        
        # Model positioning
        box = layout.box()
        box.label(text="Model Positioning", icon='MESH_CUBE')
        box.prop(context.scene, "mindar_model_scale", text="Model Scale")
        box.prop(context.scene, "mindar_model_position", text="Position")
        box.prop(context.scene, "mindar_model_rotation", text="Rotation")
        
        # Export settings
        box = layout.box()
        box.label(text="Export Settings", icon='EXPORT')
        box.prop(context.scene, "mindar_export_path", text="Export Path")
        
        # Action buttons
        col = layout.column(align=True)
        col.operator("mindar.create_marker_reference", text="Create Marker Reference")
        col.operator("mindar.scale_to_marker", text="Scale Model to Marker")
        col.operator("mindar.export_settings", text="Export Settings")
        col.operator("mindar.import_settings", text="Import Settings")

class MINDAR_OT_create_marker_reference(bpy.types.Operator):
    bl_idname = "mindar.create_marker_reference"
    bl_label = "Create Marker Reference"
    bl_description = "Create a reference plane showing marker size"
    
    def execute(self, context):
        # Get marker size in meters
        marker_size = context.scene.mindar_marker_size / 100.0  # Convert cm to m
        
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
        
        self.report({'INFO'}, f"Created marker reference: {marker_size}m x {marker_size}m")
        return {'FINISHED'}

class MINDAR_OT_scale_to_marker(bpy.types.Operator):
    bl_idname = "mindar.scale_to_marker"
    bl_label = "Scale Model to Marker"
    bl_description = "Scale selected model to fit marker size"
    
    def execute(self, context):
        if not context.selected_objects:
            self.report({'ERROR'}, "No objects selected")
            return {'CANCELLED'}
        
        marker_size = context.scene.mindar_marker_size / 100.0  # Convert cm to m
        scale_factor = context.scene.mindar_marker_scale
        
        for obj in context.selected_objects:
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
                
                # Update scene properties
                context.scene.mindar_model_scale = scale_factor_calc
                
                self.report({'INFO'}, f"Scaled {obj.name} by factor {scale_factor_calc:.3f}")
        
        return {'FINISHED'}

class MINDAR_OT_export_settings(bpy.types.Operator):
    bl_idname = "mindar.export_settings"
    bl_label = "Export Settings"
    bl_description = "Export MindAR settings to JSON file"
    
    def execute(self, context):
        settings = {
            "marker_size": context.scene.mindar_marker_size,
            "marker_scale": context.scene.mindar_marker_scale,
            "model_scale": context.scene.mindar_model_scale,
            "model_position": list(context.scene.mindar_model_position),
            "model_rotation": list(context.scene.mindar_model_rotation),
        }
        
        export_path = context.scene.mindar_export_path
        if not export_path:
            export_path = os.path.join(bpy.path.abspath("//"), "mindar_settings.json")
        
        try:
            with open(export_path, 'w') as f:
                json.dump(settings, f, indent=2)
            self.report({'INFO'}, f"Settings exported to {export_path}")
        except Exception as e:
            self.report({'ERROR'}, f"Export failed: {str(e)}")
            return {'CANCELLED'}
        
        return {'FINISHED'}

class MINDAR_OT_import_settings(bpy.types.Operator):
    bl_idname = "mindar.import_settings"
    bl_label = "Import Settings"
    bl_description = "Import MindAR settings from JSON file"
    
    def execute(self, context):
        import_path = context.scene.mindar_export_path
        if not import_path or not os.path.exists(import_path):
            self.report({'ERROR'}, "Invalid import path")
            return {'CANCELLED'}
        
        try:
            with open(import_path, 'r') as f:
                settings = json.load(f)
            
            context.scene.mindar_marker_size = settings.get("marker_size", 10.0)
            context.scene.mindar_marker_scale = settings.get("marker_scale", 1.0)
            context.scene.mindar_model_scale = settings.get("model_scale", 1.0)
            context.scene.mindar_model_position = settings.get("model_position", [0, 0, 0])
            context.scene.mindar_model_rotation = settings.get("model_rotation", [0, 0, 0])
            
            self.report({'INFO'}, f"Settings imported from {import_path}")
        except Exception as e:
            self.report({'ERROR'}, f"Import failed: {str(e)}")
            return {'CANCELLED'}
        
        return {'FINISHED'}

# Properties
def register():
    bpy.types.Scene.mindar_marker_size = bpy.props.FloatProperty(
        name="Marker Size (cm)",
        description="Size of the printed marker in centimeters",
        default=10.0,
        min=1.0,
        max=100.0
    )
    
    bpy.types.Scene.mindar_marker_scale = bpy.props.FloatProperty(
        name="Scale Factor",
        description="How much of the marker the model should occupy",
        default=0.8,
        min=0.1,
        max=2.0
    )
    
    bpy.types.Scene.mindar_model_scale = bpy.props.FloatProperty(
        name="Model Scale",
        description="Current scale of the model",
        default=1.0,
        min=0.001,
        max=100.0
    )
    
    bpy.types.Scene.mindar_model_position = bpy.props.FloatVectorProperty(
        name="Position",
        description="Model position offset",
        default=(0.0, 0.0, 0.0),
        size=3
    )
    
    bpy.types.Scene.mindar_model_rotation = bpy.props.FloatVectorProperty(
        name="Rotation",
        description="Model rotation in degrees",
        default=(0.0, 0.0, 0.0),
        size=3
    )
    
    bpy.types.Scene.mindar_export_path = bpy.props.StringProperty(
        name="Export Path",
        description="Path to export/import settings",
        default="",
        subtype='FILE_PATH'
    )

def unregister():
    del bpy.types.Scene.mindar_marker_size
    del bpy.types.Scene.mindar_marker_scale
    del bpy.types.Scene.mindar_model_scale
    del bpy.types.Scene.mindar_model_position
    del bpy.types.Scene.mindar_model_rotation
    del bpy.types.Scene.mindar_export_path

if __name__ == "__main__":
    register()
