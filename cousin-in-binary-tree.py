# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return root
        queue = collections.deque()
        info = collections.defaultdict(tuple)
        depth = 0
        # (Node, Parent)
        queue.append((root, None))
        
        while any(queue):
            size = len(queue)
            for i in range(size):
                node, p = queue.popleft()
                if not node:
                    continue
                info[node.val] = (p, depth)
                queue.append((node.left, node))
                queue.append((node.right, node))
            depth += 1
        px, dx = info[x]
        py, dy = info[y]
        return px != py and dx == dy