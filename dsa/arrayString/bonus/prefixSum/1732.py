class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # n time complexity
        # n time complexity
        # altitude = [0]
        # for i in range(len(gain)):
        #     alt = altitude[-1] + gain[i]
        #     print(alt)
        #     altitude.append(alt)
        # return max(altitude)
        # we do not have to get
        # the full list of altitude
        # just get the highest one

        # model solution
        # n time complexity
        # 1 space complexity
        curr = highest = 0
        for gap in gain:
            curr += gap
            if curr > highest:
                highest = curr
        return highest
