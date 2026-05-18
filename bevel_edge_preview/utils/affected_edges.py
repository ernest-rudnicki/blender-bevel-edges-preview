class AffectedEdges:
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
