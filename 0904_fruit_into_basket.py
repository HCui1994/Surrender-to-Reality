class Solution:
    def totalFruit(self, tree):
        if len(tree) <= 2:
            len(tree)
        curr_fruit_num = 1
        max_fruit_num = 0
        prev_fruit_num = 0
        post_prev_fruit_num = 0
        prev_fruit_type = -1
        post_prev_fuit_type = -1
        i = 1
        while i < len(tree):
            while tree[i] == tree[i-1]:
                curr_fruit_num += 1
                i += 1
            if tree[i-1] == post_prev_fuit_type and max_fruit_num < :
                pass
                    



        print(max_fruit_num)


solution = Solution()
tree = [1,2,3,4,3,3,3,2,2,2,2,3,4,5,6,6,,6,5,4,3,3,2,2,2,1,1,1,1,1]

