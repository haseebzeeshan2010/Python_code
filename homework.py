def welcome():
    name = input("What's your name?")
    if len(name) > 2:
        print(f"Welcome {name}")
    return(name)




def radiuscor(rad):
    if rad > 0:
        return(rad)





def circum(rad):
    diameter = rad*2
    pi = 3.14
    circumference = diameter*pi
    return(circumference)




def ar(rad):
    pi = 3.14
    area = pi*(rad**2)
    return(area)





def vol(rad):
    pi = 3.14
    volume = (4/3)*pi*(rad**3)
    return(volume)

def prints(circ,ar,vol,name):
    print(f"circumference of a circle is {round(circ,2)} area of a circle is {round(ar,2)} and volume of a sphere is {round(vol,2)}")
    print(f"goodbye {name}")



name = welcome()

rad = int(input("Please enter the radius: "))
radcor = radiuscor(rad)

circumference = circum(radcor)
area = ar(radcor)
volume = vol(rad)

prints(circumference,area,volume,name)