'''
Dynamic Programming:

Given a target value and an array of coin denominations, find minimum number of coins required to get the 
target amount. If we can't have target amount from the given denominations, return -1

Ex: [1,2,4], amount - 6
Ans: 2 (2 + 4 = 6)

Ex: [3,5] amount - 7
Ans: -1


Time: O(Nd) where N is the target amount, d is the denomination array size
Space: O(N) as we create an array of len target amount + 1
'''

def minNumberOfCoinsForChange(n, denoms):
    nums = [float("inf") for _ in range(n+1)]  # set all num to inf to update later
    nums[0] = 0		# set base case to 0, we need 0 change to get 0$

    for denom in denoms:	# Iterate through the denominations
        for amount in range(len(nums)):  # Iterate through the array of nums
            if denom <= amount:	
                nums[amount] = min(nums[amount], 1 + nums[amount - denom] ) # update target if it less than prev updated value
    return nums[n] if nums[n] != float("inf") else -1