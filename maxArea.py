def maxArea(height):
    m = 0
    for index, element in enumerate(height):
        for s_i, s_e in enumerate(height[index+1:]):
            m_height = min(element, s_e)
            m = max(m, m_height * (s_i+1))
    return m 

print(maxArea([1,8,6,2,5,4,8,3,7]))
