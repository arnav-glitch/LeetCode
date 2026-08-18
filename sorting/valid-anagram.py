from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = Counter(s)
        for i in t:
            if i not in counter:
                return False
        return True