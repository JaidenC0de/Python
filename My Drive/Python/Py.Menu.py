#___________Menu____________
#Prints the format of the menu.
def menu():
    print('[1] Option 1')
    print('[2] Option 2')
    print('[3] Option 3')
    print('[4] Option 4')
    print('[5] Option 5')
    print('[6] Option 6')

def option():
    print('option 1 doesnt wrk')

menu()
option = int(input("choose an option: "))
#option 1 when chosen will show text asking what your name is.
#once you input your name the command will say "hello 'name' nice to see you" "today date is...""
if option == 1:
    input ("what is your name?: ")