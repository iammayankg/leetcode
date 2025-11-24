class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        top, remainder = SortedList(), SortedList()
        frequency = Counter()
        N = len(nums)
        results = []
        currSum = 0

        def rebalance():
            nonlocal x
            nonlocal currSum
            # print(f"Before rebalance: remainder={remainder} top={top}")
            if top and (remainder[-1][0] > top[0][0] or (remainder[-1][0] == top[0][0] and remainder[-1][1] > top[0][1])):
                f1, n1 = top.pop(0)
                currSum -= f1*n1
                f2, n2 = remainder.pop(-1)
                currSum += f2*n2
                top.add((f2, n2))
                remainder.add((f1, n1))
            
            if len(top) < x and remainder:
                f2, n2 = remainder.pop(-1)
                currSum += f2*n2
                top.add((f2, n2))
            # print(f"After rebalance: remainder={remainder} top={top}")

        def add(num):
            nonlocal currSum
            if num in frequency and frequency[num]:
                prevFreq = frequency[num]
                if (prevFreq, num) in top:
                    top.remove((prevFreq, num))
                    currSum -= num * prevFreq
                else:
                    remainder.remove((prevFreq, num))
                
                # frequency[num] -= 1
                # if frequency[num] == 0:
                #     del frequency[num]
            # print(f"***** add={num} *******")
            frequency[num] += 1
            remainder.add((frequency[num], num))
            rebalance()
            pass

        def remove(num):
            nonlocal currSum
            if num in frequency and frequency[num]:
                prevFreq = frequency[num]
                if (prevFreq, num) in top:
                    top.remove((prevFreq, num))
                    currSum -= num * prevFreq
                else:
                    remainder.remove((prevFreq, num))
                # currSum -= num * prevFreq
                # frequency[num] -= 1
                # if frequency[num] == 0:
                #     del frequency[num]
            # print(f"***** remove={num} *******")
            frequency[num] -= 1
            remainder.add((frequency[num], num))
            rebalance()

        for num in nums[:k]:
            add(num)
            # print(f"currSum={currSum}")
        results.append(currSum)

        for idx in range(k, N):
            # print("*"*20)
            remove(nums[idx-k])
            add(nums[idx])
            # print(f"currSum={currSum}")
            results.append(currSum)
        return results
        