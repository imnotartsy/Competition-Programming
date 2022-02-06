# top-interview-questions-easy/92/array/72
# 7/11/2021 13:07	Accepted	228 ms	15.8 MB	python3

class Solution(object):

    # def __init__():
    #     print('__init__ is the constructor for a class')
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        lastnew = 0

        if len(nums) == 0:
            return 0

        for i in range(1, len(nums)):
            print("Index:", i, "\tElement", nums[i], end='')
            if nums[i] != nums[lastnew]:
                print("\tNew Element!\tCount:", lastnew)
                lastnew +=1
                nums[lastnew] = nums[i]
                
            else:
                print("\tDuplicate Element!")
                
        nums = nums[0:lastnew+1]
        print(nums)    
        return lastnew + 1