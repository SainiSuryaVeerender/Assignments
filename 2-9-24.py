#### empty tuple in python

my_tuple=()
print(my_tuple)



#### unpack a tuple into several variables

a = input("Enter College name : ") 
b=input("Enter Students : ")
c=(input("Enter branch : "))

(college,students,branch)=a,b,c 

print(college)

print(students)

print(branch)


####   add an item to the tuple 

t = (22,30,42,64,88) 

print(t)

t = t + (20,)

print(t)

l = list(t) 

l.append(30)

t = tuple(l)

print(t)



### convert tuple into a string

t = ('S', 'U', 'R', 'Y', 'A', ' ', 'S', 'A', 'I', 'N' , 'I')
s =  ''.join(t)
print(s)



###### find most frequent element in tuple


test_tuple = input("Entetr text : ")

print("The original tuple : " + str(test_tuple))

cnt = 0
res = test_tuple[0]

for ele in test_tuple:
	curr_freq = test_tuple.count(ele)

	if(curr_freq > cnt):
		cnt = curr_freq
		res = ele

print("Maximum element frequency tuple : " + str(res))