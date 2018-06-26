import matplotlib.pyplot as plt
from matplotlib import collections  as mc

def visualize_fisheye_mesh(mesh_list, face_names, color_list):
    fig, ax = plt.subplots()
    line_collections = []
    for i, f_mesh in enumerate(mesh_list):
        lines = []
        for f in f_mesh.faces:
            v0 = f[0]
            v1 = f[1]
            v2 = f[2]
            for p in [(v0, v1), (v1, v2), (v2, v0)]:
                f = (f_mesh.vertices[p[0]][0], f_mesh.vertices[p[0]][1])
                t = (f_mesh.vertices[p[1]][0], f_mesh.vertices[p[1]][1])
                lines.append([f,t])
        lc = mc.LineCollection(lines, linewidths=1, color = color_list[i])
        line_collections.append(lc)
        ax.add_collection(lc)
        ax.autoscale()
        ax.margins(0.1)
    ax.legend(line_collections, face_names)
    #plt.show()
    plt.savefig('fisheye.png')
