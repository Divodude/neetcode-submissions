# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(node1,node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
             
            l=same(node1.left,node2.left)
            r=same(node1.right,node2.right)
            return node1.val==node2.val and l and r
        def trav(node):
            if not node:
                return False
            is_same=False
            if node.val==subRoot.val:
                is_same=same(subRoot,node)
            l=trav(node.left)
            r=trav(node.right)
            return  r or l or is_same 
        return trav(root)