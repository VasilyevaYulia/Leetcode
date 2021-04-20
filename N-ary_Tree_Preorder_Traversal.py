#Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
#Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value 

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        l = [root]
        ans = []
        while l:
            c = l.pop()
            ans.append(c.val)
            l.extend(c.children[::-1])
        return ans
