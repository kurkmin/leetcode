# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.

from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # counts: keep track of prefix sums
        # where its key: prefix sum
        # its value: occurences
        # this is to find a subarray whose sum is equal to k
        # prefix sum at index i - prefix sum at index j = k
        # , which can be expressed in a different way:
        # prefix sum at index i - k = prefix sum at index j
        # so if we find prefix sum at index j in our hashmap,
        # we can get a subarray whose value (# occurences) will be counted
        # we repeat this process, and return the counter variable value (ans)

        counts = defaultdict(int)
        # prefix sum (0) occurs once at least ?
        counts[0] = 1
        # answer: counter variable
        # curr: current prefix sum
        ans = curr = 0

        for num in nums:
            curr += num
            # understand how the occurences of curr - k, (which is prefix j), are added to ans
            ans += counts[curr - k]
            counts[curr] += 1

        return ans

        # can you solve this using brute force approach,
        # which is literally going through every possible subarray
        # * brute force approach (altho it cannot pass the test case #61):
        # # double nested loop (for & while)
        # cnt = 0
        # for i in range(len(nums)):
        #     j = i + 1
        #     while j <= len(nums):
        #         print("subArray: " + str((nums[i:j])))
        #         print("sum: " + str(sum(nums[i:j])))
        #         if sum(nums[i:j]) == k:
        #             cnt += 1
        #         j += 1
        #         print("cnt: " + str(cnt))
        #     print("for")
        # print(cnt)
        # return cnt

        # # double nested for loop
        # cnt = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums) + 1):
        #         if sum(nums[i:j]) == k:
        #             cnt += 1
        # return cnt
