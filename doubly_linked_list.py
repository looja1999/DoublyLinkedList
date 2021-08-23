# Doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
         if self.head is None:
             new_node = Node(data)
             new_node.prev = None
             self.head = new_node
         else:
             new_node = Node(data)
             cur = self.head
             while cur.next:
                 cur = cur.next
             cur.next = new_node
             new_node.prev = cur
             new_node.next = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

dlist = DoublyLinkedList()
dlist.prepend(0)
dlist.append(1)
dlist.append(2)
dlist.append(3)
dlist.append(4)
dlist.prepend(10)

dlist.print_list()
