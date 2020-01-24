def farmAnimal():
    a = int(input("number of chickens : "))
    b = int(input("number of cows : "))
    c = int(input("number of pigs : "))
    NoL = (a*2)+(b*4)+(c*4)
    return NoL
print("Number of legs the " + str(farmAnimal()))