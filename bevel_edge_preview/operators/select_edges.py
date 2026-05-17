import bpy


class BEVEL_EDGE_PREVIEW_OT_select_edges(bpy.types.Operator):
    bl_idname = "bevel_edge_preview.select_edges"
    bl_label = "Select Bevel Edges"
    bl_description = "Select edges that would be used by a Bevel Modifier with angle limit"

    def execute(self, context):
        obj = context.object

        if obj is None:
            self.report({"WARNING"}, "No active object")
            return {"CANCELLED"}

        print(f"Select bevel edges: {obj.name}, mode: {obj.mode}, type: {obj.type}")
        return {"FINISHED"}


classes = (
    BEVEL_EDGE_PREVIEW_OT_select_edges,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
