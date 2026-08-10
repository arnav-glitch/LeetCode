class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            product = 1
            temp = n
            while temp != 0:
                digit = temp % 10
                temp = temp // 10
                product *= digit
            if product % t == 0:
                return n
            else:
                n += 1