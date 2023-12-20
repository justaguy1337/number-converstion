import time



def dtb(num):
    
    if num >= 1:
        dtb(num // 2)
        time.sleep(.1)
        print(num % 2, end = '')

def dto(num):

    if num >= 1:
        dto(num // 8)
        time.sleep(.1)
        print(num % 8, end = '')

def dth(num):

    if num >= 1:
        dth(num // 16)
        x =num % 16
        y=x
        if x==10:
            y='A'
        if x==11:
            y='B'
        if x==12:
            y='C'
        if x==13:
            y='D'
        if x==14:
            y='E'
        if x==15:
            y='F'
        time.sleep(.1)
        
        print(y, end = '')
        
def one():
    
    try:

        num = int(input("\nEnter number in decimal(whole number): "))
        print("\n",num,"in Binary is :")
        dtb(num)

    except ValueError:

        print("\nInvalid Input!!!")
        print("\nPlease try with a whole number   :)")
        

def two():

    try:

        num = int(input("\nEnter number in decimal(whole number): "))
        print("\n",num,"in Octal is :")
        dto(num)

    except ValueError:

        print("\nInvalid Input!!!")
        print("\nPlease try with a whole number   :)")
        

def three():

    try:
        
        num = int(input("\nEnter number in decimal(whole number): "))
        print("\n",num,"in Hexadecimal  is :")
        dth(num)
        
    except ValueError:

        print("\nInvalid Input!!!")
        print("\nPlease try with a whole number   :)")

        
try:
    
    try:

        dict = {1:one, 2:two, 3:three}
    
        choice = 0
        ans = 'y'
        while ans == 'y' :
            print("\nWhat would you like to try?")
            print('\n1.Convert Decimal number into Binary number')
            print('2.Convert Decimal number into Octal number')
            print('3.Convert Decimal number into Hexadecimal number')
            choice = int(input('\nPlease enter your choice: '))
            dict.get(choice)()
            ans = input('\n\nDo you want to do something else?\n(y/n)--->')
            ans=ans.lower()

        if ans != 'y':
            print('\n\t\t\tThank You, Have a nice day')
        
    except ValueError:
        
        print("\nInvalid Choice!")

except TypeError:

    print("\nInvalid Choice!!!")
