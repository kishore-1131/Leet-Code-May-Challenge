class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        lst  = list(J)
        for ch in S:
            if ch in lst:
                count = count +1
        return count        
            