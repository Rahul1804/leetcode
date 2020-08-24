def findStartIndex(nums, target):
    index = -1
    start = 0
    end = len(nums)-1

    while start <= end:
        mid = start + (end-start)//2
        if nums[mid] == target:
            index = mid
        if nums[mid] >= target:
            end = mid-1
        else:
            start = mid+1
    return index


def findLastIndex(nums, target):
    index = -1
    start = 0
    end = len(nums)-1

    while start <= end:
        mid = start + (end-start)//2
        if nums[mid] == target:
            index = mid
        if nums[mid] <= target:
            start = mid+1
        else:
            end = mid-1
    return index


def searchRange(self, nums: List[int], target: int) -> List[int]:
    return [findStartIndex(nums, target), findLastIndex(nums, target)]


def main():
    nums = []
    target = 8

    print(searchRange(self, nums, target))


main()
