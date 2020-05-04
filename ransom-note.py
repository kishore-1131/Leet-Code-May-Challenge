class Solution:
    def canConstruct(self, sub: str, string: str) -> bool:
        dic = {}
        dic1 = {}
        count = 0
        for ch in string:
            dic[ch] = string.count(ch)
        for ele in sub:
            dic1[ele] = sub.count(ele)
        for key in dic1.keys():
            if key in dic.keys():
                if dic1[key] <= dic[key]:
                    count = count + 1
        if count < len(set(sub)):
            return False
        else:
            return True