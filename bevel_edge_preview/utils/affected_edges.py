import bmesh
import bpy

from bevel_edge_preview.utils.mesh_validation import (
    validate_affected_edges,
    validate_bevel_angles,
    validate_prerequisites,
)
from bevel_edge_preview.utils.modifiers import get_bevel_angles, get_bevel_modifiers


def select_bevel_affected_edges(obj):
    bm = bmesh.from_edit_mesh(obj.data)
    validator, affected_edges = get_bevel_affected_edges(obj, bm)

    if validator is not None:
        return validator

    bpy.ops.mesh.select_all(action="DESELECT")
    select_edges(affected_edges)

    bmesh.update_edit_mesh(obj.data)


def set_bevel_weight_for_affected_edges(obj, weight):
    bm = bmesh.from_edit_mesh(obj.data)

    layer = bm.edges.layers.float.get("bevel_weight_edge")
    if layer is None:
        layer = bm.edges.layers.float.new("bevel_weight_edge")

    validator, affected_edges = get_bevel_affected_edges(obj, bm)

    if validator is not None:
        return validator

    for edge in affected_edges:
        edge[layer] = weight

    bmesh.update_edit_mesh(obj.data)


def get_bevel_affected_edges(obj, bm):
    prerequisite_validator = validate_prerequisites(obj)
    if prerequisite_validator is not None:
        return [prerequisite_validator, None]

    modifiers = get_bevel_modifiers(obj)
    bevel_angles = get_bevel_angles(modifiers)

    bevel_validator = validate_bevel_angles(bevel_angles)
    if bevel_validator is not None:
        return [bevel_validator, None]

    affected_edges = find_bevel_affected_edges(bm, bevel_angles)

    affected_edges_validator = validate_affected_edges(affected_edges)
    if affected_edges_validator is not None:
        return [affected_edges_validator, None]

    return [None, affected_edges]


def find_bevel_affected_edges(obj, angles):
    edges = obj.edges
    affected_edges = []

    for edge in edges:
        link_faces = edge.link_faces

        if len(link_faces) == 2:
            face_a = link_faces[0]
            face_b = link_faces[1]
            link_faces_angle = face_a.normal.angle(face_b.normal)

            for angle in angles:
                if link_faces_angle >= angle:
                    affected_edges.append(edge)

    return affected_edges


def select_edges(affected_edges):
    for edge in affected_edges:
        edge.select_set(True)
