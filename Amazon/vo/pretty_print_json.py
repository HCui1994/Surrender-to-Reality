class Solution(object):
    def pretty_print_json(self, json):
        self.idx = 0
        self.json = json
        self.obj()

    def obj(self, indent=""):
        print(indent, end="")
        while self.idx < len(self.json):
            if self.json[self.idx] == '{':
                print('{')
                self.idx += 1
                self.obj(indent + "\t")
            elif self.json[self.idx] == '}':
                print()
                print(indent[:-1] + "}", end="")
                self.idx += 1
                return
            elif self.json[self.idx] == '[':
                print('[')
                self.idx += 1
                self.grp(indent + "\t")
            elif self.json[self.idx] == ',':
                print(',')
                print(indent, end="")
                self.idx += 1
            else:
                print(self.json[self.idx], end="")
                self.idx += 1
            
    def grp(self, indent):
        print(indent, end="")
        while self.idx < len(self.json):
            if self.json[self.idx] == '{':
                print('{')
                self.idx += 1
                self.obj(indent + "\t")
            elif self.json[self.idx] == ']':
                print()
                print(indent[:-1] + "]", end="")
                self.idx += 1
                return
            elif self.json[self.idx] == '[':
                print('[')
                self.idx += 1
                self.grp(indent + "\t")
            elif self.json[self.idx] == ',':
                print(',')
                peint(indent, end="")
                self.idx += 1
            else:
                print(self.json[self.idx], end="")
                self.idx += 1




json = "{{},{},{{{},{{[],[]},[{}]}}}}"
soln = Solution()
soln.pretty_print_json(json)

