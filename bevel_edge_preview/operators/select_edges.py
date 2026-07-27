import bpy

from bevel_edge_preview.utils.affected_edges import AffectedEdges
from bevel_edge_preview.utils.validators import Validator


class BEVEL_EDGE_PREVIEW_OT_select_edges(bpy.types.Operator):
    bl_idname = "bevel_edge_preview.select_edges"
    bl_label = "Select Edges"
    bl_description = "Selects edges affected by bevel angle modifier"

    def execute(self, context):
        obj = context.object
        validator = AffectedEdges.select_bevel_affected_edges(obj)
        if isinstance(validator, Validator):
            self.report(validator.type, validator.message)
            return {"CANCELLED"}

        return {"FINISHED"}


classes = (BEVEL_EDGE_PREVIEW_OT_select_edges,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
