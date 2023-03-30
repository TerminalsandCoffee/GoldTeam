from random import choice
import string
import sys

def string_generator(size=6, string=string.ascii_letters + string.digits):
    return ''.join(choice(string) for _ in range(size))

print()
print("WARNING: Only Accounting, FinOps, and Marketing are authorized to use")
print()
department = input("Enter Department: ")  
    
for _ in department:
    
    if department == "Marketing" or department.lower() == "marketing" :
        break
    elif department == "Accounting" or department.lower() == "accounting" :
        break
    elif department == "FinOps" or department.lower() == "finops" :
        break
    else:
        print("Error: You can not use this generator, enter the name correctly.")
        raise SystemExit
        sys.exit()  

number = int(input("Enter the number of EC2 instances required: "))

if number < 0:
    print("Please enter a positive number: ")

elif number > 0:
    print()

print("##########################")
print("   EC2 Instance Names  ")
print("##########################")
print()

for _ in range(1, number + 1):
    EC2_unique_name = department + "-" + string_generator()
    print("Your EC2 Instance's unique name is: ", EC2_unique_name)



#One way to improve the efficiency of the code would be to use a list of authorized departments instead of multiple if-elif statements. 
#You can use the in keyword to check if the department entered by the user is in the list of authorized departments. 


authorized_departments = ["Accounting", "FinOps", "Marketing"]

department = input("Enter Department: ")

if department.title() not in authorized_departments:
    print("Error: You can not use this generator, enter the name correctly.")
    raise SystemExit


#Another improvement would be to use a while loop for validating the input for the number of instances until a positive number is entered.


while True:
    try:
        number = int(input("Enter the number of EC2 instances required: "))
        if number > 0:
            break
        else:
            print("Please enter a positive number: ")
    except ValueError:
        print("Please enter a valid number: ")
