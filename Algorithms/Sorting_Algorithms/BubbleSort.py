"""
Bubble Sort Algorithm: This the one the simplest and easy to implement sorting algorithm.
Time Complexity : O(N^2)
Space Complexity : O(N)
"""
class Solution:
    def __init__(self):
        pass

    def bubbleSort(self, arr : list):
        for i in range(0, len(arr) - 1): #for controlling the pass
            for j in range(0, len(arr) - 1 - i): # for swapping the numbers if unsorted elements found
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    
    # function to display the result
    def display(self, arr: list):
        print("---------------------------------")
        for i in range(len(arr)):
            print(arr[i], end = " | ")
        print("\n---------------------------------")


# Driver Code
def main():
    arr = [1, 9, 12, 18, 25, 0]
    oSolution = Solution()
    print("Given Array : \n")
    oSolution.display(arr)
    print("\nAfter Sorting of Array: \n")
    oSolution.bubbleSort(arr)
    oSolution.display(arr)




if __name__ == '__main__':
    main()