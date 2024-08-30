### occurrence of a given characters in string.

"""name=input("Enter a string : ")
character=input("Enter a characterto be searched : ")
count=0
for i in name:
    if(character==i):
        count=count+1
print("count of {} is {}".format(character,count))



###### check if two Strings are Anagram.

s1=input("Enter first string : ")
s2=input("Enter second string : " )

if(len(s1)==len(s2)):
    if(sorted(s1)==sorted(s2)):
        print("These are Anagrams")
    else:
        print("These are not Anagrams")
else:
    print("These are not Anagrams")


 ####### String is palindrome or not.   

name=input("Enter a string/name : ")
print("original string",name)
reversedValue = name[::-1]
print("reversed string",reversedValue)
if (name==reversedValue):
    print("It is a palindrome")
else:
    print("It is not a palindrome")



######## replace the string space with a given character.

string=input("Enter a string : ")
character=input("Enter a character to be repalced : ")
string = string.replace(' ', character)  
print("String after replacing spaces with given character : ")  
print(string) 

    
######## convert lowercase char to uppercase of string.

string=input("Enter a string : ")
string= string.upper()
print(string)


####### convert lowercase vowel to uppercase in string.

string = input("Enter a string: ")
vowels = "aeiou"
for char in string:
    if char in vowels:
        upper_char = char.upper()
        string = string.replace(char, upper_char)
print("Uppercase vowels string:", string)



##### separate characters in a given string.

string = input("Enter a string : ")
print("Separating characters from given string:")
for i in range(0, len(string)):  
    print(string[i], end="  ");



##### remove blank space from string.

s=input("Enter a string : ")
s1=s.replace(" ","")
print("The string after removing blank spaces")
print(s1)


######concatenate two strings using join() method.

string1 =input("Enter 1st string : ")
string2 = input("Enter 2nd string : ")
print("".join([string1, string2]))
string3 = " ".join([string1, string2])
print(string3)"""

##### concatenate two strings without using join() method.

str1 = input("Enter the value of Str1: ")   
str2 = input("Enter the value of Str2: ")      
print("{} {}".format(str1, str2,))      
str3 = "{} {}".format(str1, str2,)      
print(str3)    



######## remove repeated character from string.

"""s = input("Enter the string: ")
newstr = ''        
for letter in s:    
   if letter not in newstr:
     newstr += letter        
     print("The string with duplicate letters removed:", newstr)



 ####### check given character is vowel or consonant.

character = input("Enter a character: ")  
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  
if character in vowels:  
    print(f"The character '{character}' is a vowel!")  
else:  
    print(f"The character '{character}' is a consonant!")  



###### check given character is digit or not.

ch = input("Enter Your Character : ")
if(ch.isdigit()):
    print("The Given Character ", ch, "is a Digit")
else:
    print("The Given Character ", ch, "is Not a Digit")




######### delete vowels in a given string.
 
def rem_vowel(string): 
	vowels = ['a','e','i','o','u'] 
	result = [letter for letter in string if letter.lower() not in vowels] 
	result = ''.join(result) 
	print(result) 
string = input("Enter the string : ")
rem_vowel(string) 




######## count the Occurrence Of Vowels & Consonants in a String.

str1 = input("Please Enter Your Own String : ")
vowels = 0
consonants = 0

for i in str1:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
       or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1
 
print("Total Number of Vowels in this String = ", vowels)
print("Total Number of Consonants in this String = ", consonants)



###### highest frequency character in a String.

string= input("Enter your string : ")
print(string)

char_freq={}

for i in string:
    if i in char_freq:
        char_freq[i]=char_freq[i]+1
    else:
        char_freq[i] = 1
result= max(char_freq, key = char_freq.get)

print("Most frequent character: ",result)


########## Replace First Occurrence Of Vowel With ‘-‘ in String.

def replace_vowel(string):
    vowels = "AEIOUaeiou"
    for i in range(len(string)):
        if string[i] in vowels:
            string = string[:i] + '-' + string[i+1:]
            break
    return string

string = input("Please enter a string: ")
print("Original String:", string)
print("Modified String:", replace_vowel(string))



######## count alphabets, digits and special characters.

string = input("Please Enter your Own String : ")
alphabets = digits = special = 0

for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets = alphabets + 1
    elif(string[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1
        
print("\nTotal Number of Alphabets in this String :  ", alphabets)
print("Total Number of Digits in this String :  ", digits)
print("Total Number of Special Characters in this String :  ", special)



####### given character is digit or not using isdigit() method.

ch = input("Please Enter Your Own Character : ")

if(ch.isdigit()):
    print("The Given Character ", ch, "is a Digit")
else:
    print("The Given Character ", ch, "is Not a Digit")





######## calculate sum of integers in string.

num= input("Enter number : ")
sum = 0

for i in num:
    sum = sum + int(i)

print(sum)






######## print all non repeating character in string.

Str = input('Enter a string: ')

for i in Str:

    count = 0

    for j in Str:

        if i == j:

            count+=1

        if count > 1:

            break

    if count == 1:

        print(i,end = " ")





####### copy one string to another string.
str1 = input("Please Enter Your Own String : ")

str2 = str1
str3 = str1[:]

print("The Final String : Str2  = ", str2)
print("The Final String : Str3  = = ", str3)"""








 


