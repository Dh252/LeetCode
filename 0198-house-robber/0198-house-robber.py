class Solution:
    def rob(self, nums: list[int]) -> int:
        a=0
        b=0
        for num in nums:
            c=max(a+num,b)
            a=b
            b=c
        return b
        