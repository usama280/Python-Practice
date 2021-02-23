# print('hello')


#OUTPUT
'''
print('   /|')
print('  / |')
print(' /  |')
print('/___|')
'''


#STRING
'''
name = 'John'
print(name + ' is cool') #John is cool
print(name[0]) #J
print(name.index('o'))      #1
print(name.replace('J', 'j'))   #john
'''


#MATH
'''
print(3 * (4+5))
print(10 % 3)
print(str(5) + ' houses')
print(abs(-5))
print(round(3.5))

from math import *      #import
print(pow(3,2)) #9
'''


#INPUT
'''
num1 = input('Enter num 1: ')
num2 = input('Enter num 2: ')

print(num1 + num2) #num1num2
print(float(num1) + float(num2))    #num1 + num2
'''


#LIST
'''
friends = ['Justice', 'Justin', 'Jake']
print(friends[1])   #Justin
print(friends[1:])  #Justin, Jake
print(friends[-1])  #Jake
print(friends[0:1])  #Justice

friends[1] = 'Nikhil'
print(friends[1])   #Nikhil


lucky_nums = [1,2,3,4,5]
#friends.extend(lucky_nums)  - links two lists togather
print(friends)  

friends.append('Creed') #add item to end of list
friends.insert(1, 'Creed') #add item to index
friends.remove('Jake')
friends.pop()   #remove end item
print(friends) 

friends.sort() #sorts 
print(friends) 
friends2 = friends.copy() #copy of orig
friends2.reverse() #sorts in reverse
print(friends2) 

print(friends.index('Creed')) 
print(friends.count('Creed')) 

friends.clear() #Empty's list
'''
 

#TUPLES 
'''
coord = (4,5)   #immutable
print(coord[0]) # 4
'''


#FUNCTIONS 
'''
def say_hi(name):
    print('Hello ' + name)

say_hi('Pi')


def cube(num):
    return num**3

print(cube(3))
'''


#IF STATEMENT
'''
is_male = True
is_tall = False

if is_male and is_tall:
    print("Male and tall")
elif is_male or is_tall:
    print("Male or tall")
else:
    print("Female")
'''


#TERNARY OPERATOR
'''
x = 8
print("kid" if x<10 else 'teen' if x < 18 else 'adult')
'''


#OPERATOR STATEMENTS
'''
def max_num(x1, x2, x3):
    if x1>=x2 and x1>=x3:
        return x1
    elif x2>=x1 and x2>=x3:
        return x2
    else:
        return x3

print(max_num(100,200,300))        
'''


#CALCULATOR SIMPLE
'''
num1 = float(input('Enter num: '))
num2 = float(input('Enter num: '))
oper = input('Enter operator: ')

def calc(n1,n2, o):
    if o == '+':
        return n1+n2;
    elif o == '-':
        return n1-n2;
    elif o == '/':
        return n1/n2;
    elif o == '*':
        return n1*n2;
    else:
        return "Error"

print(calc(num1, num2, oper))
'''


#DICTIONARY 
'''
month_conv = {
    'Jan' : 'January',
    'Mar' : 'March',
    'Apr' : 'April'
    }

print(month_conv['Mar'])    #March
print(month_conv.get('Apr'))    #April
print(month_conv.get('Dec', 'Not Valid'))   #Not Valid
'''


#WHILE LOOP
'''
i = 1
while i<=10:
    print(i)
    i+=1
'''


#GUESSING GAME
'''
from random import *  #import
val = randint(0, 10)    #random int between 0 and 10
guess = -1

while guess != val:
    guess = int(input('Guess val: '))

print('You got it!')
'''


#FOR LOOPS
'''
for letter in 'Hello World!':
    print(letter)


friends = ['Jim', 'Justin', 'Jake']
for name in  friends:
    print(name)
#OR
for index in range(len(friends)):
    print(friends[index])


for i in range(3,10):
    print(i)    #3-9
'''


#2D ARRAY
'''
grid = [
[1,2,3],
[4,5,6],
[7,8,9]
]

print(grid[0][2])   #3

for row in grid:
    for col in row:
        print(col)
'''


#VOWEL REMOVER
'''
def vowelRemover(phrase):
    result = ''

    for letter in phrase:
        if letter in 'AEIOUaeiou':
            result += ''
        else:
            result += letter
    return result

print(vowelRemover(input('Enter phrase: ')))
'''


#TRY AND EXCEPT
'''
while True:
    try:
        num = int(input('Enter Num: '))
        print(num)
        break;
    except ZeroDivisionError:
        print('Divided by 0')
    except ValueError as err:
        print('Invalid Input')
        print(err)         #Specific error msg
'''


#READ FILES
'''
file = open('Employee.txt', 'r') #r - read, w - write, a- append, r+ - read and write
print(file.readable()) #True

print(file.readline()) #Reads first line
print(file.readline()) #Reads next line
#OR
print(file.readlines()) #Puts each line into array   -    Can also get specific index: file.readlines()[i]
#OR
for emp in file.readlines():
    print(emp)

print(file.read()) #Everything in file
file.close()
'''


#WRITE OR APPEND FILES
'''
file = open('Employee.txt', 'a') #r - read, w - write, a- append, r+ - read and write
file.write('\nToby - Human Resources')

file.close()

file = open('Employee2.txt', 'w') #r - read, w - write, a- append, r+ - read and write
file.write('Toby - Human Resources\n')

file.close()
'''


#MODULES
'''
import usefulTools

print(usefulTools.roll_dice(10))
'''


#CLASS
'''
#     file           class
from Student import Student

student1 = Student('Jim', 'Business', 3.5, False)
student2 = Student('Pam', 'CompSci', 3.8, True)

print(student1.name)    #Jim
'''


#MULTIPLE CHOICE QUIZ
'''
from Question import Question

quest_prompts = ['What color are apples? \n(a) Red\n(b) Blue\n(c) Purple\n\n', 
                 'What color are bananas? \n(a) Red\n(b) Blue\n(c) Yellow\n\n',
                 'What color are grapes? \n(a) Red\n(b) Blue\n(c) Purple\n\n'
                ]

questions = [Question(quest_prompts[0], 'a'),
             Question(quest_prompts[1], 'c'),
             Question(quest_prompts[2], 'c')
            ]

q = Question
q.run_test(questions)

#OR 

def run_test(quests):
        score = 0;

        for q in quests:
            answer = input(q.prompt)
            if answer == q.answer:
                score += 1
        print("Score: " + str(score) + "/" + str(len(quests)))

run_test(questions)
'''


#CLASS METHODS
'''
from Student import Student

student1 = Student('Jim', 'Business', 3.5, False)
student2 = Student('Pam', 'CompSci', 3.8, True)

print(student1.on_honour_roll())    #False
print(student2.on_honour_roll())    #True
'''


#INHERITANCE
'''
from Chef import Chef 
from ThaiChef import ThaiChef

myChef = Chef
myChef.make_special()

myThaiChef = ThaiChef
myThaiChef.make_rice()
myThaiChef.make_special()
'''


#2D ARRAY DECLARE + INITIALIZE
'''
matrix = [[0]*3 for c in range(5)] # 5X3
k = 0

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix[i][j] = k
        k+=1

print(matrix)
'''

#MATRIX EXAMPLE
'''
from Relation import Relation


matrix = [[0]*7 for c in range(7)]
r = Relation(matrix)

r.mat()
print(r.ref())
print(r.sym())
print(r.tran())
'''

'''
word = 'hello'
used_letters = ['e','l']
word_list = []


for letter in word:
    if letter in used_letters:
        word_list.append(letter)
    else:
        word_list.append('-')


#word_list = [letter if letter in used_letters else '-' for letter in word]

print(word_list)
'''