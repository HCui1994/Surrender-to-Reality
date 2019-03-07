import sys
sys.path.append("../..")

from playground.TreePlayground import BinaryTreeUtil, TreeNode



def traverse_with_budget(root, budget):
    import collections
    if not root:
        return 0
    queue = [root]
    cnt = 0
    level = 1
    ternimate = False
    while queue:
        temp_queue = []
        for node in queue:
            print(node.val, level, budget)
            if budget < level:
                ternimate = True
                break
            cnt += 1
            budget -= level
            if node.left:
                temp_queue.append(node.left)
            if node.right:
                temp_queue.append(node.right)
        if ternimate:
            break
        queue = temp_queue
        level += 1
    print(cnt)
        






root = BinaryTreeUtil.build_tree([1, 2, 3, 4, 5, 6, 7, 8, 9])
BinaryTreeUtil.pretty_print_tree(root)


traverse_with_budget(root, 10)