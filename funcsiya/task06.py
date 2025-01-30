def largest_number(nums):
    nums = list(map(str, nums))
    
    nums.sort(key=lambda x: x*10, reverse=True)
    
    largest_num = ''.join(nums)
    
    return int(largest_num)

print(largest_number([1, 2, 3])) 
print(largest_number([61, 228, 9]))  