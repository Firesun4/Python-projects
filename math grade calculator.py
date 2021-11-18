percentageForTests = input('What Percentage do tests count for? ')
print(' ')
percentageForHW = input('What Percentage does Homework count for? ')
print(' ')

list1 = []
x = input('What grade did you get on assesments? Type done if done : ')
print(' ')


while x != "done":
    if x.isnumeric():
        list1.append(x)
    x= input('What grade did you get on assesments? Type done if done : ')
    print(' ')


sets = 0 
for i in list1:
    sets += int(i)

lengthoflist = len(list1)
grade = sets/lengthoflist

percentageTest=float(percentageForTests)*0.01

grademath = grade*percentageTest

print('Your Average for Assesments is : ' + str(grade) +'\n')
print(' - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print(' ')

percentageHW = float(percentageForHW)*0.01
z= input('What grade did you get on daily work? Type done if done : ')
print(' ')

set2= 0
list2 = []
while z != "done":
    if z.isnumeric():
        list2.append(z)
    z= input('What grade did you get on daily work? Type done if done : ')
    print(' ')
set2= 0
for p in list2:
    set2 += int(p)

lengthoflist2 = len(list2)

gradeHW = set2/lengthoflist2

gradeHWMath = gradeHW*percentageHW

finalgrade = grademath + gradeHWMath

print('Your Average for Homework is : ' + str(gradeHW) + '\n')

print('Your Overall Average is : ' + str(finalgrade) + ' \n')

input('Type done once you have seen your grade')

