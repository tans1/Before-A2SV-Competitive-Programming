class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j +1], nums[j]
        output = []
        i = 0
        while i < len(nums):
            if nums[i] == target:
                output.append(i)
            i +=1
        return output
