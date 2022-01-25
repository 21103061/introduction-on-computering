# QUESTION1: Write the python code of the following :
# Answer: input_string = "Python is a case sensitive language"
print("input_string")
# (a) Find the length of the input string.
print('/n (a)')
print("The length of the input string: /n,len(input_string)")

# (b) Reverse the order of the string in one line code.
print('/n (b)')
print("The reversed of the input string:/n ",'input_string'  [::-1])

# (c) Using slice function store "a case sensitive" in new string.
print('/n (c)')
new_string = 'input_string'[10:26]
print("Store a case sensitive in new string: /n",'new_string')

# (d) Replace 'a case sensitive' with 'object oriented'.
print('/n (d)')
updated_string = 'input_string'.replace('a case sensitive','object oriented' )
print("Updated string after replacing 'a case sensitive ' with 'object oriented'")

# (e) Find index of substring "a" in the given input string.
print('/n (e)')
index_string = 'input_string'.find('a')
print("The index of substring 'a' in the given input: /n,"'index_string')

# (f) Remove the white spaces from the given input string.
print('/n (f)')
inp_string = 'input_string'.replace('','')
print("string after removing the white space from the given input string: /n",'inp_string')


# QUESTION2: Use the string formatting to print your name, SID, department name and CGPA in  the following output:
# ANSWER:
NAME = ("MUSKAN")
SID = 21103061
DEPARTMENT_NAME = "CSE"
CGPA = 9.9
PRINT(f"/nHey, {name} here!/n")
f"My SID is {SID} /n"
f"I from {department_name} department and my CGPA is {CGPA}"

# QUESTION3: For a = 56 and b = 10 with the help of the bitwise operators calculate the following:
# ANSWER:
a = 56
b = 10
print('/n (a)')
print("With the help of bitwise AND operation:/n",a & b)
print('/n (b)')
print("With the help of bitwise OR operation:/n",a|b)
print('/n (C)')
print("With the help of bitwise XOR operation:/n",a^b)
print('/n (d)')
print("Bitwise left shift a with 2 bits: /n",a<<2)
print("Bitwise left shift b with 2 bits:/n",b<<2)
print('/n (e)')
print("Bitwise right shift a with 4 bits: /n",a>>4)
print("Bitwise right shift b with 4 bits: /n",b>>4)

# QUESTION4: To find the greatest of three numbers entered by the user.
# ANSWER:
num1 = float(input("/nEnter the first number:/n"))
num2 = float(input("/nEnter the second number:/n"))
num3 = float(input("/nEnter the third number:/n "))
if(num1>num2) and (num1>num3):
    print(f"First number i.e. {num1} is the greatest.")
elif (num2>num1) and (num2>num3):
    print(f"Second number i.e. {num2} is the greatest.")
else:
    print(f"Third number i.e. {num3} is the greatest.")

# QUESTION5: To check if the word 'name' is present in the string entered by the user or not(print: "YES or NO").
# ANSWER:
input_string = input("/nEnter the string:/n")
print("/nThe word 'name' is present in the entered string or not (YES or NO)?")

if "name" in input_string
    print("YES /n")
else:
    print("NO /n")

# QUESTION6: To check whether the given input lengths can form a triangle or not(Print: "yes or no").
# ANSWER:
side1 = int(input("Enter the first side of a triangle:/n"))
side2 = int(input("Enter the second side of a triangle:/n"))
side3 = int(input("Enter the third side of a triangle :/n"))
sum1 = side1 + side2
sum2 = side2 + side3
sum3 = side3 + side1
if side1>sum1 or side1>sum2 or side1>sum3:
    print("No")
elif side2>sum1 or side2>sum2 or side2>sum3:
    print("No")
elif side3>sum1 or side3>sum2 or side3>sum3:
    print("No")
else:
    print("Yes")

































