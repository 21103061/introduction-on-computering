#QUESTION1:
print("Question1")
a=str(input("Enter any string:"))
list=a.split() #To splite all the elements of string in a list
dict={} #intializing an empty dictionary
if (list._len_()==1) :  #if statement will be implemented when a single word is entered
    for i in list[0]:
        if i in dict:
            dict[i]+=1
    else:
        dict[i]+=1
    print(dict)
else:                #else statement ebill be implemented when more than one word is entered in a string
    for i in list:
        if i in dict:
            dict[i]+=1

    else:
     print(dict)
    print("\n")

    #QUESTION2:
    print("Question 2")
    list1=[1,3,5,7,8]
    list2=[4,6,9,11]
    list3=[2]
    list4=[12]
    while(True):       #while loop is used so that if any wrong value is entered then values will be entered again
        day=int(input("Enter the day:"))
        if(1<=day<=31):
            breakpoint()
        else:
            print("Enter a valid day")
        while(True):    #while loop is used so that if any wrong value is entered then values will be entered a
     month=int(input("Enter the month of the year"))
    if(1<=month<=12):
        breakpoint()
    else:
        print("Enter a valid month")
while(True) : #while loop is used so that if any wrong value is entered then value will be entered
    year=int(input("Enter the year"))
    if(1800<=year<=2025)
       breakpoint()
    else:
        print("Enter the yea from 1800 to 2025 only")
    if month in list1:
      if(day==31):
         day=1
         month=month+1
         print(day,"/",month,"/",year)
      elif(day<31):
          day+=1
         print(day,"/",month,"/",year)
    else:
        print("Enter invalid date")


     list2:
      if(day==30):
          day=1
          month=month+1
          print(day,"/",month,"/",year)
      elif(day<30):
          day+=1
          print(day,"/",month,"/",year)
      else:
          print("Enter invalid date try again")
          Next_Date()
       list: list_str3
          if (year % 4 == 0):
              if(day==29):
                  day=1
                  month=month+1
                  print(day,"/",month,"/",year)
              elif(day<29):
                  day+=1
                  print(day,"/",month,"/",year)
              else:
                  print("Enter invalid date try again")
                  Next_Date()
          else:
              if(day==28):
                  day=1
                  month+=1
                  print(day,"/",month,"/",year)
              elif(day<28):
                  day+=1
                  print(day,"/",month,"/",year)
              else:
                  print("Enter invalid date try again")
       list: list_str4:
    if(day==31):
        day=1
        month=1
        year+=1
        print(day,"/",month,"/",year)
    elif(day<31):
        day+=1
        print(day,"/",month,"/",year)
    else:
        print("Enter invalid date try again")
        Next_Date()
    Next_Date()
    print("/n")


    #QUESTION3:
    print("Question3")
    input_list = input("Enter elements of a list separated by space")
    user_list = inputlist.splite()
    #print list
    print(list)
    print('list: ','input_list')

    #convert each item to int type
    for i in range(len(user_list)):
        #convert each item to int type
        user_list[i] = int(user_list[i])
    squarelist =[(user_list[i],user_list[i]**2)]

    print(squarelist)

    print("/n")

    #QUESTION4:
    print("Question4")
    point = int(input("Enter grade point"))
    #check if the grade point meets the conditions
    if point>10 or point<4:
        print("Enter invalid grade point! try again")
        point = input_point()

    grade = input_point()
    if(grade==4):
        print("Your grade is 'D' and poor performance")
    elif(grade==5):
        print("Your grade is'C' and below average performance")
    elif(grade==6):
        print("Your grade is 'C+' and average performance")
    elif(grade==7):
        print("Your grade is 'B' and good performance")
    elif(grade==8):
        print("Your grade is 'B+' and very good performance")
    elif(grade==9):
        print("Your grade is 'A' and excellent performance")
    else:
        print("Your grade is 'A+' and outstanding performance")
     print("\n")

    #QUESTION5:
    print("Question5")
    x = 6
    for i in range(x):
         #printing_spaces
       for j in range(i):
           print('',end='')
        #printing_alphabet
         for j in range(2*(x-i)-1):
             print(chr(65 + j), end='')    #ASCII value of A=65,B=66,C=67,D=68,E=69,F=70,G=71,H=72,I=73,J=74,K=75
             print()
            print("\n")


         #QUESTION6:
         print("Question6")
         sid = int(input("Enter SID"))
         name = int(input("Enter Name"))
         students[SID] = Name
       elif  option ='N'
             breakpoint()
       else:
            print('invalid input!')

       #part(a) print the dictionary
       print("<a>",students)

       #part(b) sort acc to the names
       print("<b>", {k:v for k,v in sorted (students items, keys = lambda x:x[1])}
       #part(c) sort acc to the SID
       print("<C>"),{k:v for k,v in sorted(students.items())}
       #part(d) search for a student by their SID
       sid = int(input("search name with SID"))
       print("<d> , students[sid]")

    #QUESTION7:
       print("Question7")
       # Function to display the fibonacci sequence
       def recur_fibo(n):
         if n <= 1:
             return n
         else:
             return(recur_fibo(n-1) + recur_fibo(n-2))
    if no_of_terms <=0:   #check if the number of terms is valid
        print("Enter a positive integer")
    else:
        print("fibonacci sequence")
        sum=0
        for i in range(no_of_terms):
            print(recur_fibo(i))
            sum=sum+recur_fibo(i)
        avg=float(sum/no_of_terms)
        print("average of resultant fibonacci series is",avg)


    #QUESTION8:
    print("Question")
    set1 = {1,2,3,4,5}
    set2 = {2,4,6,8}
    set3 = {1,5,9,13,17}
    # part(a)
    set_union = set1.union(set2)
    set_intersection = set1.intersection(set2)
    part_A_set = set_union - set_intersection
    print("<a>",part_A_set)

    # part(b) (subtracting the intersection of sets taken two at a time from the union of all three sets)
    part_B_set = set1.union(set2.union(set3)) - set1.intersection(set2) - set2.intersection(set3) - set3.intersection(set1
    print("<b>")


    # part(c) (subtracting the intersection of all three sets from the intersection of sets taken two at a time)
    part_C_set = ((set1.intersection(set2)).union((set1.intersection(set3)).union((set2.intersection(set3)))
-(set1.intersection(set2.intersection(set3)))

# part(d) (excluding the numbers from 1 to 10 that are in set1)
     for i in range (1,11)
        if i is not set1
     print("<d>")

  # part(e)   (excluding the numbers from 1 to 10 that are in set1 , set2 ,set3)
for i in range (1,11)
    if i not in set1 and i not in set2 and i not in set3:
    print("<e>")
























































