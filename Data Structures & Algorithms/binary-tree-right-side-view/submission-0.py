# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        que=[root]
        ans=[]
        while que:

            level=[]
            n=len(que)
            count=0
            for n_ in range(n):
                
                node=que.pop(0)
                level.append(node.val)

                if node.right:
                    que.append(node.right)
                if node.left:
                    que.append(node.left)
                
            ans.append(level)
        result=[]
        for i in ans:
            result.append(i[0])
        return result