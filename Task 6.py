# Переписати def sort_numbers(nums): nums.sort() return nums так, щоб функція була immutable
def sort_numbers(nums):
    return sorted(nums)

# Приклад
nums = [3, 1, 2]

sorted_nums = sort_numbers(nums)

print(nums)        # [3, 1, 2]
print(sorted_nums) # [1, 2, 3]