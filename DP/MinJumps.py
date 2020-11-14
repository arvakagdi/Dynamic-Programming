'''
 Given an array of positive integers, find min jumps you will need to reach end of array.

 Every integer represents how many steps you can take.

 Ex:
 Array = [3,4,1,2,2,7,1,1,1,3]

 At index 0, we have 3 - i.e we can either go to index 1,2,or 3.

 Ans: 3 ( 3->4->7->3)
 '''

# Method 1: Time:O(N^2)  | Space: O(N)

def minNumberOfJumps1(array):
    jumps = [float("inf") for _ in range(len(array))]
    jumps[0] = 0   # 0 jumps to reach 0 from 0 ---- base case

    for i in range(1,len(array)):
        for j in range(0,i):
            if array[j] + j >= i:
                jumps[i] = min(jumps[i], jumps[j] + 1)

    return jumps[-1]



# Method 2: Time:O(N)  | Space: O(1)

def minNumberOfJumps2(array):
    maxReach = array[0]
    steps = array[0]
    jumps = 0

    for i in range(1, len(array)):
        if i == len(array) - 1:
            return jumps + 1
        
        maxReach = max(maxReach, array[i] + i)
        steps -= 1
        
        if steps == 0:
            jumps += 1    # if steps == 0, we finish reach for 1 integer and took a jump
            steps = maxReach - i    # update new steps, which is macReach - curr i
    return jumps



# Method 2: Time:O(N)  | Space: O(1)

def minNumberOfJumps3(array):
    maxReach = array[0]
    steps = array[0]
    jumps = 0

    if len(array) == 1:     # return 0 if only 1 elem in array
        return 0

    for i in range(1, len(array) - 1):		# iterate from 1 to one index less then last
        maxReach = max(maxReach, array[i] + i)
        steps -= 1    # one step near to maxReach
        
        if steps == 0:
            jumps += 1    # if steps == 0, we finish reach for 1 integer and took a jump
            steps = maxReach - i    # update new steps, which is macReach - curr i

    return jumps + 1   # at last index return jump + 1, 1 for the last jump
            

			
Array = [3,4,1,2,2,7,1,1,1,3]
print(minNumberOfJumps1(Array))