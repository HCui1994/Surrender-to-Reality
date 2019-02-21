"""
You are given two jugs with capacities x and y litres. 
There is an infinite amount of water supply available. 
You need to determine whether it is possible to measure exactly z litres using these two jugs.
If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:
1.  Fill any of the jugs completely with water.
2.  Empty any of the jugs.
3.  Pour water from one jug into another till the other jug is completely full or the first jug itself is empty

Example 1: (From the famous "Die Hard" example)
Input: x = 3, y = 5, z = 4
Output: True

Example 2:
Input: x = 2, y = 6, z = 5
Output: False
"""

class Solution:
    def __init__(self):
        self.x = self.y = self.z = 0
        self.memo = set([])

    def can_measure_water_recursive(self, x, y, z):
        """
        递归。如何判断无法 measure？会没有递归出口?
        添加备忘，如果曾经遇到某个状态，就直接返回
        RE: RecursionError: maximum recursion depth exceeded in comparison
        """
        if z > x + y:
            return False
        self.x, self.y, self.z = x, y, z
        # status = (0, 0)
        # self.memo.add(status)
        return self._traversal((0, 0))
    
    def _traversal(self, status):
        print(status)
        if sum(status) == self.z:
            return True
        if status in self.memo:
            return False
        x, y = status
        args = []
        # fill x with water
        args.append((self.x, y))
        # fill y with water
        args.append((x, self.y))
        # empty x
        args.append((0, y))
        # empty y
        args.append((x, 0))
        # pour x to y
        args.append((min(x + y, self.x), (x + y) - min(x + y, self.x)))
        # pout y to x
        args.append(((x + y) - min(x + y, self.y), min(x + y, self.y)))
        self.memo.add(status)
        result = False
        for arg in args:
            result = result or self._traversal(arg)
            if result:
                break
        return result

    def can_measure_water_iterative(self, x, y, z):
        """
        换个思路，即然递归会导致过深，就递推
        TLE
        """
        if z > x + y:
            return False
        if x > y:
            temp = x
            x = y
            y = temp
        queue = [(0, 0)]
        visited = set((0, 0))
        while queue:
            a, b = queue.pop(0)
            if a + b == z:
                return True
            states = set()
            states.add((x, b)) # fill jar x;
            states.add((a, y)) # fill jar y;
            states.add((0, b)) # empty jar x;
            states.add((a, 0)) # empty jar y;
            states.add((min(x, b + a), a + b - min(x, b + a))) # pour jar y to x;
            states.add((a + b - min(b + a, y), min(b + a, y))) # pour jar x to y;
            for state in states:
                if state in visited:
                    continue;
                queue.append(state)
                visited.add(state)
            print(queue)
        return False

    def can_measure_water_math(self, x, y, z):
        """ 
        如果 z 可用 x y 测量，z 必然是 x 和 y 的某一个线性组合。why？？？
        即 z = kx + ly其中k和l是常数，z是可测量的
        如果 g 是 x 和 y 的 gcd，那么 x = ag, y = bg
        z = kag + lbg = (ka + lb)g  -> 这表明 z 若可用 x y 测量，必须可被 g 整除
        """
        if x + y < z:
            return False
        def gcd(x, y):
            #Using Euclid's algorithm - https://en.wikipedia.org/wiki/Greatest_common_divisor
            if x < y : 
                x, y = y, x
            while x != y and y != 0 :
                x, y = y, x % y
            return x        
        g = gcd(x,y)
        if g == 0:
            return z == 0
        return z % g == 0 

    def test(self):
        x, y, z = 22003, 31237, 1
        print(self.can_measure_water_math(x, y, z))


soln = Solution()
soln.test()