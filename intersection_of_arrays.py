from collections import Counter
def intersect(nums1, nums2):
    c1 = Counter(nums1)
    c2 = Counter(nums2)
    ret = []
    for c in c1:
        if c in c2:
            ret.extend([c] * min(c1[c], c2[c]))
    return ret

print(intersect([1,2,2,1], [2,2]))