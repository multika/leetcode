class Solution:
    def isValid(self, s: str) -> bool:
        matching_brackets = {
            ')': '(',
            '}':'{',
            ']':'['
              
        }
        
        stack = list()
        
        for bracket in s:
            if stack and matching_brackets.get(bracket) == stack[-1]:
                stack.pop()
            else:
                stack.append(bracket)
        return stack == []
