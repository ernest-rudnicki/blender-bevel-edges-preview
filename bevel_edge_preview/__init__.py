bl_info = {
    "name": "Bevel Edge Preview",
    "author": "Your Name",
    "version": (0, 1, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar",
    "description": "Learning add-on for previewing edges affected by bevel angle logic.",
    "category": "Mesh",
}

from . import operators
from . import panels
from . import properties

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
