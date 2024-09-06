

####  Write a python program to  add a key to a dictionary

d = {"Name":"Surya" , "Age":23}
print(d)
d.update({"City":"Karimnagar"})
print(d)




#### check weather the given value is present in the dictionary or not 


my_dict = {'a': 10, 'b': 20, 'c': 30}
value_to_check = 40

if value_to_check in my_dict.values():
	print(f"The value {value_to_check} exists in the dictionary.")
else:
	print(f"The value {value_to_check} does not exist in the dictionary.")
	

###print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
###Sample Dictionary
###{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

result_dict = {}
for num in range(1, 16):
    result_dict[num] = num ** 2
print("Resulting dictionary:", result_dict)



##### create a dictionary from the string 

string = "{'A':13, 'B':14, 'C':15}"
 
Dict = eval(string)
print(Dict)
print(Dict['A'])
print(Dict['C'])


###  Write a python program to combine two dictionaries by adding values of common keys ?



d1 = {'Q': 200, 'W': 600, 'R': 300}
d2 = {'Q': 400, 'R': 700, 'd': 300}
combined_dict = {}
for key, value in d1.items():
    combined_dict[key] = value
for key, value in d2.items():
    if key in combined_dict:
        combined_dict[key] += value
    else:
        combined_dict[key] = value

print("Combined dictionary with added values for common keys:", combined_dict)
 



 #### Write a python program to merge two python dictionaries 



dict1 = {1: 'One', 2: 'Two', 3: 'Three'}
dict2 = {5: 'Zero', 4: 'Four'}

print('Merged dictionary:', dict1|dict2)


###### Write a python program to merge two python dictionaries 


def Merge(dict1, dict2):
    return(dict2.update(dict1))


dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

print(Merge(dict1, dict2))

print(dict2)




###### program to sort dictionary by keys or values

myDict = {'rajesh': 20, 'karthik': 40,
        'sanjeev': 15, 'Akhil': 48, 'Lokesh': 32}

myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict = {i: myDict[i] for i in myKeys}

print(sorted_dict)




###Write a Python program to create a dictionary from a string.  Note: Track the count of the letters from the string.
###Sample string : 'w3resource'
###Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

my_string = 'w3resource'

my_dict = {letter: my_string.count(letter) for letter in my_string}
print(my_dict)











