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
    
    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtBegin(data)
        
        curr = self.head
        while index > 1 or curr != None:
            curr = curr.next 

        if curr == None:
            print("Index not Found")
        
        curr.next = Node(data, None)
