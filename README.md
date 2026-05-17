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

## Installation

### Build the ZIP File

The add-on can be packaged with the included script:

```bash
bash zip_project.sh
```

This creates:

```text
build/bevel.edge_preview.zip
```

On Windows, run the script from Git Bash. From PowerShell, you can also run:

```powershell
& "C:\Program Files\Git\bin\bash.exe" -lc "./zip_project.sh"
```

### Install in Blender

1. Build the ZIP file with `bash zip_project.sh`.
2. Open Blender.
3. Go to `Edit > Preferences > Add-ons`.
4. Click `Install...`.
5. Select `build/bevel.edge_preview.zip`.
6. Enable the add-on named `Bevel Edge Preview`.

## Testing

The current version can be tested by building and installing the add-on ZIP:

1. Run `bash zip_project.sh`.
2. Install `build/bevel.edge_preview.zip` in Blender.
3. Enable the add-on.
4. Now you should be able to test the addon.

For later bevel detection testing, use a simple mesh with clear hard edges, such as a cube or a low-poly object with different face angles.

## License

This project is licensed under the GNU General Public License v3.0 or later.

## Requirements
1. Python
2. Bash
