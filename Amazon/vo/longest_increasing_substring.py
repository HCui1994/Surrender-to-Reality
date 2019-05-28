class LongestIncreasingSubstring(object):
    def find_lis(self, string):
        if len(string) < 2:
            return string
        stack = []
        max_lis = ""
        for char in string:
            print(stack, char, max_lis)
            if not stack:
                stack.append(char)
            elif char.lower() >= stack[-1].lower():
                stack.append(char)
            else:
                if len(max_lis) < len(stack):
                    max_lis = "".join(stack)
                    stack = []
        return max_lis




if __name__ == "__main__":
    string = "aAdbdcdEzxycg"
    lis = LongestIncreasingSubstring()
    res = lis.find_lis(string)
    print(res)