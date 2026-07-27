from . import edit_mesh_context_menu

modules = (edit_mesh_context_menu,)


def register():
    for module in modules:
        module.register()


def unregister():
    for module in reversed(modules):
        module.unregister()
