# 27. Remove Element: https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        front = 0
        for i in range(len(nums)):
            if nums[i] != val:
                temp = nums[i]
                nums[front] = nums[i]
                nums[i] = temp
                front += 1
                
        return front