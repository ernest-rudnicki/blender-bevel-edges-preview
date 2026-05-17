# Development Notes

## First Milestone

Detect candidate edges in Edit Mode:

1. Get the active mesh object.
2. Use `bmesh.from_edit_mesh(obj.data)`.
3. Loop over `bm.edges`.
4. Inspect `edge.link_faces`.
5. For edges with exactly two linked faces, compare face normals.

## API Areas To Explore

- `bpy.types.Operator`
- `bpy.types.Panel`
- `bmesh.from_edit_mesh`
- `BMEdge.link_faces`
- `BMFace.normal`
- `Vector.angle`
- `bpy.types.BevelModifier.limit_method`
- `bpy.types.BevelModifier.angle_limit`
- `Mesh.attributes`
