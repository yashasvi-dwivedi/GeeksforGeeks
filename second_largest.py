class Solution:
    def getSecondLargest(self, arr):
        if len(arr) < 2:
            return -1

        largest = -1
        second_largest = -1

        for i in arr:
            if i > largest:
                second_largest = largest
                largest = i
            elif i < largest and i > second_largest:
                second_largest = i

        return second_largest


# Test cases
if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 5]
    print(sol.getSecondLargest(arr))  # Output: 4
    arr = [5, 5, 5]
    print(sol.getSecondLargest(arr))  # Output: -1
    arr = [1]
    print(sol.getSecondLargest(arr))  # Output: -1
    arr = []
    print(sol.getSecondLargest(arr))  # Output: -1
