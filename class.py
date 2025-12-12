def rec(n,memo={}):
    if n in memo:
        return memo[n]
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    memo[n] = rec(n-1) + rec(n-2)
    return memo[n]

print(rec(7))