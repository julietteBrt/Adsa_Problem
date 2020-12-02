import numpy as np
from math import inf
from copy import copy
import pandas as pd

class Graph():
    def __init__(self, nb_vertices=0):
        self.adj_matrix = np.ones((nb_vertices, nb_vertices)) * inf
        for i in range(nb_vertices):
            for j in range(nb_vertices):
                if(i == j):
                    self.adj_matrix[i][j] = 0
        self.label = [i for i in range(nb_vertices)]

    def add_edge(self, edge, weight=1, by="index"):
        if by == "index":
            self.adj_matrix[edge[0], edge[1]] = weight
            self.adj_matrix[edge[1], edge[0]] = weight
        elif by == "label":
            index1 = self.label.index(edge[0])
            index2 = self.label.index(edge[1])
            self.adj_matrix[index1, index2] = weight
            self.adj_matrix[index2, index1] = weight


    def set_label_vertex(self, vertex, label):
        self.label[vertex] = label

    def floydWarshall(self):
        """Return the minimal distances between every node.

        :param matrix: Matrix of adjacency of a graph.
        :return: Matrix of minimal distances between every node.
        """
        self.dist = copy(self.adj_matrix)
        for k in range(len(self.adj_matrix)):
            for i in range(len(self.adj_matrix)):
                for j in range(len(self.adj_matrix)): 
                    self.dist[i][j] = min(self.dist[i][j], self.dist[i][k] + self.dist[k][j])
        return self.dist

    def __str__(self):
        return self.adj_matrix.__str__()



map = Graph(14)
# Label
map.set_label_vertex(0, "Reactor")
map.set_label_vertex(1, "UpperE")
map.set_label_vertex(2, "LowerE")
map.set_label_vertex(3, "Security")
map.set_label_vertex(4, "Electrical")
map.set_label_vertex(5, "Medbay")
map.set_label_vertex(6, "Storage")
map.set_label_vertex(7, "Cafetaria")
map.set_label_vertex(8, "Unnamed1")
map.set_label_vertex(9, "Unnamed2")
map.set_label_vertex(10, "O2")
map.set_label_vertex(11, "Weapons")
map.set_label_vertex(12, "Shield")
map.set_label_vertex(13, "Navigations")

# Edge
map.add_edge(("Reactor", "UpperE"), 9, by="label")
map.add_edge(("Reactor", "Security"), 6, by="label")
map.add_edge(("Reactor", "LowerE"), 9, by="label")
map.add_edge(("UpperE", "LowerE"), 12, by="label")
map.add_edge(("UpperE", "Security"), 9, by="label")
map.add_edge(("UpperE", "Medbay"), 10, by="label")
map.add_edge(("UpperE", "Cafetaria"), 15, by="label")
map.add_edge(("Security", "LowerE"), 9, by="label")
map.add_edge(("LowerE", "Electrical"), 14, by="label")
map.add_edge(("LowerE", "Storage"), 14, by="label")
map.add_edge(("Electrical", "Storage"), 10, by="label")
map.add_edge(("Medbay", "Cafetaria"), 10, by="label")
map.add_edge(("Cafetaria", "Storage"), 12, by="label")
map.add_edge(("Cafetaria", "Unnamed1"), 11, by="label")
map.add_edge(("Cafetaria", "Weapons"), 9, by="label")
map.add_edge(("Storage", "Unnamed1"), 8, by="label")
map.add_edge(("Storage", "Unnamed2"), 9, by="label")
map.add_edge(("Weapons", "O2"), 7, by="label")
map.add_edge(("Weapons", "Navigations"), 10, by="label")
map.add_edge(("O2", "Navigations"), 10, by="label")
map.add_edge(("O2", "Shield"), 13, by="label")
map.add_edge(("Unnamed2", "Shield"), 6, by="label")
map.add_edge(("Shield", "Navigations"), 12, by="label")
map.add_edge(("Navigations", "Shield"), 12, by="label")


df_map = pd.DataFrame(map.adj_matrix, columns = map.label, index = map.label)
df_min_dist_map = pd.DataFrame(map.floydWarshall(), columns = map.label, index = map.label)
df_map
df_min_dist_map

impostors_map = Graph(15)
# Label
impostors_map.set_label_vertex(0, "Reactor")
impostors_map.set_label_vertex(1, "UpperE")
impostors_map.set_label_vertex(2, "LowerE")
impostors_map.set_label_vertex(3, "Security")
impostors_map.set_label_vertex(4, "Electrical")
impostors_map.set_label_vertex(5, "Medbay")
impostors_map.set_label_vertex(6, "Storage")
impostors_map.set_label_vertex(7, "Cafetaria")
impostors_map.set_label_vertex(8, "Unnamed1")
impostors_map.set_label_vertex(9, "Unnamed2")
impostors_map.set_label_vertex(10, "O2")
impostors_map.set_label_vertex(11, "Weapons")
impostors_map.set_label_vertex(12, "Shield")
impostors_map.set_label_vertex(13, "Navigations")
impostors_map.set_label_vertex(14, "CorridorW")

# Edge
impostors_map.add_edge(("Reactor", "UpperE"), 0, by="label")
impostors_map.add_edge(("Reactor", "Security"), 6, by="label")
impostors_map.add_edge(("Reactor", "LowerE"), 0, by="label")
impostors_map.add_edge(("UpperE", "LowerE"), 12, by="label")
impostors_map.add_edge(("UpperE", "Security"), 9, by="label")
impostors_map.add_edge(("UpperE", "Medbay"), 10, by="label")
impostors_map.add_edge(("UpperE", "Cafetaria"), 15, by="label")
impostors_map.add_edge(("Security", "LowerE"), 9, by="label")
impostors_map.add_edge(("Security", "Medbay"), 0, by="label")
impostors_map.add_edge(("Security", "Electrical"), 0, by="label")
impostors_map.add_edge(("LowerE", "Electrical"), 14, by="label")
impostors_map.add_edge(("LowerE", "Storage"), 14, by="label")
impostors_map.add_edge(("Electrical", "Storage"), 10, by="label")
impostors_map.add_edge(("Electrical", "Medbay"), 0, by="label")
impostors_map.add_edge(("Medbay", "Cafetaria"), 10, by="label")
impostors_map.add_edge(("Cafetaria", "Storage"), 12, by="label")
impostors_map.add_edge(("Cafetaria", "Unnamed1"), 0, by="label")
impostors_map.add_edge(("Cafetaria", "Weapons"), 9, by="label")
impostors_map.add_edge(("Storage", "Unnamed1"), 8, by="label")
impostors_map.add_edge(("Storage", "Unnamed2"), 9, by="label")
impostors_map.add_edge(("Weapons", "O2"), 7, by="label")
impostors_map.add_edge(("Weapons", "Navigations"), 0, by="label")
impostors_map.add_edge(("O2", "Navigations"), 10, by="label")
impostors_map.add_edge(("O2", "Shield"), 13, by="label")
impostors_map.add_edge(("Unnamed2", "Shield"), 6, by="label")
impostors_map.add_edge(("Shield", "Navigations"), 0, by="label")
impostors_map.add_edge(("Navigations", "Shield"), 12, by="label")
impostors_map.add_edge(("CorridorW", "Cafetaria"), 0, by="label")
impostors_map.add_edge(("CorridorW", "Navigations"), 6, by="label")
impostors_map.add_edge(("CorridorW", "Shield"), 6, by="label")
impostors_map.add_edge(("CorridorW", "Unnamed1"), 0, by="label")
impostors_map.add_edge(("CorridorW", "Navigations"), 6, by="label")
impostors_map.add_edge(("CorridorW", "O2"), 6, by="label")
impostors_map.add_edge(("CorridorW", "O2"), 6, by="label")

df_impostors = pd.DataFrame(impostors_map.adj_matrix, columns = impostors_map.label, index = impostors_map.label)
df_min_dist_imp = pd.DataFrame(impostors_map.floydWarshall(), columns = impostors_map.label, index = impostors_map.label)
df_min_dist_imp
