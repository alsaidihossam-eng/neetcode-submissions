class Solution:
    def isPalindrome(self, s: str) -> bool:
        ascii = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        ascii_dict = {char:0 for char in ascii}
        s_reversed = ''
        s_check = ''

        for char in s:
            if char in ascii_dict:
                s_check += char

        for i in range(1, (len(s) + 1), 1):
            if s[i*-1] in ascii_dict:
                s_reversed += s[i*-1]

        if s_check.lower() == s_reversed.lower():
            return True

        return False