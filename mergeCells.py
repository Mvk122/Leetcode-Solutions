import heapq

def minPower(cells):
    heapq.heapify(cells)
    total_power = 0
    while len(cells) > 1:
        print(total_power, cells)
        cell1 = heapq.heappop(cells)
        cell2 = heapq.heappop(cells)
        merged = cell1 + cell2
        total_power += merged
        heapq.heappush(cells, merged)
    return total_power   

