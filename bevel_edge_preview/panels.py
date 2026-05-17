import bpy


class BEVEL_EDGE_PREVIEW_PT_main(bpy.types.Panel):
    bl_label = "Bevel Edge Preview"
    bl_idname = "BEVEL_EDGE_PREVIEW_PT_main"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Bevel Preview"

    def draw(self, context):
        layout = self.layout
        layout.operator("bevel_edge_preview.report_context")


classes = (
    BEVEL_EDGE_PREVIEW_PT_main,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
