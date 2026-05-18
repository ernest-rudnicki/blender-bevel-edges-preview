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

        prerequisite_validator = MeshValidation.validate_prerequisites(obj)
        if prerequisite_validator is not None:
            self.report(prerequisite_validator.type, prerequisite_validator.message)
            return {"CANCELLED"}

        modifiers = ModifiersHelper.get_bevel_modifiers(obj)
        bevel_angles = ModifiersHelper.get_bevel_angles(modifiers)

        bevel_validator = MeshValidation.validate_bevel_angles(bevel_angles)
        if bevel_validator is not None:
            self.report(bevel_validator.type, bevel_validator.message)
            return {"CANCELLED"}

        bm = bmesh.from_edit_mesh(obj.data)
        affected_edges = AffectedEdges.find_bevel_affected_edges(bm, bevel_angles)

        affected_edges_validator = MeshValidation.validate_affected_edges(
            affected_edges
        )
        if affected_edges_validator is not None:
            self.report(affected_edges_validator.type, affected_edges_validator.message)
            return {"CANCELLED"}

        bpy.ops.mesh.select_all(action="DESELECT")
        bpy.ops.mesh.select_mode(type="EDGE")
        AffectedEdges.select_bevel_affected_edges(affected_edges)
        bmesh.update_edit_mesh(obj.data)

        return {"FINISHED"}


classes = (BEVEL_EDGE_PREVIEW_OT_select_edges,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
