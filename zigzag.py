# Given a binary tree, return the zigzag level order traversal of its nodes' values.
# (ie, from left to right, then right to left for the next level and alternate between).

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return None

        res = []
        level = 0
        self.zigzag_helper(root, level, res)
        return res

    def zigzag_helper(self, root, level, res):
        if root is None:
            return None
        if len(res) < level+1:
            res.append([])
        if level % 2 == 1:
            res[level].append(root.val)
        else:
            res[level].insert(0, root.val)

        self.zigzag_helper(root.right, level+1, res)
        self.zigzag_helper(root.left, level+1, res)
