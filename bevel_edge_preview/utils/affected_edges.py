import bmesh

from bevel_edge_preview.utils.mesh_validation import MeshValidation
from bevel_edge_preview.utils.modifiers import ModifiersHelper


class AffectedEdges:
    @staticmethod
    def get_bevel_affected_edges(obj):
        prerequisite_validator = MeshValidation.validate_prerequisites(obj)
        if prerequisite_validator is not None:
            return [prerequisite_validator, None]

        modifiers = ModifiersHelper.get_bevel_modifiers(obj)
        bevel_angles = ModifiersHelper.get_bevel_angles(modifiers)

        bevel_validator = MeshValidation.validate_bevel_angles(bevel_angles)
        if bevel_validator is not None:
            return [bevel_validator, None]

        bm = bmesh.from_edit_mesh(obj.data)
        affected_edges = AffectedEdges.find_bevel_affected_edges(bm, bevel_angles)

        affected_edges_validator = MeshValidation.validate_affected_edges(
            affected_edges
        )
        if affected_edges_validator is not None:
            return [affected_edges_validator, None]

        return [None, affected_edges]

    @staticmethod
    def find_bevel_affected_edges(obj, angles):
        edges = obj.edges
        affected_edges = []

        for edge in edges:
            link_faces = edge.link_faces

            if len(link_faces) == 2:
                faceA = link_faces[0]
                faceB = link_faces[1]
                link_faces_angle = faceA.normal.angle(faceB.normal)

                for angle in angles:
                    if link_faces_angle >= angle:
                        affected_edges.append(edge)

        return affected_edges

    @staticmethod
    def select_bevel_affected_edges(edges):
        for edge in edges:
            edge.select_set(True)
