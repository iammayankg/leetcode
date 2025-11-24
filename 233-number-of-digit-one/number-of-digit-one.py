class Solution:
    def countDigitOne(self, n: int) -> int:
        """
        1-9 => 1
        10-19 => 9 + 1
        """ 
        ns = str(n)
        @cache
        def digitDP(index, tight, one_count):
            if index == len(ns):
                return one_count
            high = int(ns[index]) if tight else 9
            count = 0
            for i in range(high + 1):
                new_tight = i == int(ns[index]) and tight
                count += digitDP(index + 1, new_tight, one_count + (1 if i == 1 else 0))
                # if i == 1:
                #     count += 1
            return count
        return digitDP(0, True,0)


            

        