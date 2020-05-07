class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        s = set(nums)
        for ele in s:
            dic[ele] = nums.count(ele)
        return (max(dic, key = dic.get))