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
		

	# inputs = {
	# 	"p1": [[7,1,5,3,6,4], 7],
    #     "p2": [[1,2,3,4,5], 4], 
	# 	"p3": [[7,6,4,3,1], 0]
	# }
	
	# sol = LC564array.Solution()

	# for input in inputs:
	# 	print(input,":", end=' ')
	# 	output = sol.maxProfit(inputs[input][0])
	# 	if output == inputs[input][1]:
	# 		print("*** PASSED! ***")
	# 	else:
	# 		print("*** FAILED ***")
	# 	print("\tInput:", inputs[input][0])
	# 	print("\tOutput:", output)
		


if __name__ == '__main__':
	main()