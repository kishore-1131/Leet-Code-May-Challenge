class Solution:
    def firstUniqChar(self, s: str) -> int:
        for ch in s:
            if ch not in s[s.index(ch) + 1:]:
                return s.index(ch)
                break
            else:
                continue
        else:
            return -1
