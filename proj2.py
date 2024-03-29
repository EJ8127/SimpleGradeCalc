'''
Eric Gomez
Project #1
Description: Find the average grade of multiple students
'''
#global values

def main():
    answer = 1
    #used to break out when user is done
    while answer == 1:
    #Retrieves user inputs to calculate
        name = input("Enter student's name: ")
        gtotal = 0
        #checks for 3 test grades
        for i in range(3):
            grade = eval(input("Enter the test grade: " ))
            gtotal += grade
            #validates inputs
            while grade < 0 or grade > 100:
                grade = eval(input("Invalid input. Enter the test "))
                gtotal += grade
           #checks attendance
        attend = eval(input("Enter attendance percentage: "))
        #validates inputs for attendance
        while attend < 0 or attend > 100:
            attend = eval(input("Invalid input, Enter attendance percentage: "))
            #calculates the grades
        average = gtotal / 3
        total = average * .9 + attend *.1
        #checks for letter grade
        if total >= 90:
            gradet = 'A'
        elif total >= 87:
            gradet = 'B+'
        elif total >= 80:
            gradet = 'B'
        elif total >= 77:
            gradet = 'C+'
        elif total >= 70:
            gradet = 'C'
        elif total >= 67:
            gradet = 'D+'
        elif total >= 60:
            gradet = 'D'
        else:
            gradet = 'F'

        print(name+" recieved a(n) "+gradet)
        #checks if user wants to check another student
        stay = eval(input("Is there another student? Type 1 for yes and 2 for no"))
        while stay < 0 or stay > 2:
            stay = eval(input("Incorrect input, please answer y or n. Is there another student?"))
        if stay == 1:
            answer = 1
        else:
            answer = 2
main()
'''
* means user inputs

Output
Enter student's name: *****
Enter the test: **
Enter the test: **
Enter the test: **
Enter attendance percentage: **
****** got an **

---------------
Pseudocode
while loop to check 
for loop to get 3 test grade 

Get input from user (There name)
Get grade of test 1
Get grade of test 2
Get grade of test 3
Get Percentage of attendance

Calculate the percentage of each test by multiplying by .30 in this case
ex: test = test1(user input) * .30

add all the values of the percentage of of the grade that was just calculated

if the total score is less then 60
    They got a F
Elif the total score is less then 70
    They got a D
Elif the total score is less then 77
    They got a C
Elif the total score is less then 80
    They got a C+
Elif the total score is less then 87
    They got a b
Elif the total score is less then 90
    They got a B+
Else
    They got an A
    
 while loop to check if user wants to continue
 
 if 1
then continue
else 
end
'''
