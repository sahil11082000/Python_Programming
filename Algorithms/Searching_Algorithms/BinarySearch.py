# Program to Implement Binary Search Algorithm in python:
# Time complexity : O(log(n))
# Space Complexity : O(n)
class Solution:
    def __init__ (self):
        pass
    # Logic for Binary Search 
    def BinarySearch(self, arr: list, target : int):
        first, last = 0, (len(arr) - 1)
        # Base condition
        if first > last:
            return False

        else:
            mid = (first + last) // 2
            if arr[mid] == target: # if target == middle element of array, then we return true
                return True
            elif arr[mid] > target: # if target < middle element, then we call the BinarySearch() function for element (0 - (mid-1))
                last = mid  - 1
                return self.BinarySearch(arr[:last+1], target)
            else: #3rd case: if target > middle element, than we call the BinarySearch() function for element ((mid + 1), last)
                first = mid + 1
                return self.BinarySearch(arr[first:], target)


if __name__ == '__main__':
    oS = Solution()
    arr = [1, 6, 8, 9 ,2 ,4]
    arr = sorted(arr, reverse=False)
    print(oS.BinarySearch(arr, 6))
    print(oS.BinarySearch(arr, 2))
    print(oS.BinarySearch(arr, 10))


# Sahil Tomar