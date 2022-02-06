# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        node = head
        nums = []
        while node != None:
            nums.append(node)
            node = head.next
        n = len(nums)
        k %= n
        
        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                
                if start == current:
                    break
            start += 1

        # only for running tests
        return head

import LC646array


def main():
	inputs = {
		"p0": [[1], 0, [1]],
		"p0-1": [[1], 1, [1]],
		"p0-2": [[1, 2], 2, [1, 2]],
		"p0-3": [[1,2,3,4,5,6], 4, [3,4,5,6,1,2]],
		"p0-4": [[1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]],
		"p1": [[1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]],
        "p2": [[-1,-100,3,99], 2, [3,99,-1,-100]], 
		"p3": [[1, 2, 3, 4, 5, 6], 3, [4, 5, 6, 1, 2, 3]],
		"p4": [[1, 2, 3, 4, 5, 6], 2, [5, 6, 1, 2, 3, 4]] 

	}
	
	sol = LC646array.Solution()

	for input in inputs:
		print(input,":", end=' ')
		output = sol.rotate(inputs[input][0], inputs[input][1])
		print("\tInput:", inputs[input][0], inputs[input][1])
		print("\tOutput:", output)
		if output == inputs[input][2]:
			print("*** PASSED! ***")
		else:
			print("*** FAILED ***")
			print("\tExpected Output:", inputs[input][2])
		

main()