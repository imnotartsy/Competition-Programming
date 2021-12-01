def LucasNumber(n):
    memo = {}
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        memo[n] = LucasNumber(n-1) + LucasNumber(n-2)
        return memo[n]

for i in range(12):
    print(LucasNumber(i))