class Solution:
    def bestClosingTime(self, customers: str) -> int:
        inCustomers = customers.count("Y")
        outCustomers = 0 # customers.count("N")
        N = len(customers)

        minCost = math.inf
        minHour = -1

        for i in range(N+1):
            currPenalty = outCustomers + inCustomers
            if currPenalty < minCost:
                minCost = currPenalty
                minHour = i
            if i != N:
                if customers[i] == "Y":
                    inCustomers -= 1
                else:
                    outCustomers += 1
        return minHour
