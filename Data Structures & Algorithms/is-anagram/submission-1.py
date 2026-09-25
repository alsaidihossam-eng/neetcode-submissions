class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        char_dict_s = {char:0 for char in s}
        char_dict_t = {char:0 for char in s}

        for char in s:
            if char in char_dict_s:
                char_dict_s[char] += 1

        for char in t:
            if char in char_dict_t:
                char_dict_t[char] += 1

        if char_dict_t == char_dict_s and len(s) == len(t):
            return True

        return False