# Create a Node class to create a node
class Node:

    # Initialise the Node object
    def __init__(self, data):
        self.data = data # assign data
        self.next = None # initialise next node as null

# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None # initialise the head as None

    # Search for a node in a linked list
    def search_list(self, the_list_head, key):
        
        # Base case
        if(not the_list_head): #if list is empty
            return False
        
        # If the item_type is found in current node, return True
        if(the_list_head.data == key):
            return True
        
        # Recur for the remaining list
        return self.search_list(the_list_head.next, key)
    
    # INSERTION

    # Insertion at the beginning of Linked List
    # Create a new_node with the given data
    # If head is empty, make new_node as head
    # Else insert current head at the next new_node and make the head equal to new_node
    def insert_at_begin(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    