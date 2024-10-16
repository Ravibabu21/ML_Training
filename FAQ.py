
#ask user to give list of numbers, if number is divisble
#  by 5 and print and continue if not
#  and break number is greater than 100

def listnum(list):
    for listnumber in list:
        if (listnumber>100):
            break
        elif (listnumber%5!=0):
            continue
        elif (listnumber%5==0):
            print(listnumber)
listnum([5,55,14,20,25,65,100,150,2500])

