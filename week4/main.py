def hello(nums):
    for i in nums:
        if i % 2 != 0:
            nums.append(i)
    return nums

nums1 = [3,1,2,4]
nums2 = [0]
print(hello(nums1))
