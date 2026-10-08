class Solution:
    def isValid(self, s: str) -> bool:
        
        p_dict = {'(':')','[':']','{':'}',
                ')':'None',']':'None','}':'None'}

        stack = []

        for char in s:
            if len(stack) >= 1:
                if char != p_dict[stack[-1]]:
                    stack.append(char)
                elif char == p_dict[stack[-1]]:
                    stack.pop()
            else:
                stack.append(char)

        if len(stack) == 0:
            return True
        else:
            return False