marks1 = int(input("Enter Marks of 1 :"))
marks2 = int(input("Enter Marks of 2 :"))
marks3 = int(input("Enter Marks of 3 :"))

total_parcentage= ((100)*(marks1+marks2+marks3))/300

if (total_parcentage>=40):
    print("pass", total_parcentage)

else:
    print("fail",total_parcentage)