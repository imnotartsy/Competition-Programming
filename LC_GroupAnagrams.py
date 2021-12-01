#  https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        print(strs)
        ret_dict = {}
        for s in strs:
            s_string = "".join(sorted(s))
            if s_string in ret_dict:
                ret_dict[s_string].append(s)
            else:
                ret_dict[s_string]= [s]

        ret = []
        for k, v in ret_dict.items():
            ret.append(v)

        return ret

def main():
    inputs = {
        "p0": [["eat","tea","tan","ate","nat","bat"],  [["bat"],["nat","tan"],["ate","eat","tea"]]],
        "p1": [[""], [[""]]],
        "p2": [["a"], [["a"]]]
    }
    
    sol = Solution()

    for input in inputs:
        print(input,":", end=' ')
        output = sol.groupAnagrams(inputs[input][0])
        print("\tInput:", inputs[input][0])
        print("\tOutput:", output)
        if output == inputs[input][1]:
            print("*** PASSED! ***")
        else:
            print("*** FAILED ***")
            print("\tExpected Output:", inputs[input][1])

        print()
        

main()