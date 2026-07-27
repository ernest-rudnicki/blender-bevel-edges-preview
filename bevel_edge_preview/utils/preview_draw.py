import gpu
from gpu_extras.batch import batch_for_shader

from bevel_edge_preview.utils.preview_state import preview_state


def draw_affected_edges_preview():
    line_positions = preview_state.get_line_coordinates()

    if len(line_positions) == 0:
        return

    shader = gpu.shader.from_builtin("UNIFORM_COLOR")
    batch = batch_for_shader(shader, "LINES", {"pos": line_positions})
    shader.uniform_float("color", (0.75, 0.25, 1.0, 1.0))
    batch.draw(shader)
