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

    # Insert a node at a specific position in a Linked List

    # Create a new_node with the given data, a current_node equals to the head
    # and a counter 'position' initialises with 0. 
    # If index equals to 0 -> node inserted at begin => use insert_at_begin()
    # Else loop until current_node is not equal to None or (position+1) is not equal
    # to the index we have to at the one position back to insert at a given position to make the 
    # linking of nodes and in each iteration, we increment the position by 1 and make current_node next of it.
    # When loop breaks and if current_node is not equal to None, insert a new_node after the current_node
    # If current_node is equal to None, index is not present

    # Indexing starts from 0
    def insert_at_index(self, data, index):
        new_node = Node(data)
        current_node = self.head
              
        if index == 0:
            self.insert_at_begin(data)
        else:

            position = 1

            while(current_node != None and position < index):
                current_node = current_node.next
                position = position + 1            
            
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present.")
    
    # Insert in Linked List at End
    # Create a new_node with the given data and check if
    # head is empty.
    # If head is empty, make new_node as head
    # Else make current_node equal to head and traverse to
    # last node

    # keep a TAIL of linked list -> O(1)
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while(current_node.next):
            current_node = current_node
        current_node.next = new_node

    # Delete node in a linked list
    # Remove first node from linked list
    # Make the second node head of the linked list
    def remove_first_node(self):
        if(self.head == None):
            return
        
        self.head = self.head.next
        # aware that remove the node you are trying to delete

    # Remove last node from linked list
    # Traverse to the second last node
    # Make the next node of that node None
    def remove_last_node(self):
        if self.head is None:
            return
        
        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next

        current_node.next = None

    # Delete node at a given index
    # Traverse to one node before
    # Make current node equal to the node next to which we
    # want to remove
    def remove_at_index(self, index):
        if self.head == None:
            return
        
        current_node = self.head
        if index == 0:
            self.remove_first_node()

        else:
            position = 1
            while(current_node != None and position < index):
                current_node = current_node.next
                position += 1

            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    # Delete a node of a given data
    # While loop until current_node becomes None or data of
    # the next node equal to the given data
    def remove_node(self, data):
        current_node = self.head

        while(current_node != None and current_node.next.data != data):
            current_node = current_node.next
        
        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next