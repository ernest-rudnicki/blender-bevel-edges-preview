import bmesh
import bpy

from bevel_edge_preview.utils.affected_edges import AffectedEdges
from bevel_edge_preview.utils.mesh_validation import MeshValidation
from bevel_edge_preview.utils.modifiers import ModifiersHelper


class BEVEL_EDGE_PREVIEW_OT_select_edges(bpy.types.Operator):
    bl_idname = "bevel_edge_preview.select_edges"
    bl_label = "Select Edges"
    bl_description = "Selects edges affected by bevel angle modifier"

    def execute(self, context):
        obj = context.object

        validator = MeshValidation.validate_prerequisites(obj)

        if validator is not None:
            self.report(validator.type, validator.message)
            return {"CANCELLED"}

        modifiers = ModifiersHelper.get_bevel_modifiers(obj)
        bevel_angles = ModifiersHelper.get_bevel_angles(modifiers)

        if len(bevel_angles) == 0:
            self.report({"WARNING"}, "Object does not have bevel modifier")
            return {"CANCELLED"}

        bm = bmesh.from_edit_mesh(obj.data)
        affected_edges = AffectedEdges.find_bevel_affected_edges(bm, bevel_angles)
        print(bevel_angles, affected_edges)

        return {"FINISHED"}


classes = (BEVEL_EDGE_PREVIEW_OT_select_edges,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
