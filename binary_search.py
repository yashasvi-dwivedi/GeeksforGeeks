class Solution:
    def binarysearch(self, arr, k):
        left, right = 0, len(arr) - 1
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == k:
                result = mid
                right = mid - 1
            elif arr[mid] < k:
                left = mid + 1
            else:
                right = mid - 1
        return result


# Test cases
if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 2, 2, 3, 4, 5]
    k = 2
    print(sol.binarysearch(arr, k))  # Output: 1
    k = 3
    print(sol.binarysearch(arr, k))  # Output: 4
    k = 6
    print(sol.binarysearch(arr, k))  # Output: -1
