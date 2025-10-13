# Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers,
# return the list of integers that are present in each array of nums sorted in ascending order.

# from collections import defaultdict

# class Solution:
#     def intersection(self, nums: List[List[int]]) -> List[int]:
#         counts = defaultdict(int)
#         for i in nums:
#             for j in i:
#                 counts[j] += 1
#         ans = []
#         occur = len(nums)
#         for num in counts:
#             if counts[num] == occur:
#                 ans.append(num)
#         return sorted(ans)

from collections import defaultdict


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)
        for arr in nums:
            for x in arr:
                counts[x] += 1

        n = len(nums)
        ans = []
        for key in counts:
            if counts[key] == n:
                ans.append(key)

        return sorted(ans)
