class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                return True
            count[nums[i]] = True            

        return False
        


def main():
	inputs = {
		"p0": [[1, 2, 3, 1], True],
        "p1": [[1, 2, 3, 4], False],
        "p2": [[1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True]
	}
	
	sol = Solution()

	for input in inputs:
		print(input,":", end=' ')
		output = sol.containsDuplicate(inputs[input][0])
		print("\tInput:", inputs[input][0])
		print("\tOutput:", output)
		if output == inputs[input][1]:
			print("*** PASSED! ***")
		else:
			print("*** FAILED ***")
			print("\tExpected Output:", inputs[input][1])
		

main()