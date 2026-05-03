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
        dummy = Node(0)
        copied = dummy
        curr = head
        nodeFactory = {}
        while curr:
            if curr not in nodeFactory:
                nodeFactory[curr] = Node(curr.val)
            if curr.next and curr.next not in nodeFactory:
                nodeFactory[curr.next] = Node(curr.next.val)
            if curr.random and curr.random not in nodeFactory:
                nodeFactory[curr.random] = Node(curr.random.val)
            copied.next = nodeFactory[curr]
            copied = copied.next
            copied.next = nodeFactory.get(curr.next)
            copied.random = nodeFactory.get(curr.random)

            curr = curr.next
        return dummy.next

        