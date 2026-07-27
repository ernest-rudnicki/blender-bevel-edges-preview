import bpy


class BEVEL_EDGE_PREVIEW_MT_context_menu(bpy.types.Menu):
    bl_label = "Bevel Edge Preview"
    bl_idname = "BEVEL_EDGE_PREVIEW_MT_context_menu"

    @classmethod
    def poll(cls, context):
        obj = context.object
        return (
            obj is not None
            and obj.type == "MESH"
            and obj.mode == "EDIT"
            and context.tool_settings.mesh_select_mode[1]
        )

    def draw(self, context):
        layout = self.layout
        layout.operator("bevel_edge_preview.set_bevel_weight")
        layout.operator("bevel_edge_preview.select_edges")
        layout.operator("bevel_edge_preview.visualize_edges")


def draw_bevel_edge_preview_menu(self, context):
    if BEVEL_EDGE_PREVIEW_MT_context_menu.poll(context):
        self.layout.separator()
        self.layout.menu(BEVEL_EDGE_PREVIEW_MT_context_menu.bl_idname)


classes = (BEVEL_EDGE_PREVIEW_MT_context_menu,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.VIEW3D_MT_edit_mesh_context_menu.prepend(draw_bevel_edge_preview_menu)


def unregister():
    bpy.types.VIEW3D_MT_edit_mesh_context_menu.remove(draw_bevel_edge_preview_menu)

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
