# Given a string s, return true if s is a good string, or false otherwise.
# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).


from collections import defaultdict


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # occurs = {}
        # for char in s:
        #     if char not in occurs:
        #         occurs[char] = 1
        #     else:
        #         occurs[char] += 1
        # return len(set(occurs.values())) == 1

        occurs = defaultdict(int)
        for char in s:
            occurs[char] += 1
        return len(set(occurs.values())) == 1
