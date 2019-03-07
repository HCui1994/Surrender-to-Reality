"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        import collections
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append({"val": x, "min": x})
        else:
            self.stack.append({"val": x, "min": min(x, self.stack[-1]["min"])})

    def pop(self) -> None:
        if not self.stack:
            return
        else:
            self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1]["val"]

    def getMin(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1]["min"]

        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()
