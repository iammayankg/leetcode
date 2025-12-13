class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        def isValidC(codeStr):
            if not codeStr:
                return False
            for ch in codeStr:
                if not ('A' <= ch.upper() <= "Z" or "0" <= ch <= "9") and ch != '_':
                    return False
            return True

        def isValidB(bStr):
            f = set(["electronics", "grocery", "pharmacy", "restaurant"])
            return bStr in f
        validCoupons = []
        for c, b, a in zip(code, businessLine, isActive):
            if isValidC(c) and isValidB(b) and a:
                validCoupons.append((c, b))

        bOrder = {
            "electronics": 1,
            "grocery": 2,
            "pharmacy": 3,
            "restaurant": 4
        }
        validCoupons.sort(key=lambda x: (bOrder[x[1]], x[0]))
        return [v[0] for v in validCoupons]

        
        