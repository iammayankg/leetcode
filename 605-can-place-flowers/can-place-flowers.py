class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        N = len(flowerbed)
        def canPlace(idx):
            canPlace = True
            if idx < N-1:
                canPlace = False if flowerbed[idx+1] == 1 else canPlace
            if idx > 0:
                canPlace = False if flowerbed[idx-1] == 1 else canPlace
            return canPlace

        for idx, flower in enumerate(flowerbed):
            if flower == 0 and n > 0 and canPlace(idx):
                n -= 1
                flowerbed[idx] = 1
        return n == 0

        