class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                
            ans.append(level)
        return ans 
                

        