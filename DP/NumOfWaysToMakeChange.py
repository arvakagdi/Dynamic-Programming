'''
Given an array for positive number which are coin denominations and a target amount to achieve from given denominations
Return number of ways target amount can be achieved

Time: O(Nd) where n is the target amount as we make ways araay of size n + 1, d is size of coin denominations
Space: O(N), N = target number
'''

def numberOfWaysToMakeChange(n, denoms):
	ways = [0 for amount in range(n+1)]
	ways[0] = 1   # as we have only one way to have 0 (base case)
	
	for denom in denoms:			 # iterate through denominations
		# can also write for amount in range(1,len(ways)):
		for amount in range(1,n+1):  # for each deno, iterate through ways array and update it
			if denom <= amount:		 # if deno is <= amount  
				ways[amount] += ways[amount - denom]
	return ways[n]


print(numberOfWaysToMakeChange(6, [1, 5]))