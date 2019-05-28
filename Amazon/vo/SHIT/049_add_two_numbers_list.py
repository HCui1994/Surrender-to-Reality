class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedListUtil(object):
    def add(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        l1_stack = self.list_2_str(list1)
        l2_stack = self.list_2_str(list2)
        res_stack = []
        carry = 0
        while l1_stack and l2_stack:
            val1, val2 = l1_stack.pop(), l2_stack.pop()
            val, carry = divmod(val1 + val2 + carry, 10)
            res_stack.append(val)
        while l1_stack:
            val1 = l1_stack.pop()
            val, carry = divmod(val1 + carry, 10)
            res_stack.append(val)
        while l2_stack:
            val2 = l2_stack.pop()
            val, carry = divmod(val2 + carry, 10)
            res_stack.append(val)
        if carry:
            res_stack.append(carry)
        
        head = ListNode("dummy")
        node = head
        while res_stack:
            node.next = ListNode(res_stack.pop())
            node = node.next
        return head.next
            
        
    def list_2_str(self, node):
        if not node:
            return []
        return [node.val] + self.list_2_str(node.next)