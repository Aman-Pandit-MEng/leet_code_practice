class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] ==0:
                for j in range(len(nums)-1,i-1,-1):
                    if nums[j] != 0:
                        nums[j] , nums[i] = nums[i] , nums[j]
          
                
            


        