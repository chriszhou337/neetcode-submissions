class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        res = 0
        char_frequency = {}
        replacements = 0

        for R in range (len(s)):
            char_frequency[s[R]] = char_frequency.get(s[R], 0) + 1
            max_freq_char = max(char_frequency, key = char_frequency.get)
            max_freq = max(char_frequency.values())

            while (R - L + 1) - max_freq > k:
                char_frequency[s[L]] -= 1
                L += 1

            res = max(res, R - L + 1)
        
        return res
        