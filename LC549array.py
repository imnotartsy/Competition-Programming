class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        stack = {}
        for i in range(len(nums)):
            if nums[i] in stack:
                del stack[nums[i]]
            else:
                stack[nums[i]] = True
        
        return list(stack.keys())[0]
        
        


def main():
	inputs = {
		"p0": [[2, 2, 1], 1],
        "p1": [[4, 1, 2, 1, 2], 4],
        "p2": [[1], 1]
	}
	
	sol = Solution()

	for input in inputs:
		print(input,":", end=' ')
		output = sol.singleNumber(inputs[input][0])
		print("\tInput:", inputs[input][0])
		print("\tOutput:", output)
		if output == inputs[input][1]:
			print("*** PASSED! ***")
		else:
			print("*** FAILED ***")
			print("\tExpected Output:", inputs[input][1])
		

main()