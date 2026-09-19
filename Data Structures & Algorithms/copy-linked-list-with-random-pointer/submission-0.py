"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        old2new = {}
        old = head
        while old:
            new = Node(x = old.val)
            old2new[old] = new
            old = old.next

        old = head
        while old:
            node = old2new[old]
            node.next = old2new[old.next] if old.next else None
            node.random = old2new[old.random] if old.random else None
            old = old.next

        return old2new[head]
