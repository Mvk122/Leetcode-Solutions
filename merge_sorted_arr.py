def merge(nums1, m, nums2, n):
    m_pointer = 0
    n_pointer = 0
    while m_pointer + n_pointer < m+n-1:
        print(m_pointer, n_pointer)
        if nums1[m_pointer] > nums2[n_pointer]:
            if m_pointer == 0:
                nums1.insert(m_pointer, nums2[n_pointer])
                n_pointer += 1
                nums1.pop()
            else:
                nums1.insert(m_pointer-1, nums2[n_pointer])
                n_pointer += 1
                nums1.pop()
        else:
            m_pointer += 1 
    m_pointer += 0
    while n_pointer < n:
        nums1[m_pointer] =  nums2[n_pointer]
        n_pointer += 1
        m_pointer += 1 
    return nums1

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print(merge([1], 1, [], 0))
print(merge([2,0], 1, [1], 1))