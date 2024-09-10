# Solution

# // Time Complexity :  O(2N) -> Worst case when none of the values have higher value till the last element
# // Space Complexity : O(N)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

# // Your code here along with comments explaining your approach
# Monotonic Stack to maintain entries in ascending order and keep checking new entries
# or indexes while going through loop
# https://www.youtube.com/watch?v=Es_eNOlpqEQ

from collections import deque

def dailyTemperatures(temperatures):
    n = len(temperatures)
    queue = deque()
    result = [0]*n

    for i in range(0,n):
        if len(queue) > 0:
            if temperatures[i] > temperatures[queue[-1]]:
                while len(queue) > 0 and temperatures[i] > temperatures[queue[-1]]:
                    tempIdx = queue.pop()
                    result[tempIdx] = i - tempIdx
        
        queue.append(i)
    
    return result

if __name__ == "__main__":
    temperatures = [73,74,75,71,69,72,76,73]
    print(dailyTemperatures(temperatures))