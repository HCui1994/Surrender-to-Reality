class Solution(object):
    def is_visited(self, path):
        # corner case
        if not path:
            return False
        # init  
        visited = set()
        current = (0, 0)
        visited.add(current)

        # core: trace path
        for direction in path:
            print(visited)
            current = list(current)
            if direction == 'N':
                current[0] -= 1
            elif direction == 'S':
                current[0] += 1
            elif direction == 'W':
                current[1] -= 1
            elif direction == 'W':
                current[1] += 1
            current = tuple(current)
            if current in visited:
                return True
            visited.add(current)
        return False


if __name__ == "__main__":
    path = "NWSNNWWSSSNSNWEEWSEW"
    soln = Solution()
    ans = soln.is_visited(path)
    print(ans)