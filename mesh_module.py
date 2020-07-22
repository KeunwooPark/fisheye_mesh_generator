import numpy as np

class Mesh:
    def __init__(self):
        pass

    def write_obj(self, file_name):
        if self.vertices is None:
            raise Exception('set vertices')
            return
        if self.uv_map is None:
            raise Exception('set uv_map')
            return
        if self.faces is None:
            raise Exception('set faces')
            return
        with open('%s.obj'%file_name, 'w') as file:
            file.write('# vertex info\n')
            for v in self.vertices:
                str = "v %f %f %f\n" % v
                file.write(str)
            file.write('# texture UV info\n')
            for uv in self.uv_map:
                str = "vt %f %f\n" % uv
                file.write(str)
            file.write('# face info\n')
            for f in self.faces:
                str = "f {0}/{0} {1}/{1} {2}/{2}\n".format(f[0]+1, f[1]+1, f[2]+1)
                file.write(str)

class SquareMesh(Mesh):
    def __init__(self, side, resolution):
        self.res = resolution
        self.square_size = 1
        self.range = (-0.5, 0.5)
        self.half_range = (0, 0.5)

        self.make_mesh(side)

    def make_mesh(self, side):
        if(side == 'front'):
            self.make_front()
        elif side == 'right':
            self.make_right()
        elif side == 'left':
            self.make_left()
        elif side == 'top':
            self.make_top()
        elif side == 'bottom':
            self.make_bottom()

    def divide_range(self, range_to_div, num_div):
        dist = range_to_div[1] - range_to_div[0]
        interval = dist/num_div
        divided = [range_to_div[0] + interval * i for i in range(num_div+1)]
        return divided

    def make_front(self):
        # set vertices
        self.vertices = []
        x_range = self.divide_range(self.range, self.res)
        y_range = self.divide_range(self.range, self.res)
        z_value = self.square_size / 2
        for y in y_range:
            for x in x_range:
                self.vertices.append((x,y,z_value))

        u_range = self.divide_range((0,1), self.res)
        v_range = self.divide_range((0,1), self.res)

        # set uv map
        self.uv_map = []
        for v in v_range:
            for u in u_range:
                self.uv_map.append((u,v))

        # set faces
        res = self.res
        i_range = range(res)
        j_range = range(res)

        bottom_left = []
        for i in i_range:
            for j in j_range:
                bottom_left.append(i * (res+1) + j)

        self.faces = []
        for k in bottom_left:
            self.faces.append((k, k+1, k+res+1))
            self.faces.append((k+1, k+res+2, k+res+1))

    def make_right(self):
        # set vertices
        self.vertices = []
        x_value = self.square_size / 2

        # You have to consider origin of camera texture(uv coordinate) here. That is why z_range is flipped
        y_range = self.divide_range(self.range, self.res)
        z_range = reversed(self.divide_range(self.half_range, int(self.res/2)))

        for z in z_range:
            for y in y_range:
                self.vertices.append((x_value,y,z))

        u_range = self.divide_range((0, 0.5), int(self.res/2))
        v_range = self.divide_range((0,1), self.res)

        # set uv map
        self.uv_map = []
        for u in u_range:
            for v in v_range:
                self.uv_map.append((u,v))

        # set faces
        res = self.res
        i_range = range(int(res/2))
        j_range = range(res)

        bottom_left = []
        for i in i_range:
            for j in j_range:
                bottom_left.append(i * (res+1) + j)

        self.faces = []
        for k in bottom_left:
            #rather than rotating, flip faces
            self.faces.append((k, k+res+1, k+1))
            self.faces.append((k+1, k+res+1, k+res+2))

    def make_left(self):
        # set vertices
        self.vertices = []
        x_value = -self.square_size / 2
        y_range = self.divide_range(self.range, self.res)
        z_range = self.divide_range(self.half_range, int(self.res/2))

        for z in z_range:
            for y in y_range:
                self.vertices.append((x_value,y,z))

        u_range = self.divide_range((0.5, 1), int(self.res/2))
        v_range = self.divide_range((0,1), self.res)

        # set uv map
        self.uv_map = []
        for u in u_range:
            for v in v_range:
                self.uv_map.append((u,v))

        # set faces
        res = self.res
        i_range = range(int(res/2))
        j_range = range(res)

        bottom_left = []
        for i in i_range:
            for j in j_range:
                bottom_left.append(i * (res+1) + j)

        self.faces = []
        for k in bottom_left:
            #rather than rotating, flip faces
            self.faces.append((k, k+res+1, k+1))
            self.faces.append((k+1, k+res+1, k+res+2))

    def make_top(self):
        # set vertices
        self.vertices = []
        x_range = self.divide_range(self.range, self.res)
        y_value = self.square_size / 2
        z_range = reversed(self.divide_range(self.half_range, int(self.res/2)))

        for z in z_range:
            for x in x_range:
                self.vertices.append((x,y_value,z))

        u_range = self.divide_range((0, 1), self.res)
        v_range = self.divide_range((0,0.5), int(self.res/2))

        # set uv map
        self.uv_map = []

        for v in v_range:
            for u in u_range:
                self.uv_map.append((u,v))

        # set faces
        res = self.res
        i_range = range(int(res/2))
        j_range = range(res)

        bottom_left = []
        for i in i_range:
            for j in j_range:
                bottom_left.append(i * (res+1) + j)

        self.faces = []
        for k in bottom_left:
            #rather than rotating, flip faces
            self.faces.append((k, k+1, k+res+1))
            self.faces.append((k+1, k+res+2, k+res+1))

    def make_bottom(self):
        # set vertices
        self.vertices = []
        x_range = self.divide_range(self.range, self.res)
        y_value = -self.square_size / 2
        z_range = self.divide_range(self.half_range, int(self.res/2))

        for z in z_range:
            for x in x_range:
                self.vertices.append((x,y_value,z))

        u_range = self.divide_range((0, 1), self.res)
        v_range = self.divide_range((0.5,1), int(self.res/2))

        # set uv map
        self.uv_map = []

        for v in v_range:
            for u in u_range:
                self.uv_map.append((u,v))

        # set faces
        res = self.res
        i_range = range(int(res/2))
        j_range = range(res)

        bottom_left = []
        for i in i_range:
            for j in j_range:
                bottom_left.append(i * (res+1) + j)

        self.faces = []
        for k in bottom_left:
            #rather than rotating, flip faces
            self.faces.append((k, k+1, k+res+1))
            self.faces.append((k+1, k+res+2, k+res+1))

    def make_right_vertices(self):
        vertices = []
        x_value = self.square_size / 2
        y_range = self.divide_range(self.range, self.res)
        z_range = self.divide_range(self.half_range, int(self.res/2))
        for z in z_range:
            for y in y_range:
                vertices.append((x_value,y,z))
        return vertices

    def arrange_vertices(self, side):
        v_mat = np.array(self.vertices)
        v_mat = v_mat.T
        v_mat = np.pad(v_mat, ((0,1),(0,0)), 'constant', constant_values = 1)
        td = (self.range[1] - self.range[0]) / 2

        if side == 'front':
            M1 = self.get_translate_matrix(0, 0, 0)
            M2 = self.get_rotation_matrix('x', 0)
            M3 = self.get_translate_matrix(0, 0, td)
        elif side == 'right':
            M1 = self.get_rotation_matrix('x', 90)
            M2 = self.get_rotation_matrix('z', -90)
            M3 = self.get_translate_matrix(-td, 0, 0)
        elif side == 'left':
            M1 = self.get_rotation_matrix('x', 90)
            M2 = self.get_rotation_matrix('z', 90)
            M3 = self.get_translate_matrix(td, 0, 0)
        elif side == 'top':
            M1 = self.get_rotation_matrix('z', 180)
            M2 = self.get_rotation_matrix('x', -90)
            M3 = self.get_translate_matrix(0, td, 0)
        elif side == 'bottom':
            M1 = self.get_rotation_matrix('x', 90)
            M2 = self.get_rotation_matrix('z', 0)
            M3 = self.get_translate_matrix(0, -td, 0)
        else:
            raise Exception("side should be one of 'front', 'right', 'left', 'up', 'down'")

        M = np.matmul(M3, M2)
        M = np.matmul(M, M1)
        v_mat = np.matmul(M, v_mat)
        v_mat = v_mat.T
        self.vertices = []
        for v in v_mat:
            self.vertices.append((v[0], v[1], v[2]))

    def get_translate_matrix(self, tx, ty, tz):
        mat = np.eye(4)

        mat[0,3] = tx
        mat[1,3] = ty
        mat[2,3] = tz
        return mat

    def get_rotation_matrix(self, axis, deg):
        # rotation by axis
        c = np.cos(np.radians(deg))
        s = np.sin(np.radians(deg))
        mat = np.eye(4)
        if axis == 'x':
            mat[1,1] = c
            mat[2,2] = c
            mat[1,2] = -s
            mat[2,1] = s
        elif axis == 'y':
            mat[0,0] = c
            mat[2,2] = c
            mat[0,2] = s
            mat[2,0] = -s
        elif axis == 'z':
            mat[0,0] = c
            mat[0,1] = -s
            mat[1,1] = c
            mat[1,0] = s
        return mat

    def make_UV_map(self, side):
        self.uv_map = []

        if side == 'front':
            u_range = self.divide_range((0,1), self.res)
            v_range = self.divide_range((0,1), self.res)
        else:
            u_range = self.divide_range((0,1), self.res)
            v_range = self.divide_range((0.5,1), int(self.res/2))

        for v in v_range:
            for u in u_range:
                self.uv_map.append((u,v))

    def make_surfaces(self, side):
        res = self.res
        if side == 'front':
            i_range = range(res)
            j_range = range(res)
        else:
            i_range = range(res)
            j_range = range(int(res/2))

        bottom_left = []
        for i in i_range:
            for j in j_range:
                bottom_left.append(j * (res+1) + i)

        self.faces = []
        for k in bottom_left:
            self.faces.append((k, k+1, k+res+1))
            self.faces.append((k+1, k+res+2, k+res+1))

class FishMesh(Mesh):
    def __init__(self, model_type, square_mesh):
        x,y = self.map_to_fisheye(model_type, square_mesh.vertices)

        self.vertices = []
        for i in range(len(x)):
            self.vertices.append((x[i], y[i], 0))

        self.uv_map = square_mesh.uv_map.copy()
        self.faces = square_mesh.faces.copy()

    def map_to_fisheye(self, model_type, vertices):
        v_mat = np.array(vertices)

        x = v_mat[:,0]
        y = v_mat[:,1]
        z = v_mat[:,2]

        theta = np.arctan2(np.sqrt(x*x + y*y), z)
        phi = np.arctan2(y, x)

        if model_type == 'equidistance':
            f = 1 / (np.pi/2)
            r = theta * f
        elif model_type == 'orthogonal':
            f = 1
            r = f * np.sin(theta)
        elif model_type == 'stereographic':
            f = 1/2
            r = 2 * f * np.tan(theta/2)
        elif model_type == 'equisolid':
            f = np.sqrt(2)/2
            r = 2 * f * np.sin(theta/2)
        else:
            raise Exception("model_type should be 'equidistance' or 'orthogonal' or 'stereographic' or 'equisolid'")

        _x = r * np.cos(phi)
        _y = r * np.sin(phi)
        return _x, _y
