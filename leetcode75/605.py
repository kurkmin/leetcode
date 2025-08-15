class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                cnt += 1
            return cnt >= n

        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    cnt += 1
                    flowerbed[i] = 1 
            elif i == len(flowerbed) - 1:
                if flowerbed[i-1] == 0 and flowerbed[i] == 0 :
                    cnt += 1
                    flowerbed[i] = 1 
            else:
                if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    cnt += 1 
                    flowerbed[i] = 1 
        if cnt >= n:
            return True
        else:
            return False

