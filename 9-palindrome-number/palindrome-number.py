class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]

        # s =str(x)
        # return s == s[::-1]

        # rev = 0
        # num = x

        # while num != 0:
        #     rev = rev * 10 + num % 10
        #     num = num // 10

        # return rev == x

        # if x < 0 or (x % 10 == 0 and x != 0):
        #     return False
        
        # reversed_half = 0
        # while x > reversed_half:
        #     reversed_half = reversed_half * 10 + x % 10
        #     x //= 10
        
        # return x == reversed_half or x == reversed_half // 10

        