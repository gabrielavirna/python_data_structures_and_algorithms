"""
Graph representation - 2 main forms:
--------------------
-> use an adjacency matrix & a dictionary
-> use an adjacency list


-> Adjacency list
-----------------
- Use a simple list can be used to present a graph. The indices of the list will represent the nodes/vertices in the
graph. At each index, the adjacent nodes to that vertex can be stored.

The vertices. Index 0 represents vertex A with its adjacent nodes being B and C.

                            0 -> [B, C]
                            1 -> [A, E]
                            2 -> [A, B, E, F]
                            3 -> [B, C]
                            4 -> [C]

Using a list for the representation is quite restrictive because we lack the ability to directly use the vertex labels.
=> Use a dictionary => vertex A has the adjacent vertices B and C. Vertex F has vertex C as its only neighbor.


-> Adjacency matrix
-------------------
Use an adjacency matrix to represent a graph. A matrix is a two-dimensional array => represent the cells with a 1 or 0
depending on whether two vertices are connected by an edge.


"""

# Graph representation using a dictionary
# Adjacency list for a graph:

graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['E', 'A']
graph['C'] = ['A', 'B', 'E', 'F']
graph['E'] = ['B', 'C']
graph['F'] = ['C']

# Given an adjacency list => create an adjacency matrix
# a sorted list of keys of graph is required:
matrix_elements = sorted(graph.keys())
# the dimensions of the matrix
cols = rows = len(matrix_elements)

# set up a cols by rows array, filling it with zeros
adjacency_matrix = [[0 for x in range(rows)] for y in range(cols)]
#  The edges_list variable will store the tuples that form the edges of in the graph.
# E.g. an edge between node A and B will be stored as (A, B).
edges_list = []

# The multidimensional array is filled using a nested for loop:
for key in matrix_elements:
    for neighbor in graph[key]:
        edges_list.append((key, neighbor))

# fill the multidimensional array by using 1 to mark the presence of an edge
# The matrix_elements array has its rows and cols starting from A through to E with the indices 0 through to 5.
# loop iterates through the list of tuples & index method gets the corresponding index where an edge is to be stored.
for edge in edges_list:
    index_of_first_vertex = matrix_elements.index(edge[0])
    index_of_second_vertex = matrix_elements.index(edge[1])
    adjacency_matrix[index_of_first_vertex][index_of_second_vertex] = 1


# The adjacency matrix produced:
# At column 1 and row 1, the 0 there represents the absence of an edge between A and A.
# On column 2 and row 3, there is an edge between C and B.
for row in adjacency_matrix:
    print(row)