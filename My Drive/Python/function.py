#www.programiz.co/python-programming/function
def absolute_value (num) :
    "function returns the absolute value of the entered number"

    if num >= 0:
        return num
    else:
        return -num

#def fancy_av (prompt, num) :
#print ("\nfancy absolute value functions")
#
#    if num >= 0:
#        x=prompt +" "+ str (num)
#        return x
#    else:
#        return -num
#
#print (fancy_av ("\nThe absolute value is",2))
print (absolute_value(2))
print (absolute_value (-4))