class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # create result list 
        result = []
        # find the greatest one without giving extra candies
        max = 0
        for candy in candies:
            if candy > max:
                max = candy 
        # now add extra candies to see if this exceeds the greatest one (max) 
        for candy in candies:
            candy += extraCandies 
            if candy >= max:
                result.append(True)
            else:
                result.append(False)
        return result

    