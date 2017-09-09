"""
Dijkstra's shortest path algorithm
-----------------------------------
- a greedy algorithm; it finds the shortest distance from a source to all other nodes or vertices in a graph.

The worst-case running time: O(|E| + |V| log |V|), where |V| is the number of vertices and |E| is the number of edges.
"""

# Dijkstra - finding the shortest path algorithm
#################################################

# begin with a dictionary representation of the table (table enables tracking the changes in the graph)
# Each key in the dictionary maps to a list.
# [1st index of the list - stores the shortest distance from the source A, 2nd index - stores the previous node]
table = dict()
table = {'A': [0, None],
         'B': [float("inf"), None],
         'C': [float("inf"), None],
         'D': [float("inf"), None],
         'E': [float("inf"), None],
         'F': [float("inf"), None]}

# DISTANCE: references the shortest path column's index, PREVIOUS_NODE: references the previous node column's index
DISTANCE = 0
PREVIOUS_NODE = 1
INFINITY = float("inf")


def find_shortest_path(graph, table, origin):
    visited_nodes = []
    current_node = origin
    starting_node = origin

    while True:
        #  obtain the current node in the graph we want to investigate
        adjacent_nodes = graph[current_node]
        # find out whether all the adjacent nodes of current_node have been visited
        if set(adjacent_nodes).issubset(set(visited_nodes)):
            pass
        else:
            # returns the nodes that have not been visited
            unvisited_nodes = set(adjacent_nodes).difference(set(visited_nodes))

            for vertex in unvisited_nodes:
                distance_from_starting_node = get_shortest_distance(table, vertex)

                if distance_from_starting_node == INFINITY and current_node == starting_node:
                    # get the value (distance) of the edge between vertex and current_node
                    total_distance = get_distance(graph, vertex, current_node)
                else:
                    # sum(distance from the starting node to current_node, distance between current_node and vertex)
                    total_distance = get_shortest_distance(table, current_node) + get_distance(graph, current_node, vertex)

                # if total distance < the existing data in the shortest distance column in our table
                if total_distance < distance_from_starting_node:
                    # update the row
                    set_shortest_distance(table, vertex, total_distance)
                    set_previous_node(table, vertex, current_node)

        visited_nodes.append(current_node)

        # If all nodes have been visited, exit the while loop.
        if len(visited_nodes) == len(table.keys()):
            break

        # fetch the next node to visit
        current_node = get_next_node(table, visited_nodes)
        return current_node


# returns the value stored in the 0th index of the table, which
# stores the shortest distance from the starting node up to vertex
def get_shortest_distance(table, vertex):
    shortest_distance = table[vertex][DISTANCE]
    return shortest_distance


# finds the distance between any two nodes
def get_distance(graph, first_vertex, second_vertex):
    return graph[first_vertex][second_vertex]


def set_shortest_distance(table, vertex, new_distance):
    table[vertex][DISTANCE] = new_distance


# When we update the shortest distance of a node, we update its previous node
def set_previous_node(table, vertex, previous_node):
    table[vertex][PREVIOUS_NODE] = previous_node


# finds the minimum value in the shortest distance column from the starting nodes using the table.
def get_next_node(table, visited_nodes):
    unvisited_nodes = list(set(table.keys()).difference(set(visited_nodes)))
    # assumed to be the smallest in the shortest distance column of table
    assumed_min = table[unvisited_nodes[0]][DISTANCE]
    min_vertex = unvisited_nodes[0]
    for node in unvisited_nodes:
        #  If a lesser value is found, update the min_vertex
        if table[node][DISTANCE] < assumed_min:
            assumed_min = table[node][DISTANCE]
            min_vertex = node
    # returns min_vertex as the unvisited vertex or node with the smallest shortest distance from the source.
    return min_vertex


# The adjacency list for the diagram and table:
# The nested dictionary holds the adjacent nodes and the distance.
graph = dict()
graph['A'] = {'B': 5, 'D': 9, 'E': 2}
graph['B'] = {'A': 5, 'C': 2}
graph['C'] = {'B': 2, 'D': 3}
graph['D'] = {'A': 9, 'F': 2, 'C': 3}
graph['E'] = {'A': 2, 'F': 3}
graph['F'] = {'E': 3, 'D': 2}

# To print the table
shortest_distance_table = find_shortest_path(graph, table, 'A')
for k in sorted(shortest_distance_table):
    print("{} - {}".format(k, shortest_distance_table[k]))