from bevel_edge_preview.utils.validators import Validator


class MeshValidation:
    @staticmethod
    def validate_prerequisites(obj):
        if obj is None:
            return Validator(type={"WARNING"}, message="No active object")

        if obj.type != "MESH":
            return Validator(type={"WARNING"}, message="Selected object is not a mesh")

        if obj.mode != "EDIT":
            return Validator(type={"WARNING"}, message="You must be in edit mode")

        return None
