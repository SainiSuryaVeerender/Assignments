##### write a Python program to flatten it into a single tuple.
listTup = ((4, 9, 1), (5,6))

print("The tuple of list : " + str(listTup))

flatTup = tuple(sum(listTup, ()))

print("Tuple after flattening : " + str(flatTup))





###### Write a Python program to sort a tuple of tuples based on the second element of each tuple.


def Sort_Tuple(tup):
 
    lst = len(tup)
    for i in range(0, lst):
 
        for j in range(0, lst-i-1):
            if (tup[j][1] > tup[j + 1][1]):
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tup
tup = [(8, 5), (9, 4), (1, 2),
       (5, 1), (6, 3), (7,6)]
 
print(Sort_Tuple(tup))
 