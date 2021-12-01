class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0

        for i in range(0, len(prices)-1):
            if prices[i] < prices[i+1]:
                profit += prices[i+1] - prices[i]
    
        return profit

def main():
    inputs = {
        "p1": [[7,1,5,3,6,4], 7],
        "p2": [[1,2,3,4,5], 4], 
        "p3": [[7,6,4,3,1], 0]
    }

    sol = LC564array.Solution()

    for input in inputs:
        print(input,":", end=' ')
        output = sol.maxProfit(inputs[input][0])
        if output == inputs[input][1]:
            print("*** PASSED! ***")
        else:
            print("*** FAILED ***")
        print("\tInput:", inputs[input][0])
        print("\tOutput:", output)

main()