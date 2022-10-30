#def delete(list_, index=None):
   # ...  # TODO реализовать функцию удаления элемента из списка по индексу


#print(delete([0, 0, 1, 2], index=0))  # [0, 1]
#print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
#(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]

def delete(list, index):

    list.pop(index)
    return list

range_1 = [0, 0, 1, 2] #index = 0
range_2 = [0, 1, 1, 2, 3] #index = 1
range_3 = [0, 1, 2, 3, 4, 4] #index = none


print(delete(range_1, 0))
print(delete(range_2, 1))
print(delete(range_3, -1))