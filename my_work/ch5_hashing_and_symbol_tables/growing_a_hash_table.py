"""
Growing a hash table
--------------------
In ex, the hash table's size was set to 256. But, as we add elements to the list, we begin to fill up the empty slots.
At some point, all the slots will be filled up & table will be full. To avoid it, grow the table when it's getting full.

=> Compare the size(the total no. of slots) & the count(the he no. of those slots that contained elements)
If count = size => we have filled up the table.

The hash table's Load Factor => how large a portion of the available slots are being used.
Def: load factor = n/k, n= no. of used slots, k = total no. of slots

- When do we grow the table? as the load factor approaches 1 (before, in order to avoid gets becoming too slow: 0.75)
- How much to grow the table by?


Open addressing - Strategies:
---------------

The collision resolution mechanism -  used in hash_table.py, linear probing - used a fixed interval between our probes.
----------------------------------
- Chaining; All other share the idea that there is an array of slots. When we want to insert a key, we check whether
the slot already has an item or not. If it does, we look for the next available slot.

If we have a hash table that contains 256 slots => 256 = maximum no. of elements in that hash.
Moreover, as the load factor increases, it will take longer to find the insertion point for the new element.
Because of these limitations => prefer to use a different strategy to resolve collisions, such as chaining.

Chaining
--------
- a strategy for resolving conflicts and avoiding the limit to the number of elements in a hash table.

-> Chaining using lists
-----------------------
- the slots in the hash table are initialized with empty lists; all are lists that can grow as needed.
- When an element is inserted, it will be appended to the list that corresponds to that element's hash value =>
if 2 elements have same hash value=1167, both will both be added to the list that exists in slot 1167 of the hash table.

Benefits:
- Chaining avoids conflict by allowing multiple elements to have the same hash value.
- Avoids the problem of insertions as the load factor increases, since we don't have to look for a slot.
- The hash table can hold more values than the number of available slots, since each slot holds a list that can grow.

Of course, if a particular slot has many items, searching them can get very slow, since we have to do a linear search
through the list until we find the element that has the key we want. This can slow down retrieval, which is not good,
since hash tables are meant to be efficient.

-> Chaining using BST
---------------------
- Allows for fast searching; put an (initially empty) BST in each slot
- potential problem: depending on the order in which the items were added to the BST, we could
end up with a search tree that is as inefficient as a list: each node in the tree has exactly one child =>
To avoid this, we would need to ensure that our BST is self-balancing.


Symbol tables
-------------
- allow a compiler or an interpreter to keep track of the symbols (variable, function, class, and so on) that have been
declared and retrieve all information about it.
- often built using hash tables, since it is important to efficiently retrieve a symbol in the table.

E.g.:

    name = "Joe"
    age = 27

=> two symbols: name and age; each symbol has a value: name -> Joe and age -> 27
- Symbols belong to a namespace, which could be __main__ or the name of a module if you placed it there.
- A symbol table allows the compiler/the interpreter to look these values up.
The symbols name and age become the keys in our hash table. All the other information associated with it, such as the
value, become part of the value of the symbol table entry.

Not only variables are symbols, but functions and classes as well. They will all be added to our symbol table, so that
when any one of them needs to be accessed, they are accessible from the symbol table:

    def greet():
        print("Hello")

    Symbol      Type        Value
    ------------------------------
    greet     function    <function>
    name        str     "John"
    age         int       33

In Python, each module that is loaded has its own symbol table. The symbol table is given the name of that module =>
modules act as namespaces. We can have multiple symbols called age, as long as they exist in different symbol tables.
To access either one, we access it through the appropriate symbol table:

    list  -> symbol table,      table  -> symbol table,     - - main - - -> symbol table
"""

