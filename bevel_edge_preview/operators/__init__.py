from . import reset_bevel_weight, select_edges, set_bevel_weight, visualize_edges

modules = (
    visualize_edges,
    select_edges,
    set_bevel_weight,
    reset_bevel_weight,
)


def register():
    for module in modules:
        module.register()


def unregister():
    for module in reversed(modules):
        module.unregister()
