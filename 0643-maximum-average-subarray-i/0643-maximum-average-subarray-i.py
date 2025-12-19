class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_max = sum_i = sum(nums[0:k])
        for i in range(1, len(nums)-k+1):
            #avg = sum(nums[i:k+i])/k
            sum_i = sum_i - nums[i-1] + nums[k+i-1]
            if sum_max < sum_i:
                sum_max = sum_i
        return sum_max/k
