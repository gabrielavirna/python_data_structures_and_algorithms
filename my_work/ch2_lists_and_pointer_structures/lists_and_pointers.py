"""
Pointers
--------
 Ex:
 a house that you want to sell;
 a few Python functions that work with images, so you pass high-resolution image data between your functions.

 Those large image files remain in one single place in memory. What you do is create variables that hold the locations
 of those images in memory. These variables are small and can easily be passed around between different functions.


Pointers: allow you to point to a potentially large segment of memory with just a simple memory address.

In Python, you don't manipulate pointers directly (unlike C/Pascal).

s = set()

We would normally say that s is a variable of the type set. That is, s is a set. This is not strictly true, however.
The variable s is rather a reference (a "safe" pointer) to a set. The set constructor creates a set somewhere in memory 
and returns the memory location where that set starts. This is what gets stored in s.

Python hides this complexity from us. We can safely assume that s is a set and that everything works fine.



Array
------

- a sequential list of data;
- sequential = each element is stored right after the previous one in memory

If array is really big & you're low on memory => might be impossible to find large enough storage to fit entire array

Benefits:
Arrays are very fast: Since each element follows from the previous one in memory, there is no need to jump around
between different memory locations => important when choosing between a list and an array in real-world applications.


Pointer structures
------------------

- Contrary to arrays, pointer structures are lists of items that can be spread out in memory.
- Each item contains one or more links to other items in the structure
- Type of links are dependent on the type of structure:
    for linked lists => links to the next (and possibly previous) items in the structure,
    for a tree => parent-child links as well as sibling links
    in a tile-based game whith a game map built up of hexes, each node will have links to up to 6 adjacent map cells.

Benefits:
They don't require sequential storage space;
They can start small and grow arbitrarily as you add more nodes to the structure

But: for a list of ints, each node needs the space of an int & an additional int for storing the pointer to next node.
"""