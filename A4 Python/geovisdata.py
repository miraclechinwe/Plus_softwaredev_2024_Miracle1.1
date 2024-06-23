"""
Geo Visualization and Interactive Segmentation

This module provides functions for reading LAS files and visualizing point cloud data using numpy, laspy, and open3d.
"""

import numpy as np
import laspy
import open3d as o3d

def read_las_file(file_path):
    """
    Reads a LAS file and returns the point cloud data as a numpy array.

    Parameters:
    file_path (str): Path to the LAS file.

    Returns:
    np.ndarray: Numpy array containing the point cloud data.
    """
    with laspy.open(file_path) as las_file:
        las = las_file.read()
        points = np.vstack((las.x, las.y, las.z)).transpose()
    return points

def visualize_point_cloud(points):
    """
    Visualizes a point cloud using Open3D.

    Parameters:
    points (np.ndarray): Numpy array containing point cloud data (Nx3 array of x, y, z coordinates).

    Returns:
    None
    """
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(points)
    
    o3d.visualization.draw_geometries([point_cloud])
