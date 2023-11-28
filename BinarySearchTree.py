class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self, root) -> None:
        self.root = root

    # def search_node(self, data):
    #     if 
    # Insert method to create nodes
    # def insert(self, data):
    #     if self.root.data:
    #         if data < self.root.data:
    #             if self.root.left is None:
    #                 self.root.left = Node(data)
    #             else:
    #                 self.root.left.insert(data)
    #         elif data > self.root.data:
    #             if self.root.right is None:
    #                 self.root.right = Node(data)
    #             else:
    #                 self.root.right.insert(data)
    #         else:
    #             self.root.data = data

    # # findval method to compare the value with nodes
    # def findval(self, lkpval):
    #     if lkpval < self.data:
    #         if self.left is None:
    #             return str(lkpval)+" Not Found"
    #         return self.left.findval(lkpval)
    #     elif lkpval > self.data:
    #         if self.right is None:
    #            return str(lkpval)+" Not Found"
    #         return self.right.findval(lkpval)
    #     else:
    #         print(str(self.data) + ' is found')

    # # Find minimum node
    # def find_minimum(self, root):
        
    #     if(root is None):
    #         print("Tree is empty")

    #     # Set the min node to the root, traverse to the left most node
    #     # which is the minimum value of the tree
    #     min_node = root
    #     while min_node.left:
    #         min_node = min_node.left

    #     # Can return min_node.data to show the data or call .data in the print statement
    #     return min_node
    
    # # Find maximum node
    # def find_maximum(self, root):
        
    #     if(root is None):
    #         print("Tree is empty")

    #     # Set the min node to the root, traverse to the right most node
    #     # which is the maximum value of the tree
    #     max_node = root
    #     while max_node.right:
    #         max_node = max_node.right

    #     # Can return max_node.data to show the data or call .data in the print statement
    #     return max_node
    
    # Print the tree with in order traversal (left -> root -> right)
    def in_order_tree(self, node):
        if node is None:
            return
        
        self.in_order_tree(node.left)
        print(node.data)
        self.in_order_tree(node.right)

        # if self.root.left is not None:
        #     self.in_order_tree(self.root.left)
        # print(node.data)
        # if self.root.right is not None:
        #     self.in_order_tree(self.root.right)

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

# root = Node(12)

# tree.insert(6)
# tree.insert(14)
# tree.insert(3)
root = Node(12)
root.left = Node(3)
root.right = Node(14)
root.left.left = Node(2)
root.left.right = Node(5)
tree = BinaryTree(root)
print("In order")
tree.in_order_tree(tree.root)

print("Pre order")
tree.pre_order_tree(tree.root)

print("Post order")
tree.post_order_tree(tree.root)
# print(root.find_minimum(root).data)
# print(root.find_maximum(root).data)
# print(root.findval(7))
# print(root.findval(14))

# class Node:
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data

# # Insert method to create nodes
#     def insert(self, data):
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#             else:
#                 self.data = data

# # findval method to compare the value with nodes
#     def findval(self, lkpval):
#         if lkpval < self.data:
#             if self.left is None:
#                 return str(lkpval)+" Not Found"
#             return self.left.findval(lkpval)
#         elif lkpval > self.data:
#             if self.right is None:
#                return str(lkpval)+" Not Found"
#             return self.right.findval(lkpval)
#         else:
#             print(str(self.data) + ' is found')

#     # Find minimum node
#     def find_minimum(self, root):
        
#         if(root is None):
#             print("Tree is empty")

#         # Set the min node to the root, traverse to the left most node
#         # which is the minimum value of the tree
#         min_node = root
#         while min_node.left:
#             min_node = min_node.left

#         # Can return min_node.data to show the data or call .data in the print statement
#         return min_node
    
#     # Find maximum node
#     def find_maximum(self, root):
        
#         if(root is None):
#             print("Tree is empty")

#         # Set the min node to the root, traverse to the right most node
#         # which is the maximum value of the tree
#         max_node = root
#         while max_node.right:
#             max_node = max_node.right

#         # Can return max_node.data to show the data or call .data in the print statement
#         return max_node
    
#     # Print the tree with in order traversal (left -> root -> right)
#     def in_order_tree(self):
#         if self.left:
#             self.left.in_order_tree()
#         print(self.data)
#         if self.right:
#             self.right.in_order_tree()

# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)
# root.in_order_tree()
# # print(root.find_minimum(root).data)
# # print(root.find_maximum(root).data)
# # print(root.findval(7))
# # print(root.findval(14))