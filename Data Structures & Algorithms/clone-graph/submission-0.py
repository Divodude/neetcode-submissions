"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        que=[node]
        
        
        if not node:
            return None
        root={node:Node(node.val)}
        
        while que:
            
            nde=que.pop(0)

            for nei in nde.neighbors:
                if nei not in root:
                    root[nei]=Node(nei.val)
                    que.append(nei)
                root[nde].neighbors.append(root[nei])
        return root[node]
        