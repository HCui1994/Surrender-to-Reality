class CollideEvaluator(object):
    def collisions(self, asteroids):
        stack = []
        for a in asteroids:
            if not stack:
                stack.append(a)
            elif a > 0:
                stack.append(a)
            else:
                while stack and stack[-1] > 0:
                    if abs(stack[-1]) < abs(a):
                        survive = True
                        stack.pop()
                    elif abs(stack[-1]) == abs(a):
                        stack.pop()
                        survive = False
                        break
                    elif abs(stack[-1]) > abs(a):
                        survive = False
                        break
                    if survive:
                        stack.append(a)
        return stack