# QUESTION1:
print("QUESTION1")
def TowerOfHanoi(n: , from_rod, to_rod, middle_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, middle_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, middle_rod, to_rod, from_rod)
    n = 3
    TowerOfHanoi(n, 'A','C','B')
    print("\n")


# QUESTION2:
print("QUESTION2")
from math import factorial, remainder
from tracemalloc import start
n=int(input("Enter the size o9f pascals triangle"))

print("using loops")

for i in range(n):
    for j in range(n-i+1):
        print(end="")  #for spacing

    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end="")
        print()  #for new line
    print("\n")

    print('using recurssions')

    def pascal_triangle(n,originalength=n):
        if n == 0:
            return
        pascal_triangle(n-1,originalength)
        #printing the spaces
        print(''*(originalength-n), end='')

        #first number is always 1
        start = 1
        for i in range(1, n+1):

            print(start, end = '')

        #using Binomial Coefficient
        start = start * (n - i) // i
        print()
        pascal_triangle(n)
        print("\n")



    #QUESTION3:
    print("QUESTION3")
    int1, int2 = map(int,input("Enter 2 numbers: ").split())
    Quotient = int1 // int2
    Remainder = int1 % int2

    #part<a>
    print("a. Checking if the quotient and remainder is a callable value or not.")
    print(callable(Quotient))
    print(callable(Remainder))

    #part<b>
    if (Quotient == 0):
        print("<b> The quotient is zero")
    if(Remainder == 0):
        print("<b> The remainder is zero")
    if (Quotient !=0 and Remainder != 0):
        print("<b> All the value are non zero")

    #part <c>
    partClist = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder +6]

  result = []
    for i in range(partClist):
        if partClist[i] > 4:
            'result'.append(partClist[i])
    print(f"<c> Filtered out numbers that are greater than 4 are: {'result'}")

    #part <d>
    setresult = set('result')
    print("<d> Set:",setresult)

    #part <e>
    immutableSet = frozenset(setresult )  #frozen set is used to make the set immutable
    print("<e> Immutable set:",immutableSet)

    #part <f>
    print("<f> Hash value of the max value from the above set:", hash(max(immutableSet)))
    print("/n")


#QUESTION4:
    print("QUESTION4")
    class student:
        def _init_(safe, student,roll_no):
            'self'.name = student
            'self'.roll_no = roll_no

        def _del_(self):
            print("Object destroyed")

        #creating object
        student1 = ("Muskan", 21103061)
        print("Object created")
        #printing the assigned values
        print(f"The name of the student it{'student1_name'} and SID is {'student'.roll_no}")
        #deleting object
        del student1
        print("\n")


    #QUESTION5:
    print("QUESTION5")
    class employee:
        def _init_(self, name, salary):
            self.name = name
            self.salary = salary
        #creating employee records
        emloyee1 = ("Muskan", 45000)
        employee2 = ("Aman", 55000)
        employee3 = ("komal", 65000)

    #'part<a>' updating salary
    employee1_salary = 70000
    print(f"<a> The updated salary of {'employee1_name'} is {'employee1_salary'}")
    #'part<b>' deleting a record
    print("<b>Record of viren deleted",end='')
    print("\n")


#QUESTION6:
print("QUESTION6")
#inputting a word from the first friend
word = input("Enter the word:")
word = word.lower()

#inputting a meaningful word with the exact same letters
test_word = input("Enter a new meaningful word using the exact same letters to test your friendship: ")
test_word = test_word.lower()
#defining dictionary
def count_in_dict(word):
    count = {}
    list1 = list(word)

    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
        return count
    #shopkeeper's input to verify the word's meaning
    def userinput()
        if count_in_dict(word) != count_in_dict(test_word):
            print("The letters aren't exact, friendship is fake")
            return
        ans = input("Does the word makes sense?(y/Y or n/N)")

        if ans == 'y' or ans=='Y':
            print("The friends pass the friendship test")
        elif ans == 'n' or ans=='N':
            print("The word doesn't have a meaning, friendship is fake")
        else:
            print("Invalid input,try again with y/Y or n/N")
            userinput()
        userinput()























