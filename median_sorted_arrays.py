def find_median(nums1, nums2):
    n1_pointer = 0 
    n2_pointer = 0
    while (n1_pointer + n2_pointer) < (len(nums1) + len(nums2) // 2):
        if nums1[n1_pointer] < nums2[n2_pointer]:
            n1_pointer += 1
        else:
            n2_pointer += 1
    return n1_pointer, n2_pointer

print(find_median([1,3], [2]))