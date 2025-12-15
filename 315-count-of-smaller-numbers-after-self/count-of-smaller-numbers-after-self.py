class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        N = len(nums)
        arr = [[num, idx] for idx, num in enumerate(nums)]
        result = [0] * N

        def mergeSort(series, left, right):
            if left >= right:
                return
            mid = (left+right)//2
            mergeSort(series, left, mid)
            mergeSort(series, mid+1, right)
            merge(series, left, right, mid)

        def merge(series, left, right, mid):
            temp = []
            lo = left
            hi = mid + 1
            while lo <= mid and hi <= right:
                if series[lo][0] <= series[hi][0]:
                    result[series[lo][1]] += hi - mid-1
                    temp.append(series[lo])
                    lo += 1
                else:
                    temp.append(series[hi])
                    hi += 1
            
            while lo <= mid:
                result[series[lo][1]] += hi - mid-1
                temp.append(series[lo])
                lo += 1
            while hi <= right:
                temp.append(series[hi])
                hi += 1

            for i in range(left, right + 1):
                series[i] = temp[i-left]
        
        mergeSort(arr, 0, N-1)
        return result
                