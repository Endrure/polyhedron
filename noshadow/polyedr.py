from math import pi
from common.r3 import R3
from common.tk_drawer import TkDrawer
import ans


class Edge:
    """ Ребро полиэдра """
    # Параметры конструктора: начало и конец ребра (точки в R3)

    def __init__(self, beg, fin):
        self.beg, self.fin = beg, fin


class Facet:
    """ Грань полиэдра """
    # Параметры конструктора: список вершин

    def __init__(self, vertexes):
        self.vertexes = vertexes


class Polyedr:
    """ Полиэдр """
    # Параметры конструктора: файл, задающий полиэдр

    def __init__(self, file):

        # списки вершин, рёбер и граней полиэдра
        self.vertexes, self.edges, self.facets = [], [], []

        # список строк файла
        with open(file) as f:
            bvert = []
            for i, line in enumerate(f):
                if i == 0:
                    # обрабатываем первую строку; buf - вспомогательный массив
                    buf = line.split()
                    # коэффициент гомотетии
                    c = float(buf.pop(0))
                    # углы Эйлера, определяющие вращение
                    alpha, beta, gamma = (float(x) * pi / 180.0 for x in buf)
                elif i == 1:
                    # во второй строке число вершин, граней и рёбер полиэдра
                    nv, nf, ne = (int(x) for x in line.split())

                elif i < nv + 2:
                    # задание всех вершин полиэдра
                    x, y, z = (float(x) for x in line.split())
                    bvert.append(R3(x, y, z))
                    self.vertexes.append(R3(x, y, z).rz(
                        alpha).ry(beta).rz(gamma) * c)
                else:
                    # вспомогательный массив
                    buf = line.split()
                    # количество вершин очередной грани
                    size = int(buf.pop(0))
                    # массив вершин этой грани
                    vertexes = [self.vertexes[int(n) - 1] for n in buf]
                    mvert = [bvert[int(n) - 1] for n in buf]

                    n = len(mvert)

                    xc = 0
                    for i in range(0, n):
                        xc += mvert[i].x
                    xc /= n

                    yc = 0
                    for i in range(0, n):
                        yc += mvert[i].y
                    yc /= n

                    v = mvert
                    if xc**2 + yc**2 > 1:
                        q = v[0]
                        for i in range(1, n-1):
                            w = i+1
                            v1 = [v[i].x - q.x, v[i].y - q.y, v[i].z - q.z]
                            v2 = [v[w].x - q.x, v[w].y - q.y, v[w].z - q.z]

                            cross = [
                                v1[1]*v2[2] - v1[2]*v2[1],
                                v1[2]*v2[0] - v1[0]*v2[2],
                                v1[0]*v2[1] - v1[1]*v2[0]
                            ]

                            length = (cross[0]**2 + cross[1]**2 + cross[2]**2)

                            ans.ans += length ** 0.5 / 2

                    # задание рёбер грани
                    for n in range(size):
                        self.edges.append(Edge(vertexes[n - 1], vertexes[n]))
                    # задание самой грани
                    self.facets.append(Facet(vertexes))

    # Метод изображения полиэдра
    def draw(self, tk):
        tk.clean()  # pragma: no cover
        for e in self.edges:  # pragma: no cover
            tk.draw_line(e.beg, e.fin)  # pragma: no cover
