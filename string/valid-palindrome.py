class Solution:
    def isPalindrome(self, s: str) -> bool:
        myString = []
        for i in s:
            if i.isalnum():
                myString.append(i)
        left = 0
        right = len(myString) - 1
        while left < right:
            if myString[left].lower() != myString[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True