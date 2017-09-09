from collections import deque

"""
Graph traversal
---------------
Since graphs don't necessarily have an ordered structure, traversing a graph can be more involving.
Traversal normally involves keeping track of which nodes or vertices have already been visited and which ones have not.

Strategies:
-> follow a path until a dead end is reached, then walk back up until there's a point where there's an alternative path.
-> or iteratively move from one node to another in order to traverse the full graph or part of it.

I.Breadth-first search - algorithm for graph traversal - use of a queue
----------------------
- Worst-case scenario: each vertex or node and edge will be traversed, thus the time complexity of the algorithm is:
    O(|V| + |E|), where |V| is the number of vertices or nodes while |E| is the number of edges in the graph.
    
- algorithm starts at a node, chooses that node or vertex as its root node, and visits the neighboring nodes,
after which it explores neighbors on the next level of the graph.

- use of a queue. The algorithm creates a list to store the nodes that have been visited as the traversal process
proceeds. We shall start our traversal from node A.


II. Depth-first search - algorithm for graph traversal - use of a stack
----------------------
- this algorithm traverses the depth of any particular path in the graph before traversing its breadth <=> 
    child nodes are visited first before sibling nodes. 

- DFS usage: in solving maze problems, finding connected components, finding the bridges of a graph, among others.

- It works on finite graphs and requires the use of a stack to maintain the state of the algorithm


Other useful graph methods
--------------------------
- Find the longest path

- Find the shortest path between nodes:

- very often there's need of finding a path between two nodes, find all the paths between nodes 
-> In an unweighted graph, the shortest path: the path with the lowest number of edges between them. 
-> In a weighted graph, it could involve calculating the total weight of passing through a set of edges.
"""


# I. Breadth-first search - using a queue
def breadth_first_search(graph, root):
    # list to store the nodes that have been visited
    visited_vertices = list()
    # Root node is queued and added to the list of visited nodes
    graph_queue = deque([root])
    visited_vertices.append(root)
    node = root

    while len(graph_queue) > 0:
        # Root node is dequeued
        node = graph_queue.popleft()
        adj_nodes = graph[node]

        # find the nodes that are in adj_nodes but not in visited_vertices
        remaining_elements = set(adj_nodes).difference(set(visited_vertices))
        if len(remaining_elements) > 0:
            # Its unvisited adjacent nodes are sorted in alphabetical order and queued up.
            # These nodes are also added to the list of visited nodes.
            for elem in sorted(remaining_elements):
                visited_vertices.append(elem)
                graph_queue.append(elem)

    return visited_vertices


# II. Depth-first search - using a stack
def depth_first_search(graph, root):
    # list to store the nodes that have been visited
    visited_vertices = list()
    # using a regular Python list as a stack
    graph_stack = list()

    # node is pushed on the stack
    graph_stack.append(root)
    node = root

    while len(graph_stack) > 0:
        # If node is not in the list of visited nodes, we add it.
        if node not in visited_vertices:
            visited_vertices.append(node)

        # node is passed with the graph's adjacency matrix
        adj_nodes = graph[node]

        # If all the adjacent nodes have been visited, we pop that node (top) from the stack
        if set(adj_nodes).issubset(set(visited_vertices)):
            graph_stack.pop()
            if len(graph_stack) > 0:
                # set node to the top node on the stack
                node = graph_stack[-1]
                # jumps back to the beginning of the while loop's test condition
            continue

        else:
            # if not all the adjacent nodes have been visited
            # find the nodes that are in adj_nodes but not in visited_vertices
            remaining_elements = set(adj_nodes).difference(set(visited_vertices))

            # The first item within sorted(remaining_elements) is assigned to first_adj_node
            first_adj_node = sorted(remaining_elements)[0]
            # and pushed onto the stack
            graph_stack.append(first_adj_node)
            # point the top of the stack to this node
            node = first_adj_node
    return visited_vertices


# The adjacency list for the graph:

graph1 = dict()
graph1['A'] = ['B', 'G', 'D']
graph1['B'] = ['A', 'F', 'E']
graph1['C'] = ['F', 'H']
graph1['D'] = ['F', 'A']
graph1['E'] = ['B', 'G']
graph1['F'] = ['B', 'D', 'C']
graph1['G'] = ['A', 'E']
graph1['H'] = ['C']

print(breadth_first_search(graph1, 'A'))

# he adjacency list of the graph:

graph2 = dict()
graph2['A'] = ['B', 'S']
graph2['B'] = ['A']
graph2['S'] = ['A', 'G', 'C']
graph2['D'] = ['C']
graph2['G'] = ['S', 'F', 'H']
graph2['H'] = ['G', 'E']
graph2['E'] = ['C', 'H']
graph2['F'] = ['C', 'G']
graph2['C'] = ['D', 'S', 'E', 'F']

print(depth_first_search(graph2, 'A'))
