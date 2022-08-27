# Program to implement Linear Search using Python:
# Time complexity : O(n)
# Space complexity : O(n)
class Solution:
    def __init__ (self):
        pass
    # Function for Linear Search
    def LinearSearch(self, arr: list, target : int):
        for i in arr:
            if target == i:
                return True

        return False
        
if __name__ == '__main__':
    oS = Solution()
    arr = [12,43,54,123,76,8,4,-1]
    if (oS.LinearSearch(arr, -1)):
        print("Element found in array")
    else:
        print("Element not Found")