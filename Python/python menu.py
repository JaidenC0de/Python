#___________Menu____________
#Prints the format of the menu.
from audioop import add


def menu():
    print('Hello User')
    print('[1] choose 1 for name entering')
    print('[2] choose 2 for adding numbers')
    print('[3] Option 3 for plus +1')
    print('[4] Option 4')
    print('[5] Option 5')
    print('[6] Option 6')

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

elif option == '4':
    