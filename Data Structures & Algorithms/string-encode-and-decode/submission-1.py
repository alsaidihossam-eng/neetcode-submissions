class Solution:

    def encode(self, strs: List[str]) -> str:
       
        s = ''
        
        for word in strs:
            for char in word:
                    new_value = round((((ord(char) + 5) * 32) - 2) / 5)
                    s += chr(new_value)
            
            s +=  ' '
            
        return s

    def decode(self, s: str) -> List[str]:
        
        output = []
        real_word = ''
        
        for char in s:
            if char == ' ':
                output.append(real_word)
                real_word = ''
            else:
                real_value = round((((ord(char) * 5) + 2) / 32) - 5)
                real_word += chr(real_value)

        return output


