def get_bevel_modifiers(obj):
    if obj is None:
        return []

    return [modifier for modifier in obj.modifiers if modifier.type == "BEVEL"]


def get_bevel_angles(modifiers):
    if modifiers is None:
        return []

    return [modifier.angle_limit for modifier in modifiers]
