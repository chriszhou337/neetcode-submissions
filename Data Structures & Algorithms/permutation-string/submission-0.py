class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        charCount_s1 = {}
        
        for i in range (len(s1)):
            charCount_s1[s1[i]] = charCount_s1.get(s1[i], 0) + 1

        L = 0
        charCount_s2 = {}

        for R in range (len(s2)):
            charCount_s2[s2[R]] = charCount_s2.get(s2[R], 0) + 1

            windowLen = R - L + 1

            if windowLen < len(s1):
                continue
            
            if charCount_s1 == {k: v for k, v in charCount_s2.items() if v > 0}:
                return True

            if charCount_s2[s2[L]] > 0:
                charCount_s2[s2[L]] -= 1

            L+= 1
                

        return False
