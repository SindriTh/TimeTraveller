# https://github.com/SindriTh/TileTraveller

str11 = "n"
str12 = "nes"
str13 = "es"
str21 = "n"
str22 = "sw"
str23 = "we"
str31 = "n"
str32 = "ns"
str33 = "sw"
location = 11

## Function 1 printallowed
def printallowed(allowed_moves):
    out_str = ""
    length = len(allowed_moves)
    for i in range(length):
        if out_str != "":
            out_str += " or "
        if allowed_moves[i].lower() == "n":
            out_str += "(N)orth"
        if allowed_moves[i].lower() == "e":
            out_str += "(E)ast"
        if allowed_moves[i].lower() == "s":
            out_str += "(S)outh"
        if allowed_moves[i].lower() == "w":
            out_str += "(W)est"
    out_str += "."
    print("You can travel:",out_str)

        
## Function 2 getinput
def getinput(currentloc,allowed_moves):
        movement=input('Direction: ')
        if isallowed(movement,allowed_moves):
            return nextTile(currentloc, movement)
            
        else:
            print('Not a valid direction!')
            return currentloc  


## Function 3 allowed
def isallowed(movement,allowed_moves):
    for ch in allowed_moves:
        if ch.lower() == movement.lower():
            return True
    return False

## Funtion 4 nextTile

def nextTile(currentloc, movement):
    if movement.lower() == "n":
        currentloc += 1
    if movement.lower() == "s":
        currentloc -= 1
    if movement.lower() == "e":
        currentloc += 10
    if movement.lower() == "w":
        currentloc -= 10
    return currentloc
    

while location != 31:

    if(location == 11):
        printallowed(str11)
        location = getinput(location,str11)
        
    elif(location == 12):
        printallowed(str12)
        location = getinput(location,str12)

    elif(location == 13):
        printallowed(str13)
        location = getinput(location,str13)

    elif(location == 21):
        printallowed(str21)
        location = getinput(location,str21)

    elif(location == 22):
        printallowed(str22)
        location = getinput(location,str22)

    elif(location == 23):
        printallowed(str23)
        location = getinput(location,str23)

    elif(location == 31):
        printallowed(str31)
        location = getinput(location,str31)

    elif(location == 32):
        printallowed(str32)
        location = getinput(location,str32)

    elif(location == 33):
        printallowed(str32)
        location = getinput(location,str33)
print("Victory!")
