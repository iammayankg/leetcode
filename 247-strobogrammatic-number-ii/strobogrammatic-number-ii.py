class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        lookup = {
            "6":"9",
            "9": "6",
            "1":"1",
            "8":"8",
            "0": "0"
        }
        def recurse(num, isFinal):
            if num == 1:
                return ["0", "1", "8"]
            if num == 2:
                if isFinal:
                    return ["11","69","88","96"]
                else:
                    return ["11","69","88","96", "00"]

            res = recurse(num-2, False)
            res2 = []
            for l, r in lookup.items():
                if isFinal and l == "0":
                    continue
                for re in res:
                    res2.append(l + re + r)
            return res2
        return recurse(n, True)


        