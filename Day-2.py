# You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.


# Examples:
# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: [1, 2, 4, 3, 5, 0, 0, 0]
# Explanation: There are three 0s that are moved to the end.

# Input: arr[] = [10, 20, 30]
# Output: [10, 20, 30]
# Explanation: No change in array as there are no 0s.

# Input: arr[] = [0, 0]
# Output: [0, 0]
# Explanation: No change in array as there are all 0s.


# Constraints:
# 1 ≤ arr.size() ≤ 105
# 0 ≤ arr[i] ≤ 105

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------   
#User function Template for python3

class Solution:
	
    # easy
    # O(n) -- time complexity
	# O(1) -- space complexity
	# 45mins to solve (which is a lot of time)
	def pushZerosToEnd(self,arr):
        # print(arr)
         if not arr:
            return

         sec_pointer = 1
         first_pointer = 0

         # this was my approach, it is the best in terms of time and space complexity
         # but this type of approach takes too much time, so I should change my thinking 
         # and try to come up with logics that take less time
         while sec_pointer < len(arr):
            if arr[first_pointer] == 0 and arr[sec_pointer] != 0:
                arr[first_pointer], arr[sec_pointer] = arr[sec_pointer], arr[first_pointer]
                sec_pointer += 1
                first_pointer += 1

            elif arr[first_pointer] != 0:
                sec_pointer += 1
                first_pointer += 1
            
            if sec_pointer != len(arr):
                if arr[first_pointer] == 0 and arr[sec_pointer] == 0:
                    sec_pointer += 1
                
                    if sec_pointer != len(arr):
                        if arr[sec_pointer] != 0:
                            arr[first_pointer], arr[sec_pointer] = arr[sec_pointer], arr[first_pointer]
                            sec_pointer += 1
                            first_pointer += 1
                            
                        else:
                            sec_pointer +=1
            
            if sec_pointer != len(arr):
                if arr[first_pointer] != 0 and arr[sec_pointer] != 0:
                        sec_pointer += 1
                        first_pointer += 1

         return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
        print("~")
# } Driver Code Ends