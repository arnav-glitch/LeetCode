class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}
        if len(s) != len(t):
            return False
        for i in s:
            hm[i] = hm.get(i, 0) + 1
        for i in t:
            if i not in hm:
                return False
            else:
                hm[i] -= 1
        for items in hm:
            if hm[items] != 0:
                return False
        return True