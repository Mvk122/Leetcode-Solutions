from operator import neg
from tkinter import N
from turtle import position


def squares(array):
    final = []
    positive = None
    for index, element in enumerate(array):
        if element > 0:
            positive = index
            negative = index - 1
            break
    if positive is None:
        return [x**2 for x in array][::-1]
    else:
        while positive < len(array) or negative > 0:
            if array[positive] ** 2  > array[negative] ** 2:
                final.append(array[negative]**2)
                negative -= 1
            else:
                final.append(array[positive]**2)
                positive += 1
            print(positive, negative)
    return final

    
print(squares([-4,-1,0,3,10]))
print(squares([-10000,-9999,-7,-5,0,0,10000]))