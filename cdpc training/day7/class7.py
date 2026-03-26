
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
# Monk loves to preform different operations on arrays, and so being the principal of Hackerearth School, he assigned a task to his new student Mishki. Mishki will be provided with an integer array A of size N and an integer K , where she needs to rotate the array in the right direction by K steps and then print the resultant array. As she is new to the school, please help her to complete the task.
T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    K = K % N  
    

    result = A[-K:] + A[:-K]
    
    print(*result)
    #Given an array of integers, find the sum of its elements
    import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # Write your code here
    
    total = 0
    for i in ar:
        total += i
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
#Complete the function  to compute the sum of two integers.
def solveMeFirst(a,b):
    return a+b
    sum
	# Hint: Type return a+b below


num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)
