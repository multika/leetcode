class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x%10 == 0 and x!= 0:
            return False
        return self.check_reverse(x)
    

    def check_reverse(self, x: int) -> int:
        number = x
        reverse = 0
        while (number>reverse):
            remainder = number%10
            reverse = (reverse*10) + remainder
            number = number//10
        
        if reverse == number:
            return True
        if reverse//10 == number:
            return True
