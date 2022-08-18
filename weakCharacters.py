def numberofWeakCharacters(properties):
    properties.sort(key=lambda x: x[0], reverse=True)
    highest = {}
    prev_atk = properties[0][0]
    weak = 0
    for index, element in enumerate(properties):
        if element[0] in highest.keys():
            if element[1] > highest[element[0]]:
                highest[element[0]] = element[1]
        else:
            highest[element[0]] = element[1]

        if element[0] < prev_atk:
            for k in highest.keys():
                if k > element[0] and highest[k] > element[1]:
                    weak += 1
                    break
        if index < len(properties)-1:
            if properties[index+1][0] < element[0]:
                prev_atk = element[0]
    return weak




q = [[5,5],[6,3],[3,6]]
p =[[10,1],[5,1],[7,10],[4,1],[5,9],[6,9],[7,2],[1,10]]
print(numberofWeakCharacters(p))