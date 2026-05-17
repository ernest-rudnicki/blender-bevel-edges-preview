from . import operators, panels, properties

bl_info = {
    "name": "Bevel Edge Preview",
    "author": "Ernest Rudnicki",
    "version": (0, 1, 0),
    "blender": (5, 0, 0),
    "location": "View3D > Sidebar",
    "description": "Add-on for previewing edges affected by bevel angle logic.",
    "category": "Mesh",
}

modules = (
    properties,
    operators,
    panels,
)


def register():
    for module in modules:
        module.register()


def unregister():
    for module in reversed(modules):
        module.unregister()
