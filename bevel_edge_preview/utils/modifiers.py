def get_bevel_modifiers(obj):
    if obj is None:
        return []

    return [modifier for modifier in obj.modifiers if modifier.type == "BEVEL"]
