def max_value(*nums) -> int:
    if not nums:
        raise ValueError("At least one number is required")
    return max(nums)

print(max_value())