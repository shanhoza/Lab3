def is_monotonic(nums):
    return (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or
            all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1)))


nums = [6, 5, 4, 4]

print(is_monotonic(nums))
