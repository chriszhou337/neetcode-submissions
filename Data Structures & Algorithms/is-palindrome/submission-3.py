class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1

        while L < R:
            while L < R and s[L].isalnum() == False:
                L += 1
            while L < R and s[R].isalnum() == False:
                R -= 1

            print("Compared letter")
            print(s[L])
            print(s[R])

            if s[L].lower() != s[R].lower():
                print("False")
                return False
            
            L += 1
            R -= 1

        return True