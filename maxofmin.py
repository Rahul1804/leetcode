# Finding maximum number out of minimum from buckets of k size from an unsorted array.
# e.g. Input: [1,3,4,6,2,9,8], and k = 2
# Output: 8
# Explanation:
# First, bucketize the input as per value k = 2 i.e: [1,3], [3,4], [4,6], [6,2], [2,9], [9,8]
# Second, find minimum of each bucket:
# [1,3] -> 1
# [3,4] -> 3
# [4,6] -> 4
# [6,2] -> 2
# [2,9] -> 2
# [9,8] -> 8
# Finally, return maximum of all minimums i.e. 8.

def maxMinInBuckets(nums, k):
    n = len(nums)
    if n == 0 or k <=0:
        return None
    
    # Create bucket
    buckets = [nums[i:i+k] for i in range(n - k + 1)]
    
    # Find the minimum value in the each bucket
    min_values = [min(bucket) for bucket in buckets]
    
    # Return the maximum value among the minimums
    
    return max(min_values)

def main():
    nums = [1, 3, 4, 6, 2, 9, 8]
    k = 2
    output = maxMinInBuckets(nums, k)
    print(output)  # Output: 8

main()
