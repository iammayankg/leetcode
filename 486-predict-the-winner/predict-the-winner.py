class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        total = sum(nums)

        @cache
        def dp(start_index, end_index):
            if start_index > end_index:
                return 0
            #take start
            from_start = nums[start_index] - dp(start_index + 1, end_index)
            #take end
            from_end = nums[end_index] - dp(start_index, end_index - 1)
            #return max
            return max(from_start, from_end)

        player_1 = dp(0, len(nums)-1)
        # player_2 = total - player_1
        return player_1 >= 0
        