import bpy


class BEVEL_EDGE_PREVIEW_OT_report_context(bpy.types.Operator):
    bl_idname = "bevel_edge_preview.report_context"
    bl_label = "Report Context"
    bl_description = "Print basic context information for learning/debugging"

    def execute(self, context):
        obj = context.object
        if obj is None:
            self.report({"WARNING"}, "No active object")
            return {"CANCELLED"}

        print(f"Active object: {obj.name}, mode: {obj.mode}, type: {obj.type}")
        self.report({"INFO"}, "Context reported in the console")
        return {"FINISHED"}


classes = (
    BEVEL_EDGE_PREVIEW_OT_report_context,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
