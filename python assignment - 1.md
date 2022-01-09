# ASSIGNMENT 1(INPUT)

# QUESTION1: Write a python program to find average number entered by the user ?
# ANSWER: #taking input from user
print("Question1")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:))
num3=int(input("Enter third number:))
total=(num1+num2+num3)/3
print("Average of three number is: ",total)


# QUESTION2: Write a python to complete a person's income tax. Assume the following tax laws:
# ANSWER: 
print("Question2")
a=int(input("Enter your Gross Income(in nearest penney): $"))
b=int(input("Enter your standard deduction))
c=a-10000-(3000*b)
Tax=c*0.2
print("Your tax is $",Tax)


# QUESTION3: Write python program to store different data type values into the list.
# ANSWER:
print("Question3")
#making the student profile list
SID : 21103061
Name : Muskan
Gender : "F"
Course Name : "CSE"
CGPA : 9.4
std_profile=[SID,Name,Gender,Course_Name,CGPA]
print(std_profile)


# QUESTION4: Write python program to enter marks 5 students into a list and display them is sorted manner.
# ANSWER:
print("Question4")
#Taking list of 5 students
std1=int(input("Enter marks of 1st student"))
std2=int(input("Enter marks of 2nd student"))
std3=int(input("Enter marks of 3rd student"))
std4=int(input("Enter marks of 4th student"))
std5=int(input("Enter marks of 5th student"))
marks_list=[std1,std2,std3,std4,std5]
marks_list.sort()
print("Sorted list (decreasing order)")
print(marks_list)


# QUESTION5: List color['Red','Green','White','Black','Pink','Yellow']
(a).Write a python program to print a specified list after removing 4th element.
#ANSWER:
print("Question5 (a)")
# color_list = ['Red','Green','White','Black','Pink','Yellow']
color_list.remove('Black')
print(color_list)

(b).Remove 'Black' and 'pink' from the list and replace them with 'Purple'.
#ANSWER:
print("Question5 (b))
color_list = ['Red','Green','White','Black','Pink','Yellow']
color_list[3:5]=['Purple']
print(color_list)



