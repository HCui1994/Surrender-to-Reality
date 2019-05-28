class Path(object):
    def simplify_path(self, path_str):
        stack = ['#']
        path = path_str.split('/')
        for directory in path:
            if directory == '.' or directory == "":
                continue
            if directory == '..':
                stack.pop()
                continue
            stack.append(directory)
        print(stack)