import bmesh
import bpy

from bevel_edge_preview.utils.affected_edges import (
    set_bevel_weight_for_affected_edges,
)
from bevel_edge_preview.utils.modifiers import set_bevel_weight_method


class BEVEL_EDGE_PREVIEW_OT_set_bevel_weight(bpy.types.Operator):
    bl_idname = "bevel_edge_preview.set_bevel_weight"
    bl_label = "Set Maximum Bevel Weight"
    bl_description = "Sets the maximum bevel weight for the bevel affected edges and sets existing modifiers to use weight method"

    def execute(self, context):
        obj = context.object

        validator = set_bevel_weight_for_affected_edges(obj, 1.0)
        if validator is not None:
            return validator

        bmesh.update_edit_mesh(obj.data)

        set_bevel_weight_method(obj, "WEIGHT")

        return {"FINISHED"}


classes = (BEVEL_EDGE_PREVIEW_OT_set_bevel_weight,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
