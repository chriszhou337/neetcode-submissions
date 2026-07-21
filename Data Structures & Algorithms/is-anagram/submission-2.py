class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap_s = {}
        hashMap_t = {}

        if len(s) != len(t):
            return False
        
        n = len(s)

        for i in range (n):
            if s[i] in hashMap_s:
                hashMap_s[s[i]] +=1
            else:
                hashMap_s[s[i]] = 1

            if t[i] in hashMap_t:
                hashMap_t[t[i]] += 1
            else:
                hashMap_t[t[i]] = 1
           
        return hashMap_s == hashMap_t

