class Solution:
    def isPalindrome(self, x: int) -> bool:
        if pow(-2, 31) <= x <= pow(2, 31) - 1:
            if x < 0:
                return False
            else:
                old_num = 0
                store = x
                while x != 0:
                    digit = x % 10
                    old_num = old_num * 10 + digit
                    x = x // 10
                return old_num == store
        else:
            return False