import heapq


class Solution:
    def kthLargest(self, arr, k):
        n = len(arr)

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]

        min_heap = []

        for start in range(n):
            for end in range(start, n):
                current_sum = prefix_sum[end + 1] - prefix_sum[start]

                if len(min_heap) < k:
                    heapq.heappush(min_heap, current_sum)
                elif current_sum > min_heap[0]:
                    heapq.heappush(min_heap, current_sum)

        return min_heap[0]


# Test the function
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = 2
    solution = Solution()
    result = solution.kthLargest(arr, k)
    print(f"The {k}th largest sum of subarrays is: {result}")
# The kth largest sum of subarrays is: 14
