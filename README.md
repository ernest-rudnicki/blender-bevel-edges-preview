# Blender Bevel Edge Preview

Blender Bevel Edge Preview is an Blender add-on for finding edges that would be affected by a Bevel Modifier using angle-based limit logic.

The goal is to make it easier to preview, inspect, select, and eventually convert bevel-angle candidates into bevel weights.

Gumroad link: https://terminat.gumroad.com/l/blender-bevel-edge-preview

<img width="1024" height="768" alt="Animation image representing the functionality of the addon" src="https://github.com/user-attachments/assets/82e6e829-7e24-4b0b-86b2-d5386141fbc7" />


## Why This Exists

Blender's Bevel Modifier can bevel edges based on the angle between adjacent faces, but it is not always easy to see exactly which original mesh edges are being targeted before applying or adjusting the modifier.

This add-on aims to help with that workflow by exposing the bevel angle logic more directly:

- preview edges that match an angle threshold by using edge highlight
- select those edges in Edit Mode
- inspect how face normals and edge topology affect the result
- set maximum bevel weight with one button click or reset to 0

## Installation
You can use the build uploaded into github packages or follow the instruction below to build the zip file yourself.

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
