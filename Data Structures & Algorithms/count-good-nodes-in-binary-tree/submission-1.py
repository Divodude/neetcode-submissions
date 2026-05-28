# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good=0
        def trav(node,pm):
            if not node:
                return 
            
            if node.val>=pm:
                self.good+=1
            pm=max(node.val,pm)
            trav(node.left,pm)
            trav(node.right,pm)
        trav(root,-1000)
        return self.good
        