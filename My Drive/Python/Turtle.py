#___________Menu____________
#Prints the format of the menu.
def menu():
    print('[1] Hello user')
    print('[2] Option 2')
    print('[3] Option 3')
    print('[4] Option 4')
    print('[5] Option 5')
    print('[6] Option 6')

menu() #displays menu
option = input("choose an option: ") #asks user to choose option
#option 1 when chosen will show text asking what your name is.
#once you input your name the command will say "hello 'name' nice to see you" "todays date is..."
if option == '1':
    name = input ("what is your name?")
    from datetime import date
    Day = date.today()
    print (f"hello {name} thanks for being here.")
    print (f"todays date is {Day}")

