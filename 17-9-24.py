#Create a dictionary where the keys are tuples representing coordinates (x, y) and the values are city names. Write a Python program to print the city name for a given coordinate.
city_coordinates = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles",
    (41.8781, -87.6298): "Chicago",
    (29.7604, -95.3698): "Houston",
    (33.4484, -112.0740): "Phoenix"
}


def get_city_name(coordinate):
    return city_coordinates.get(coordinate, "City not found")


if __name__ == "__main__":
   
    coordinate = (41.8781, -87.6298)
    
    city_name = get_city_name(coordinate)
    
    print(f"The city at coordinates {coordinate} is {city_name}.")



    #####Write a Python program to sort a tuple of tuples based on the second element of each tuple.


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




###  Write a Python program to find the minimum and maximum elements in a tuple of integers.


numbers = (550, 200, 680, 750, 900)

min_value = min(numbers)
max_value = max(numbers)


print(f"Min: {min_value}, Max: {max_value}")


#### Given a tuple containing nested tuples, write a Python program to flatten it into a single tuple.


def flatten_tuple(nested_tuple):
    flattened = []

    for item in nested_tuple:
        if isinstance(item, tuple):
          
            flattened.extend(flatten_tuple(item))
        else:
            
            flattened.append(item)

    return tuple(flattened)


nested = (9, (3, 6), (2, 8, 5))


flattened_result = flatten_tuple(nested)


print(flattened_result)

