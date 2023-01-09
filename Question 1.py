MyGrade = int(input("Enter the Marks "))

if 0<= MyGrade :
    if 80< MyGrade :
            print("Your Grade is ‘A’")
    elif 60< MyGrade <=80 :
            print("Your Grade is ‘B’")
    elif 50< MyGrade <=60 :
            print("Your Grade is ‘C’")
    elif 45< MyGrade <=50 :
            print("Your Grade is ‘D’")
    elif 25<= MyGrade <=45 :
            print("Your Grade is ‘E’")
    elif 0<= MyGrade <=25 :
            print("Your Grade is ‘F’")
    else:
        pass
else:
     print("Enter a Valid Marks")