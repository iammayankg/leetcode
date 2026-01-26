class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_difference = math.inf
        c = collections.Counter()
        # c[arr[0]] = 1
        for i in range(1, len(arr)):
            min_difference = min(min_difference, arr[i]-arr[i-1])
            # c[arr[i]] += 1

        
        pairs = []
        for num in arr:
            if num - min_difference in c:
                pairs.append([num-min_difference, num])
            c[num] += 1
        return pairs