import math
import sys
import numpy as np
from scipy.spatial import KDTree
import trimesh

def load_obj_file(filename):
    mesh = trimesh.load_mesh(filename)
    return mesh.vertices

def normalize_coordinates(vertices):
    centroid = np.mean(vertices, axis=0)
    vertices_centered = vertices - centroid
    max_extent = np.abs(vertices_centered).max()
    normalized_vertices = vertices_centered / max_extent
    return normalized_vertices

def find_correspondences(ground_truth, scanned):
    tree = KDTree(scanned)
    distances, indices = tree.query(ground_truth)
    return distances, indices

def compute_mean_absolute_error(distances):
    return np.mean(abs(distances))

def compute_mean_squared_error(distances):
    return np.mean(distances ** 2)

def main():
    GROUNDTRUTH_NORMALIZATION_FACTOR = 165.88/2
    # Load OBJ files
    ground_truth_points = load_obj_file("groundtruth.obj")
    scanned_points = load_obj_file("1-rotated.obj")

    # Normalize coordinates (optional)
    ground_truth_points = normalize_coordinates(ground_truth_points)
    scanned_points = normalize_coordinates(scanned_points)

    # Find corresponding points
    distances, _ = find_correspondences(ground_truth_points, scanned_points)

    # Compute mean error
    mae = compute_mean_absolute_error(distances)
    mse = compute_mean_squared_error(distances)
    print(f"Mean Absolute Error: {mae * GROUNDTRUTH_NORMALIZATION_FACTOR} mm")
    print(f"Root Mean Squared Error: {math.sqrt(mse) * GROUNDTRUTH_NORMALIZATION_FACTOR} mm")

if __name__ == "__main__":
    main()