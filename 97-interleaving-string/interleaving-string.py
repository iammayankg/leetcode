class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        N1 = len(s1)
        N2 = len(s2)
        N3 = len(s3)

        @cache
        def recurse(l1, l2, l3):
            # if l1 == N1 and l2 == N2 and l3 == N3:
            #     return True
            if l1 == N1:
                return s2[l2:] == s3[l3:]
            if l2 == N2:
                return s1[l1:] == s3[l3:]
            
            res = False
            if s1[l1] == s3[l3]:
                res |= recurse(l1+1, l2, l3+1)
            if s2[l2] == s3[l3]:
                res |= recurse(l1, l2+1, l3+1)
            return res

        if N1 + N2 != N3:
            # print("early")
            return False
        return recurse(0, 0, 0)        