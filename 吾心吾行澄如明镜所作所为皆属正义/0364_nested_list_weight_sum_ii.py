"""
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
Each element is either an integer, or a list -- whose elements may also be integers or other lists.
Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. 
i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 8 
Explanation: Four 1's at depth 1, one 2 at depth 2.
Example 2:

Input: [1,[4,[6]]]
Output: 17 
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17.
"""


class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """



class Solution:
    def __init__(self):
        self._max_depth = 0

    def depth_sum_inverse(self, nestedList):
        for l in nestedList:
            self._find_max_depth(l, 1)
        summation = 0
        for l in nestedList:
            summation += self._calc_weighted_sum(l, 0)
        return summation

    def _find_max_depth(self, node : NestedInteger, depth):
        self._max_depth = max(self._max_depth, depth)
        if node.isInteger():
            return
        for l in node.getList():
            self._find_max_depth(l, depth + 1)
    
    def _calc_weighted_sum(self, node : NestedInteger, depth):
        if node.isInteger():
            return (self._max_depth - depth) * node.getInteger()
        summation = 0
        for l in node.getList():
            summation += self._calc_weighted_sum(l, depth + 1)
        return summation
        
