# binary search tree
# Given an array in ascending order and a target value
# return the target value starts and ends.
# If the target value is not in memory, return [-1, -1]

def searchRange(nums, target):
    def findBound(nums, target, isLeft):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target or (isLeft and nums[mid] == target):
                right = mid - 1
            else:
                left = mid + 1
        return left if isLeft else right

    # left one
    left_bound = findBound(nums, target, True)
    # right one
    right_bound = findBound(nums, target, False)

    # check if it's valid
    if left_bound <= right_bound and right_bound < len(nums) and nums[left_bound] == target and nums[right_bound] == target:
        return [left_bound, right_bound]
    return [-1, -1]

# testing
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums, target))

target = 6
print(searchRange(nums, target)) 
