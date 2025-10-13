class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        largest = -1
        for num in counts:
            if counts[num] == 1:
                if num > largest:
                    largest = num
        return largest
