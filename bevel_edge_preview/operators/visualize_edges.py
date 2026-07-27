import bpy

from bevel_edge_preview.utils.affected_edges import visualize_affected_edges
from bevel_edge_preview.utils.preview_state import preview_state


class BEVEL_EDGE_PREVIEW_OT_visualize_edges(bpy.types.Operator):
    bl_idname = "bevel_edge_preview.visualize_edges"
    bl_label = "Visualize Bevel Edges"
    bl_description = (
        "Show edges that would be used by a Bevel Modifier with angle limit"
    )

    def execute(self, context):
        validator = visualize_affected_edges(context)

        if validator is not None:
            return validator

        return {"FINISHED"}


classes = (BEVEL_EDGE_PREVIEW_OT_visualize_edges,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    if preview_state.get_is_active():
        draw_handler = preview_state.get_draw_handler()
        if draw_handler is not None:
            bpy.types.SpaceView3D.draw_handler_remove(draw_handler, "WINDOW")
        preview_state.clear_state()

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
