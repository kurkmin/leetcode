# Given a string s and an integer k,
# return the length of the longest substring of s that contains at most k distinct characters.

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # count the occurences of each char first
        # this is to do compare with k distinct chars later
        counts = defaultdict(int)
        # use sliding window
        ans = left = 0
        for right in range(len(s)):
            counts[s[right]] += 1
            while len(counts) > k:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1
            ans = max(ans, right - left + 1)
        return ans
