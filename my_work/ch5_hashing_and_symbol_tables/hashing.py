"""
Hashing and Symbol Tables
-------------------------
Lists vs Dictionary

-> Lists:
- items are stored in sequence and accessed by index number
- Index numbers work well for computers; They are integers so they are fast and easy to manipulate.

However - If we have an address book entry, with index number 56, that number doesn't tell us much. There is nothing to
link a particular contact with number 56. It just happens to be the next available position in the list.

-> Dictionary
- a similar structure; a dictionary uses a keyword instead of an index number. So, if that contact was called James,
we would probably use the keyword James to locate the contact. That is, instead of accessing the contact by calling
contacts [56], we would use contacts ["james"].

- often built using hash tables; hash tables rely on a concept called hashing


Hashing
-------
- the concept of converting data of arbitrary size into data of fixed size:
    used this to turn strings (or possibly other data types) into integers
    E.g. hash the expression hello world <=> get a numeric value that represents the string

- ord() function: get the ordinal value of any character
    To get the hash of the whole string, sum the ordinal numbers of each character in the string:
    (If the order of the characters in the string is changed, we still get the same hash for both different strings)

     sum(map(ord, 'world hello')) => 1116 (same as sum(map(ord, 'hello world')))

    since >>> ord('f') => 102; ord('g') => 103; ord('w') => 119; ord('x') => 120
    sum(map(ord, 'hello world')) => 116 (same as sum(map(ord, 'gello xorld')


Perfect hashing functions
-------------------------
- one function in which each string is guaranteed to be unique
In practice, hashing functions need to be very fast => creating a function that will give each string a unique
hash value is normally not possible. Instead, we sometimes get collisions (2/more strings having the same hash value).
We need a strategy for resolving collisions. To avoid some of the collisions: Add a multiplier => see myhash() function.
"""


def my_hash(s):
    multiplier = 1
    hash_value = 0
    for ch in s:
        # hash value for each character becomes the multiplier value * the ordinal value of the character
        hash_value += multiplier * ord(ch)
        # The multiplier then increases as we progress through the string
        multiplier += 1
    return hash_value

# This time we get different hash values for our strings
for item in ('hello world', 'world hello', 'gello xord'):
    print("{}: {}".format(item, my_hash(item)))

