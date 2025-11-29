class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        N = len(arr)
        oddPossible = [False] * N
        evenPossible = [False] * N
        oddPossible[N-1] = True
        evenPossible[N-1] = True

        def createBitMask(indices):
            res = [None] * N
            stack = []
            for i in indices:
                while stack and stack[-1] < i:
                    res[stack.pop()] = i
                stack.append(i)
            return res

        B = sorted(range(N), key=lambda i: arr[i])
        oddNext = createBitMask(B)

        B = sorted(range(N), key=lambda i: -arr[i])
        evenNext = createBitMask(B)

        for i in range(N-2, -1, -1):
            ai = arr[i]
            # min_j = sorted([(arr[j], j) for j in range(i+1, N) if arr[j] >= ai] + [(math.inf, -1)])
            # min_j = [x for x in min_j if x[0] == min_j[0][0]]
            # if min_j[0][1] != -1:
            #     oddPossible[i] = evenPossible[min_j[0][1]]
            if oddNext[i] is not None:
                oddPossible[i] = evenPossible[oddNext[i]]

            # max_j = sorted([(arr[j], j) for j in range(i+1, N) if arr[j] <= ai] + [(-math.inf, -1)], reverse=True)
            # max_j = [x for x in max_j if x[0] == max_j[0][0]]
            # if max_j[0][1] != -1:
            #     evenPossible[i] = oddPossible[max_j[-1][1]]
            if evenNext[i] is not None:
                evenPossible[i] = oddPossible[evenNext[i]]

        return sum(oddPossible)
        