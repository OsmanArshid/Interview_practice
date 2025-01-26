# You are given an array of integers arr[]. Your task is to reverse the given array.
# Note: Modify the array in place.


# Examples:
# Input: arr = [1, 4, 3, 2, 6, 5]
# Output: [5, 6, 2, 3, 4, 1]
# Explanation: The elements of the array are 1 4 3 2 6 5. After reversing the array, the first element goes to the last position, the second element goes to the second last position and so on. Hence, the answer is 5 6 2 3 4 1.

# Input: arr = [4, 5, 2]
# Output: [2, 5, 4]
# Explanation: The elements of the array are 4 5 2. The reversed array will be 2 5 4.

# Input: arr = [1]
# Output: [1]
# Explanation: The array has only single element, hence the reversed array is same as the original.


# Constraints:
# 1<=arr.size()<=105
# 0<=arr[i]<=105

#--------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
# User function Template for python3
class Solution:

    # easy
    # O(n) --- Time complexity
    # O(1) --- Space complexity
    # 9mins (COULD HAVE DONE WAYYYYYYYYY BETTER)
    def reverseArray(self, arr):
        if not arr:
            return 
        
        if len(arr) == 1:
            return arr
            
        fir_pointer = 0
        sec_pointer = len(arr) - 1
        
        while fir_pointer <= sec_pointer:
            arr[fir_pointer], arr[sec_pointer] = arr[sec_pointer], arr[fir_pointer]
            fir_pointer +=1
            sec_pointer -=1
        
        # print (sec_pointer)
        # print (fir_pointer)
        return arr


        # Apparently, there's an inbuilt method to reverse an array and it is also super 
        # efficient with O(n) time complexity and O(1) space complexity
        arr.reverse()

#{ 
 # Driver Code Starts
import sys
def main():
    # Read the number of test cases
    tc = int(sys.stdin.readline())
    while tc > 0:
        # Read the array elements as a string
        str_arr = sys.stdin.readline().split()
        # Convert the string array to an integer array
        arr = [int(x) for x in str_arr]
        # Create a Solution object
        obj = Solution()
        # Reverse the array
        obj.reverseArray(arr)
        # Print the reversed array
        for i in range(0, len(arr)):
            print(arr[i], end=" ")
        print()
        print("~")
        # Decrement the test case count
        tc -= 1

if __name__ == "__main__":
    main()
# } Driver Code Ends