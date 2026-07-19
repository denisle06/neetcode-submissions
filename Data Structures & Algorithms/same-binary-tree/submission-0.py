class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            a, b = stack.pop()
            if a is None and b is None:
                continue
            if a is None or b is None or a.val != b.val:
                return False
            stack.append((a.left, b.left))
            stack.append((a.right, b.right))
        return True