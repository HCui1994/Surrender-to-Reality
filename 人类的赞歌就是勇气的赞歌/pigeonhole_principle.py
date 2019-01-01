"""
题目描述：
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
prove that at least one duplicate element must exist. Assume that there is only one duplicate number, find the duplicate one.
Note:
You must not modify the array (assume the array is read only).
You must use only constant extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

题目大意：
给定一个包含n + 1个整数的数组，其中每一个整数均介于[1, n]之间，证明其中至少有一个重复元素存在。假设只有一个数字出现重复，找出这个重复的数字。
注意：
不可以修改数组（假设数组是只读的）
只能使用常数空间
运行时间复杂度应该小于O(n^2)
数组中只存在一个重复数，但是可能重复多次
"""

"""
解法一：快慢双指针

问题的第一部分 - 证明至少存在一个重复元素 - 是鸽笼原理的直接应用。如果元素的范围是[1, n]，那么只存在 n 种不同的值。如果有 n+1 个元素，其中一个必然重复。
问题的第二部分 - 在给定约束条件下寻找重复元素。

解决本题需要的主要技巧就是要注意到：
由于数组的 n + 1 个元素范围从 1 到 n ，我们可以将数组考虑成一个从集合{1, 2, ..., n}到其本身的函数f。这个函数的定义为f(i) = A[i]。
基于这个设定，重复元素对应于一对下标i != j满足 f(i) = f(j)。
我们的任务就变成了寻找一对(i, j)。一旦我们找到这个值对，只需通过f(i) = A[i]即可获得重复元素。

"""