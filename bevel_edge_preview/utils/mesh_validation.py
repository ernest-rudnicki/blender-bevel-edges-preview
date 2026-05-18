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

    @staticmethod
    def validate_bevel_angles(bevel_angles):
        if not isinstance(bevel_angles, list):
            return Validator(
                type={"ERROR"},
                message="Something went wrong. bevel_angles variable is not a list",
            )

        if len(bevel_angles) == 0:
            return Validator(
                type={"WARNING"},
                message="Object does not have bevel modifier",
            )

        return None

    @staticmethod
    def validate_affected_edges(affected_edges):
        if not isinstance(affected_edges, list):
            return Validator(
                type={"ERROR"},
                message="Something went wrong. affected_edges variable is not a list",
            )

        if len(affected_edges) == 0:
            return Validator(
                type={"WARNING"},
                message="There are no edges affected by bevel modifiers",
            )

        return None
