class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            c=0
            for j in range(len(nums)):
                if nums[i] == nums[j] and i != j:
                    c=c+1
            if c == 0:
                sum = sum + nums[i]
        return sum
