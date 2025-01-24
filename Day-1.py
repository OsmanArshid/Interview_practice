# Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.
# Note: The second largest element should not be equal to the largest element.

# Examples:

# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.

# Input: arr[] = [10, 5, 10]
# Output: 5
# Explanation: The largest element of the array is 10 and the second largest element is 5.

# Input: arr[] = [10, 10, 10]
# Output: -1
# Explanation: The largest element of the array is 10 and the second largest element does not exist.


# Constraints:
# 2 ≤ arr.size() ≤ 105
# 1 ≤ arr[i] ≤ 105

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#User function Template for python3
class Solution:
    
    # 19 mins
    #first approach
    # O(nlogn) time and O(1) space
    def getSecondLargest(self, arr):
        
        if not arr:
            return -1
            
        # if you want to sort, then alwasy call the method of the input
        arr.sort() # sorting takes O(nlogn) time
        # this is in-place sorting
        
        
        first_pointer = len(arr) - 1
        # print (first_pointer)
        second_pointer = len(arr) - 1
        
        
        while arr[second_pointer] == arr[first_pointer]:
            second_pointer -= 1
            
            if second_pointer == -1:
                return -1
        
        return arr[second_pointer]
    

    # 35mins
    #second approach ------- (BETTER APPROACH)
    # O(n) time and O(1) space
    def getSecondLargest(self, arr):
        #print(arr)
        
        if not arr:
            return -1
            
        first_pointer = 0
        second_pointer = 1
        small, large = 0,0
        
        
        while second_pointer <= len(arr) -1:
            
            if (arr[second_pointer] > arr[first_pointer]):
                
                if (large < arr[second_pointer]):
                    
                    if (large != 0):
                        small = large
                    
                    else:
                        small = arr[first_pointer]
                    
                    large = arr[second_pointer]
                    
                
                elif (large > arr[second_pointer]):
                    
                    if (small < arr[second_pointer]):
                        small = arr[second_pointer]
                        
            
            elif (arr[second_pointer] < arr[first_pointer]):
                
                if (small < arr[second_pointer]):
                    small = arr[second_pointer]
                
                if (large < arr[first_pointer]):
                    large = arr[first_pointer]

            first_pointer += 1
            second_pointer += 1

        
        if large == small:
            return -1
            
        return small

#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends