class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def trav(node):
            if not node:
                return 
            node.left=trav(node.left)
            node.right=trav(node.right)
            if not  node.left and not node.right and node.val==target:
                return None
            return node
        return trav(root)
        
        