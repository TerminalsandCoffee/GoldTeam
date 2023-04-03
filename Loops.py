#python loops

#accept user input
upper_number = int(input("How many values should we process: "))

#range from 1 to the users provided input
for number in range(1, upper_number + 1):
     if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
     elif number % 3 == 0:
        print("Fizz")
     elif number % 5 == 0:
        print("Buzz")
     else:
        print(number)
        
 