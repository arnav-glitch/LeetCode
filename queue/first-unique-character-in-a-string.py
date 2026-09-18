class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_map = {}
        for i in s:
            char_map[i] = char_map.get(i, 0) + 1
        ans = None
        for key, value in char_map.items():
            if value == 1:
                ans = key
                break
        if ans == None:
            return -1
        for i in range(len(s)):
            if s[i] == ans:
                return i