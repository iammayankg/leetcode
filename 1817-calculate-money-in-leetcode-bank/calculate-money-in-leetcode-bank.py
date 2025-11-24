class Solution:
    def totalMoney(self, n: int) -> int:
        def total(start, end):
            return (end*(end+1) - start*(start-1))//2
        money = 0
        quotient = n//7
        remainder = n%7
        for i in range(quotient):
            money += total(i+1, i+7)
        money += total(quotient+1, quotient+remainder)
        return money
        