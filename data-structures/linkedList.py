# create an array internally in our HashMap class
# 

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self, data):
        new_node = Node(data, None)
        if self.head == None:
            self.head = new_node 
        else:
            # we are inserting in the front 
            new_node.next = self.head
            # move the head to the head node
            self.head = new_node 