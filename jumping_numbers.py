x = int(input("ENTER THE NUMBER :"))
while(x!=0):

    dig =  x %10
    a=dig
    if a-dig == [1,-1,0]:

       x=x//10
       print("it is not a jumping number")
       break
    else:
        print("jumping number")
        break