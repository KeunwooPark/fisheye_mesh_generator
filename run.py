from mesh_module import *
import visualize as viz
import sys
import os

faces = ['front', 'left', 'right', 'bottom', 'top']

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("How to use: > run.py 'fisheye model type' 'resolution'")
        print("ex) run.py equidistance 64")
        exit()

    fisheye_type = sys.argv[1]
    resolution = int(sys.argv[2])
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
