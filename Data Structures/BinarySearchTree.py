class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self, root) -> None:
        self.root = root

    def search_node(self, root, data):
        print("data", data)
        
        if data < root.data:
            if root.left is None:
                return f'{data} NOT found'
            return self.search_node(root.left, data)
        elif data > root.data:
            if root.right is None:
                return f'{data} NOT found'
            return self.search_node(root.right, data)
        else:
            return f'{data} is found'

    # Find minimum node
    def find_minimum(self, root):
        if root is None:
            return "Tree is empty"
        
        # Set the min node to the root, traverse to the left most node
        # which is the minimum value of the tree
        min_node = root
        while min_node.left:
            min_node = min_node.left

        # Can return min_node.data to show the data or call .data in the print statement
        return min_node
    
    # Find maximum node
    def find_maximum(self, root):
        
        if(root is None):
            print("Tree is empty")

        # Set the min node to the root, traverse to the right most node
        # which is the maximum value of the tree
        max_node = root
        while max_node.right:
            max_node = max_node.right

        # Can return max_node.data to show the data or call .data in the print statement
        return max_node
    
    # Print the tree with in order traversal (left -> root -> right)
    def in_order_tree(self, node):
        if node is None:
            return
        
        self.in_order_tree(node.left)
        print(node.data)
        self.in_order_tree(node.right)

    # Pre order: root -> left -> right
    def pre_order_tree(self, node):
        if node is None: 
            return
        print(node.data)
        self.pre_order_tree(node.left)
        self.pre_order_tree(node.right)

    # Post order: left -> right -> root
    def post_order_tree(self, node):
        if node is None:
            return
        self.post_order_tree(node.left)
        self.post_order_tree(node.right)
        print(node.data)

    # Insert method to create nodes
    def insert(self, root, data):
        temp_node = root
        if temp_node:
            if data < temp_node.data:
                if temp_node.left is None:
                    temp_node.left = Node(data)
                else:
                    self.insert(temp_node.left, data) # temp_node become the new root to traverse

            elif data > temp_node.data:
                if temp_node.right is None:
                    temp_node.right = Node(data)
                else:
                    self.insert(temp_node.right, data)
            else:
                temp_node.data = data 

    def deleteNode(self, root, k):
        # Base case
        if root is None:
            return root
    
        # Recursive calls for ancestors of
        # node to be deleted
        if root.data > k:
            root.left = self.deleteNode(root.left, k)
            return root
        elif root.data < k:
            root.right = self.deleteNode(root.right, k)
            return root
    
        # We reach here when root is the node
        # to be deleted.
    
        # If one of the children is empty
        if root.left is None:
            temp = root.right
            del root
            return temp
        elif root.right is None:
            temp = root.left
            del root
            return temp
    
        # If both children exist
        else:
    
            successorParent = root
    
            # Find successor
            successor = root.right
            while successor.left is not None:
                successorParent = successor
                successor = successor.left
    
            # Delete successor.  Since successor
            # is always left child of its parent
            # we can safely make successor's right
            # right child as left of its parent.
            # If there is no succ, then assign
            # succ.right to succParent.right
            if successorParent != root:
                successorParent.left = successor.right
            else:
                successorParent.right = successor.right
    
            # Copy Successor Data to root
            root.data = successor.data
    
            # Delete Successor and return root
            del successor
            return root

root = Node(12)
# root.left = Node(3)
# root.right = Node(14)
# root.left.left = Node(2)
# root.left.right = Node(5)
tree = BinaryTree(root)
tree.insert(root, 3)
tree.insert(root, 14)
tree.insert(root, 2)
tree.insert(root, 5)
print("In order")
tree.in_order_tree(tree.root)

tree.deleteNode(root, 3)
print("In order after delete")
tree.in_order_tree(tree.root)
# print("Pre order")
# tree.pre_order_tree(tree.root)

# print("Post order")
# tree.post_order_tree(tree.root)

# print(tree.search_node(tree.root, 2))
# print(tree.search_node(tree.root, 1))
# print("minimum node", tree.find_minimum(root).data)
# print("maximum node", tree.find_maximum(root).data)