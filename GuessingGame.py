pin = 2010

loopNum = 1
attempts = 3

while loopNum <= attempts:
    Trial = int(input("Enter Pin: "))
    if pin == Trial:
        print("pin Accepted")
        break
    else:
        attempts = attempts - 1

        if attempts != 0:
            print("Pin is Wrong " + str(attempts) + " attempts left")
        else:
            print("Pin is wrong, try again later")



