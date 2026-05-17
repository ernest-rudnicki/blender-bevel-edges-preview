# Blender Bevel Edge Preview

Blender Bevel Edge Preview is an Blender add-on for finding edges that would be affected by a Bevel Modifier using angle-based limit logic.

The goal is to make it easier to preview, inspect, select, and eventually convert bevel-angle candidates into bevel weights.

## Why This Exists

Blender's Bevel Modifier can bevel edges based on the angle between adjacent faces, but it is not always easy to see exactly which original mesh edges are being targeted before applying or adjusting the modifier.

This add-on aims to help with that workflow by exposing the bevel angle logic more directly:

- preview edges that match an angle threshold
- select those edges in Edit Mode
- inspect how face normals and edge topology affect the result
- optionally convert detected edges into bevel weights later

## Features

- Detect edges whose adjacent face angle passes a bevel angle threshold.
- Select matching edges in Edit Mode.
- Read useful settings from an existing Bevel Modifier.
- Handle common edge cases such as boundary edges, non-manifold geometry, and flat faces.
- Write detected edges into the `bevel_weight_edge` mesh attribute.
- Provide a small UI panel for running the workflow from the 3D View sidebar.

## License

This project is licensed under the GNU General Public License v3.0 or later.
