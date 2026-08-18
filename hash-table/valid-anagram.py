from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = Counter(t)
        for i in s:
            if i not in counter:
                return False
        return True