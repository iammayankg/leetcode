class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = nums[0::2]
        odd = nums[1::2]
        even.sort()
        odd.sort(reverse=True)
        even_index = 0
        for i in range(0, len(nums), 2):
            nums[i] = even[even_index]
            even_index += 1
        odd_index = 0
        for i in range(1, len(nums), 2):
            nums[i] = odd[odd_index]
            odd_index += 1
        return nums