class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    
    # reminded about how this can be solved using slicing 
    
    # a[start:stop]  # items start through ((((((stop-1))))))
    # a[start:]      # items start through the rest of the array
    # a[:stop]       # items from the beginning through (((((((stop-1)))))))
    # a[:]           # a copy of the whole array   
    
    # a[start:stop:step] # start through not past stop, by step
    
    # a[-1]    # last item in the array
    # a[-2:]   # last two items in the array
    # a[:-2]   # everything except the last two items
    def rotateArr(self, arr, d):
        # 3rd Approach
        # O(n) --- Time complexity as slicing only goes thru the array once
        # O(1) --- Space complexity because it is in place
        if not arr:
            return
        
        if d == 0:
            return
        
        n = len(arr) 
        # this step because rotating d times = rotating d % length times
        # e.g., If d = 7, rotating 7 times is the same as rotating 7 % 5 = 2 times
        d = d % n
        
        arr[:] = arr[d:] + arr[:d]
        
        return arr
            

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
        
        # 2nd Approach
        # 12 mins
        # O(n^2) -- Time Complexity
        # O(1) -- Space Complexity
        
        # if not arr:
        #     return
        
        # if d == 0:
        #     return
    
        # d_approach = 0
        # temp = -1
        
        # while d_approach < d:
        #     temp = arr.pop(0)
        #     arr.append(temp)
        #     d_approach += 1
        
        # return arr
        
        # if you want to remove and return something from the list at any index, you use 
        # arr.pop(index) --- THIS HAS A TIME COMPLEXITY OF O(n) 
        
        # or by Default 
        # arr.pop() for last element --- THIS HAS A TIME COMPLEXITY OF O(1)
        
        
        # to put back, u use 
        # insert, append, 
        # to append 2 lists together, you use "extend()" method
        
# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------

        # 1st Approach
        # 23 mins
        # O(n^2) -- Time Complexity
        # O(1) --- Space Complexity
        
        # if not arr:
        #     return
        
        # if d == 0:
        #     return
        
        # # counter = 0
        # temp = -1
        # d_approach = 0
        
        # while d_approach < d:
            
        #     temp=arr[0]

        #     for counter in range(len(arr) - 1):
        #         arr[counter]=arr[counter + 1]
                
        #     arr[len(arr) - 1]=temp

        #     d_approach += 1
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math
def main():
    T = int(input())

    while (T > 0):
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ob.rotateArr(A, D)

        for i in A:
            print(i, end=" ")

        print()

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends