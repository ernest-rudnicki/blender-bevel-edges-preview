from . import select_edges, visualize_edges

modules = (
    visualize_edges,
    select_edges,
)


def register():
    for module in modules:
        module.register()


def unregister():
    for module in reversed(modules):
        module.unregister()
