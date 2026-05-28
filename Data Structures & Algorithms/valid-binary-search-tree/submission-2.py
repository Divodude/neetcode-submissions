# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.nums=[]
        def trav(node):
            if not node:
                return 
            
            trav(node.left)
            self.nums.append(node.val)
            trav(node.right)
        trav(root)
        print(self.nums)
                
        return self.nums==sorted(self.nums) and len( self.nums)==len(set(self.nums))

        