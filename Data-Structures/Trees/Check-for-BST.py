#Given the root of a binary tree. Check whether it is a BST or not.
#Note: We are considering that BSTs can not contain duplicate Nodes.
#A BST is defined as follows:

#The left subtree of a node contains only nodes with keys less than the node's key.
#The right subtree of a node contains only nodes with keys greater than the node's key.
#Both the left and right subtrees must also be binary search trees.

class Solution:
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root, mini=-4294967296, maxi=4294967296):
        if root is None:
            return True
        if root.data<mini or root.data>maxi:
            return False
        return self.isBST(root.left,mini,root.data-1) and self.isBST(root.right,root.data+1,maxi)
