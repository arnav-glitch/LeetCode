class Solution:
    def reverse(self, x: int) -> int:
        sign = -1
        old_num = 0
        if x < 0:
            x = x * sign
            while x != 0:
                digit = x % 10
                new_num = old_num * 10 + digit
                old_num = new_num
                x = x // 10
            if pow(-2, 31) <= old_num * sign <= pow(2, 31) - 1:
                return old_num * sign
            else:
                return 0
        else:
            while x != 0:
                digit = x % 10
                new_num = old_num * 10 + digit
                old_num = new_num
                x = x // 10
            if pow(-2, 31) <= old_num <= pow(2, 31) - 1:
                return old_num
            else:
                return 0