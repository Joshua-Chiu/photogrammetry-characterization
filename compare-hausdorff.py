import sys
import numpy as np
from scipy.spatial.distance import directed_hausdorff
import trimesh

def load_obj_file(filename):
    mesh = trimesh.load_mesh(filename)
    return mesh.vertices

def hausdorff_distance(v, u):
    return max(directed_hausdorff(v, u)[0], directed_hausdorff(v, u)[0])

def hausdorff_avg(v, u):
    return max(directed_hausdorff(v, u)[0], directed_hausdorff(v, u)[0])

def normalize_coordinates(vertices):
    centroid = np.mean(vertices, axis=0)
    vertices_centered = vertices - centroid
    max_extent = np.abs(vertices_centered).max()
    normalized_vertices = vertices_centered / max_extent
    return normalized_vertices

def main():
    GROUNDTRUTH_NORMALIZATION_FACTOR = 165.88/2

    # Load vertices from OBJ files and normalize coordinates
    vertices_truth = normalize_coordinates(load_obj_file("groundtruth.obj"))
    vertices_scan = normalize_coordinates(load_obj_file("1-rotated.obj"))

    # Compute Hausdorff distance
    hausdorff_dist = hausdorff_distance(vertices_truth, vertices_scan)

    print(f"Normalized Hausdorff Distance: \t {hausdorff_dist}")
    print(f"Measured Hausdorff Distance: \t {hausdorff_dist * GROUNDTRUTH_NORMALIZATION_FACTOR} mm")

if __name__ == "__main__":
    main()