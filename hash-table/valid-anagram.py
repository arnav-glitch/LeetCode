class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        for ch in s:
            s_map[ch] = s_map.get(ch, 0) + 1
        t_map = {}
        for ch in t:
            t_map[ch] = t_map.get(ch, 0) + 1
        for key, value in t_map.items():
            if key not in s_map:
                return False
            else:
                s_value = s_map.get(key, 0)
                t_value = t_map.get(key, 0)
                if s_value != t_value:
                    return False
        return True