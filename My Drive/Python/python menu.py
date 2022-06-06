#___________Menu____________
#Prints the format of the menu.
from audioop import add
from datetime import datetime


def menu():
    print('Hello Broski')
    print('[1] choose 1 for name entering')
    print('[2] choose 2 for adding numbers')
    print('[3] Option 3 for plus +1')
    print('[4] Option 4 for minutes to seconds')
    print('[5] Option 5 birthday to seconds')
    print('[6] Option 6 disecting words')
    print('[7] Option 7 string swap')
    print('[8] Option 8 scramble words')

menu() #displays menu
option = input("Choose option here: ") #asks user to choose option
#option 1 when chosen will show text asking what your name is.
#once you input your name the command will say "hello 'name' nice to see you" "todays date is..."
if option == '1':

    name = input ("what is your name?")
    from datetime import date
    Day = date.today()
    print (f"hello {name}. thanks for being here.")
    print (f"todays date is {Day}")
#addition numbers
elif option == '2': 
    #float makes number a floating point number which means it will have a decimal.
    numb = int(input ('choose fisrt number: '))
    num = int(input ('choose second number: '))
    sum = (numb) + (num)
    print (f"your answer is:", sum)
    #takes a number and adds 1 to it.
elif option == '3':
    number = int(input('enter your number of choice '))
    solid_num = 1
    result = (number) + (solid_num)
    print (f'your answer is', result)
#turning minutes into seconds.
elif option == '4':
    minute = int(input('enter number of minutes: '))
    seconds = (60) * (minute)
    print (f'it calculated', seconds)
# turns your birthday into seconds.
#elif option == '5':
#    time_string = 
#cuts the first and last 2 letters of a string.
elif option == '6': 
    string_cheese = input('enter string: ')
    print(string_cheese[0:2],string_cheese[-2:])

#swaps 2 strings from order they were typed in.
elif option == '7':
    string_one = input('enter first string: ')
    string_two = input('enter second string: ')
    string_combine = string_two+string_one
    print(string_combine)
#This code will shift the entered string around and give the length of the string 
elif option == '8': 
    shift_string = input('enter string: ')
    number_length = len(shift_string)
    print(f' length of string' + (number_length))
    #A_string = 2
    #B_string = 1
   # shift_string = (A_string - B_string)
   # print (shift_string)