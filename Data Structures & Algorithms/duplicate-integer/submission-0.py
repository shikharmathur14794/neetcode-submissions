class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        st=False
        for i in range(0, len(nums)):
            if nums[i] in nums[i+1:] and i!=len(nums)-1:
                st= True
                break
            else:
                st= False
        return st



        