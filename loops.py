 counter = 0
my_number = 9

 while(counter < my_number):
     print(f"Counter's value is {counter}")
     counter = counter + 1 # this is the same as counter += 1 


 task1
 pin_number = 1234

 input_pin = int(input("Insert your pin"))
 while(input_pin != pin_number):
     print("Wrong number. Try Again")
     input_pin = int(input())

 print("Your balance is $500")



 how to use for loops 
 numbers = [1, 2, 3, 4, 5] # list
print(numbers[0])

 for loops syntax
 declare a list
 declare a variable called number# assign the first value from the collection to this variable
execute code block under the loop
 reassigns umber variables to the second item in the list

 total = 0

 for number in numbers: 
     print(number)
      print(number * 3)

      if number > 2:
         print(number * 3  )
     total += number
 print(total)



 students = ["Ana", "Collins", "ed", "Joe"]

 for student in students:
     print(student.upper())


 How to combine lists and dicts
students = [
    {"name": "Ana", "result": 92},
    {"name": "Colin", "result": 88},
    {"name": "Ed", "result": 98},
    {"name": "Joe", "result": 67},
]
total = 0

for student in students:
 print(student["result"])
    total += student["result"]

mean_result = total / len(students)
print(mean_result)  this is the same thing as print(total / len(students))