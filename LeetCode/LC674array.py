class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        if len(nums1) < len(nums2):
            long = nums1
            short = nums2
        else:
            long = nums2
            short = nums1

        ret = []

        for i in range(len(long)):
            for j in range(i, len(short)):
                if long[i] == short[j]:
                    ret.append(long[i])
                    break

        return ret

def main():
    inputs = {
        "p0": [[1,2,2,1], [2,2], [2, 2]],
        "p1": [[4,9,5], [9,4,9,8,4], [4,9]],
        "p2": [[2, 1], [1, 1], [1]],
        "p3": [[1, 1], [2, 1], [1]]
    }
    
    sol = Solution()

    for input in inputs:
        print(input,":", end=' ')
        output = sol.intersect(inputs[input][0], inputs[input][1])
        print("\tInput:", inputs[input][0], inputs[input][1])
        print("\tOutput:", output)
        if output == inputs[input][2]:
            print("*** PASSED! ***")
        else:
            print("*** FAILED ***")
            print("\tExpected Output:", inputs[input][2])

        print()
        

main()