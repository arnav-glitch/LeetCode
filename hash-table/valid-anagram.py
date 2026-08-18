from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = Counter(t)
        counter2 = Counter(s)
        for i in s:
            if i not in counter1:
                return False
            if i not in counter2:
                return False
        return True