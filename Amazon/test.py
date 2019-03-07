import collections


class Solution(object):
    def insert(self, head: 'Node', insertVal: 'int') -> 'Node':
        if not head:
            node = Node(insertVal, None)
            node.next = node
            return node
        
        newNode = Node(insertVal, None)
        curr = head
        while True:
            # If the insert value is in between
            if curr.val <= insertVal <= curr.next.val:
                newNode.next, curr.next = curr.next, newNode
                break
            
            # If the insert value is the largest
            if curr.next.val < curr.val < insertVal:
                newNode.next, curr.next = curr.next, newNode
                break
                
            # If the insert value is the smallest
            if insertVal < curr.next.val < curr.val:
                newNode.next, curr.next = curr.next, newNode
                break
              
            # If the insert value is the largest element that 
            # is smaller than the head
            if curr.next is head:
                newNode.next, curr.next = curr.next, newNode
                break
            
            curr = curr.next
            
        return head