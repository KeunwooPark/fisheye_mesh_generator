import argparse
from mesh_module import *
import visualize as viz
import sys
import os

faces = ['front', 'left', 'right', 'bottom', 'top']

def parse_args():
    parser = argparse.ArgumentParser(description='Create meshes for a virtual fisheye camera.')
    parser.add_argument('--model_type', type=str, required = True, \
                        choices = ["equidistance", "orthogonal", "stereographic", "equisolid"],\
                        help = "The model type for a fisheye camera.")
    parser.add_argument("--res", type=int, default = 64,\
                        help = "The number grids that splits the side of a view. (default: 64)")

    return parser.parse_args()

def main(args):
    fisheye_type = args.model_type
    resolution = args.res
    square_obj_dir = "square_objs"
    fish_obj_dir = "fish_objs"

    if not os.path.exists(square_obj_dir):
        os.makedirs(square_obj_dir)

    if not os.path.exists(fish_obj_dir):
        os.makedirs(fish_obj_dir)

    fish_meshes = []
    for face in faces:
        s_mesh = SquareMesh(face, resolution)
        s_mesh.write_obj("%s/%s" % (square_obj_dir, face))
        f_mesh = FishMesh(fisheye_type, s_mesh)
        f_mesh.write_obj("%s/%s" % (fish_obj_dir, face))
        fish_meshes.append(f_mesh)

    viz.visualize_fisheye_mesh(fish_meshes, faces, ['b', 'r', 'y', 'c', 'm'])

if __name__ == "__main__":
    args = parse_args()
    main(args)
