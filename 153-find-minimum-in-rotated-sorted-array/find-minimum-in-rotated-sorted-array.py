class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        low, high = 0, N-1
        if nums[high] > nums[low]:
            return nums[low]

        while low <= high:
            mid = (low+high)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] > nums[0]:
                low = mid + 1
            else:
                high = mid-1
        
