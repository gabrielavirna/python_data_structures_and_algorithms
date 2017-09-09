"""
Hash table
----------
Use hashed keys to quickly and efficiently look up the value that corresponds to a key.

A) String Keys

- a form of list where elements are accessed by a keyword rather than an index number; a key-value store
At least, this is how the client code will see it. Internally, it will use a slightly modified version of our hashing
function in order to find the index position in which the element should be inserted. This gives us fast lookups,
since we are using an index number which corresponds to the hash value of the key.

Hash Table
-----------
-> using 2 operations: add elements to the hash using put() function & retrieve elements using get() method
-> treat our hash table as a list: with the special methods __setitem__() and __getitem__()



B) Non-string keys
If necessary, you could use any other Python type for keys. If you create your own class that you want to use as a key,
you will probably want to override the special __hash__() function for that class, so that you get reliable hash values.
Note that you would still have to calculate the modulo (%) of the hash value and the size of the hash table to get the
slot. That calculation should happen in the hash table and not in the key class, since the table knows its own size
(the key class should not know anything about the table that it belongs to).
"""


# Create a class to hold hash table items, which have a key and a value.
class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# Create a hash table class - table uses a standard Python list to store its elements (could use linked list)
class HashTable:
    def __init__(self):
        # total number of slots in the table (used/unused): 256 elements
        self.size = 256
        #  initialize a list containing 256 elements (slots/buckets)
        self.slots = [None for i in range(self.size)]
        # the number of slots that are filled
        # the number of actual elements(key-value pairs) added to the table
        self.count = 0

    # Add hashing function to the table - meant to be used internally by the class => underscore(_)
    # this _hash() function is going to generate the hash value of keys = strings
    def _hash(self, key):
        multiplier = 1
        hash_value = 0
        for ch in key:
            hash_value += multiplier * ord(ch)
            multiplier += 1
        # ensure that the hashing function returns a value in (1, 256) (table size)
        # by returning the remainder (is always going to be an int in (0, 255)
        return hash_value % self.size

    # I. put() and get()
    # Add elements to the hash
    def put(self, key, value):
        # embedding the key and the value into the HashItem class
        item = HashItem(key, value)
        # computing the hash of the key
        h = self._hash(key)

        # Now we need to find an empty slot. We start at the slot that corresponds to the hash value of the key.
        #  # If that slot is empty, we insert our item there; if the slot is not empty
        while self.slots[h] is not None:
            # if the key of the item is the same as our current key
            if self.slots[h].key is key:
                break
            # if not => collision => handle a conflict => this linear way of resolving collisions:
            h = (h + 1) % self.size
        # If this is a new element (that is, it contained None previously), increase count
        if self.slots[h] is None:
            self.count += 1
        # insert the item into the list at the required position:
        self.slots[h] = item

    # Returns the value that corresponds to a key
    def get(self, key):
        # Calculate the hash of the key
        h = self._hash(key)

        # start looking through the list for an element that has the key we are searching for
        while self.slots[h] is not None:
            # start at the element which has the hash value of the key that was passed in
            # if the current element is the correct one (If we find our key), return the value
            if self.slots[h].key is key:
                return self.slots[h].value
            # else, move to next slot (compute a new index)
            h = (h + 1) % self.size
        # if we find an element that contains None (key was not found in the table):
        return None

    # II. special methods __setitem__() and __getitem__()
    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

ht = HashTable()
ht.put("good", "eggs")
ht.put("better", "ham")
ht.put("best", "spam")
ht.put("ad", "do not")
ht.put("ga", "collide")

# I. Test code for put() and get() methods; using ht.get("good")
# key worst returns None, since the key does not exist
# The keys ad and ga also return their corresponding values => the collision between them is dealt with.
for key in ("good", "better", "best", "worst", "ad", "ga"):
    v = ht.get(key)
    print(v)

print("\n")

# II. Test code for special methods __setitem__() and __getitem__(); using ht["good"]
for key in ("good", "better", "best", "worst", "ad", "ga"):
    v = ht[key]
    print(v)
print("The number of elements is: {}".format(ht.count))