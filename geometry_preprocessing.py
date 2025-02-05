import pandas as pd
import numpy as np
from shapely.geometry import Polygon, Point

def apply_geometry_preprocessing(df):
    df["area"] = df["geometry"].apply(lambda poly: poly.area)
    df["perimeter"] = df["geometry"].apply(lambda poly: poly.length)
    df["compactness"] = (4 * np.pi * df["area"]) / (df["perimeter"] ** 2)
    df["elongation"] = df["geometry"].apply(compute_elongation)
    df.drop(columns=["perimeter", "geometry"], inplace=True)
    return df


# Compute Elongation
def compute_elongation(polygon):
    min_rect = polygon.minimum_rotated_rectangle  # Get the minimum bounding rectangle
    coords = list(min_rect.exterior.coords)
    
    edge_lengths = [Point(coords[i]).distance(Point(coords[i+1])) for i in range(len(coords) - 1)]
    major_axis = max(edge_lengths)
    minor_axis = min(edge_lengths)
    
    return major_axis / minor_axis if minor_axis > 0 else 1
