
''' find all such numbers which are divisible by 7 but are not a 
multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be 
printed in a comma-separated sequence on a single line.'''


result = [] 
 
for number in range(2000, 3201): 

    if number % 7 == 0 and number % 5 != 0: 
        result.append(number) 
  
print(result) 




'''With a given integral number n, write a program to generate a dictionary that contains (i, 
i*i) such that is an integral number between 1 and n (both included). and then the program 
should print the dictionary. Suppose the following input is supplied to the program: 8 Then, 
the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}'''

number = int(input("Type a number: "))

numberDict = {}
for i in range(1, number+1):
    numberDict[i] = i*i

print(numberDict)




''' Write a program which accepts a sequence of comma-separated numbers from console 
and generate a list and a tuple which contains every number. Suppose the following input 
is supplied to the program: 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', 
'33', '12', '98'] ('34', '67', '55', '33', '12', '98')'''

numbers = input("Type in numbers seperated only by a comma :")
numbers_split = numbers.split(',')

number_tuple = tuple(numbers_split)

print(number_tuple)
print(numbers_split)



'''Write a program that accepts a comma separated sequence of words as input and prints 
the words ina comma-separated sequence after sorting them alphabetically. Suppose the 
following input is supplied to the program: without, hello, bag, world Then, the output 
should be: bag,hello,without,world'''




phrase = input("Input words: ")

phrase_list = phrase.split(",")
phrase_list.sort()
print((', ').join(phrase_list))




'''Write a program that accepts a sentence and calculate the number of letters and digits. 
Suppose the following input is supplied to the program: hello world! 123 Then, the output 
should be: LETTERS 10 DIGITS 3'''






phrase = input("Type in: ")
phrase = list(phrase)

l, d = 0, 0
for i in phrase:
    if i.isalpha():
        l = l + 1
    if i.isdigit():
        d = d + 1
    else:
        pass

print("Letters:", l)
print("Digits:", d)



'''Write a program that accepts a sentence and calculate the number of upper case letters 
and lower case letters. Suppose the following input is supplied to the program: Hello 
world! Then, the output should be: UPPER CASE 1 LOWER CASE 9'''




phrase = input("Type in: ")
phrase = list(phrase)

u, l = 0, 0
for i in phrase:
    if i.isupper():
        u = u + 1
    if i.islower():
        l = l + 1
    else:
        pass

print("UPPER:", u)
print("lower:", l)




'''Write a program that computes the net amount of a bank account based a transaction 
log from console input.The transaction log format is shown as following: D 100 W 200 D 
means deposit while W means withdrawal. Suppose the following input is supplied to the
program: D 300 D 300 W 200 D 100 Then, the output should be: 500'''


total = 0
while True:
    d_w_trans = input()
    if d_w_trans == "":
        break
    else:
        d_w_trans = d_w_trans.split(" ")
        if d_w_trans[0] == "D":
            total = total + int(d_w_trans[1])
        elif d_w_trans[0] == "W":
            total = total - int(d_w_trans[1])

print(total)