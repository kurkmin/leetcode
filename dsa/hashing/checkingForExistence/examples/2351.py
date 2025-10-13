class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # runtime: n
        # space (memory): 1
        # myDict = {}
        # for char in s:
        #     if char not in myDict:
        #         myDict[char] = 1
        #     else:
        #         myDict[char] += 1
        #     if myDict[char] == 2:
        #         return char
        # efficient solution:
        seen = set()
        for char in s:
            if char in seen:
                return char
            seen.add(char)
        return " "
