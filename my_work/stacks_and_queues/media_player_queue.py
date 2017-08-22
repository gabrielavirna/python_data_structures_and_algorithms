"""
Application of queues
----------------------
Queues - used to implement a variety of functionalities in computer land:
- instead of providing each computer on a network with its own printer, a network of computers can be made to share one
printer by queuing what each printer wants to print. When the printer is ready to print, it will pick one of the items
(jobs) in the queue to print out.

- Operating systems also queue processes to be executed by the CPU.

Media player queue - implement a playlist queue that plays songs in the FIFO manner
------------------
Most music player software allows users to add songs to a playlist. Upon hitting the play button, all the songs in the
main playlist are played one after the other. The sequential playing of the songs can be implemented with queues because
the first song to be queued is the first song that is played => FIFO

Media player queue will only allow: the addition of tracks & a way to play all the tracks in the queue
The media player queue is made up of nodes.
When a track is added to the queue, the track is hidden in a newly created node and associated with the data attribute
of the node. That explains why we access a node's track object through the data property of the node which is returned
by the call to dequeue. Instead of our node object just storing just any data, it stores tracks in this case.

"""

from random import randint
import time


# The class represents any MP3 track or file that contains music
# Each track holds a reference to the title & the length of the song

# uses the double-linked-list node
class Node:
    # The prev variable holds a reference to the previous node, the next variable holds a reference to the next node
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class NodeBasedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0  # To count the number of nodes in Queue

    # enqueue: nodes are added to the queue - same append operation from doubly linked list
    def enqueue(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    # def dequeue: removes the node at the front of the queue
    def dequeue(self):
        current = self.head
        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1


class Track:
    def __init__(self, title=None):
        self.title = title
        self.length = randint(5, 10) # random length simulates the number of seconds it takes to play a song or track


# MediaPlayerQueue class - inherit from the queue class
# is a queue that holds a number of track objects in a queue
class MediaPlayerQueue(NodeBasedQueue):
    def __init__(self):
        super(MediaPlayerQueue, self).__init__()

    # add tracks to the queue
    # it creates a Node using the track object (as the node's data) & points to the tail if the queue is not empty,
    # or both head & tail if the queue is empty, to this new node.
    def add_track(self, track):
        self.enqueue(track)

    # Assuming the tracks in the queue are played sequentially from the first track added to the last
    # (FIFO), the play function has to loop through the elements in the queue:
    def play(self):
        while self.count > 0:
            current_track_node = self.dequeue()
            print("Now playing {}".format(current_track_node.data.title))
            time.sleep(current_track_node.data.length)


track1 = Track("white whistle")
track2 = Track("gold butter")
track3 = Track("Oh black star")
track4 = Track("Watch that chicken")
track5 = Track("Don't go")
print(track1.length, track2.length, track3.length, track4.length, track5.length)

# tracks are played in the order in which they were queued
# When playing the track, the system also pauses for the number of seconds equal to that of the length of the track
media_player = MediaPlayerQueue()
media_player.add_track(track1)
media_player.add_track(track2)
media_player.add_track(track3)
media_player.add_track(track4)
media_player.add_track(track5)
media_player.play()




