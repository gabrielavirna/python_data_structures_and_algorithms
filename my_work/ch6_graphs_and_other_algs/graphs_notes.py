"""
Graphs and Other Algorithms
---------------------------
Graphs - used to solve a number of computing problems.
They also have much less structure than other data structures and things like traversal can be much more unconventional.

Graphs
-------
- a set of vertices and edges that form connections between the vertices;
- a graph G is an ordered pair of a set V of vertices and a set E of edges given as G = (V, E) - formal math. notation.

Definitions of a graph:
-----------------------
Node or vertex: A point, usually represented by a dot in a graph. The vertices or nodes are A, B, C, D, and E.
Edge: This is a connection between two vertices. The line connecting A and B is an example of an edge.
Loop: When an edge from a node is incident on itself, that edge forms a loop.
Degree of a vertex: This is the number of vertices that are incident on a given vertex. The degree of vertex B is 4.
Adjacency: This refers to the connection(s) between a node and its neighbor.
           The node C is adjacent to node A because there is an edge between them.
Path: A sequence of vertices where each adjacent pair is connected by an edge.


Directed and undirected graphs
------------------------------
-> Undirected graph: simply represents edges as lines between the nodes. There is no additional information about the
relationship between the nodes than the fact that they are connected.

-> Directed graph: the edges provide orientation in addition to connecting nodes. The edges, which will be drawn as
lines with an arrow, will point in which direction the edge connects the two nodes.
The arrow of an edge determines the flow of direction. One can only move from A to B if A -> B and not B -> A.

Weighted graphs
---------------
A weighted graph adds a bit of extra information to the edges. This can be a numerical value that indicates something.

E.g. A graph that indicates different ways to get from point A to point D. You can either go straight from A to D, or
choose to pass through B and C. Associated with each edge is the amount of time in minutes the journey to the next node
will take: A->B(5), B->C(10), C->D(10), A->D(40). Perhaps the journey AD would require you to ride a bike (or walk).
B and C might represent bus stops. At B you would have to change to a different bus. CD may be a short walk to reach D.

In this example, AD and ABCD represent two different paths.
A path is simply a sequence of edges that you pass through between two nodes. Following these paths, you see that the
total journey AD takes 40 minutes, whereas the journey ABCD takes 25 minutes. If your only concern is time, you would
be better off traveling along ABCD, even with the added inconvenience of changing buses.

The fact that edges can be directed and may hold other information, such as time taken or whatever other value the move
along a path is associated with, indicates something interesting. In previous data structures that we have worked with,
the lines we have drawn between nodes have simply been connectors. Even when they had arrows pointing from a node to
another, that was easy to represent in the node class by using next or previous, parent or child.

With graphs, it makes sense to see edges as objects just as much as nodes. Just like nodes, edges can contain extra
information that is necessary to follow a particular path.
"""

