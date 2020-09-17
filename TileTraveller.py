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
location = 12

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
            out_str += "(s)outh"
        if allowed_moves[i].lower() == "w":
            out_str += "(W)est"
    out_str += "."
    print("You can travel:",out_str)

        
## Function 2 getinput
def getinput(location,allowedmoves):
    movement=input('Direction: ')
    if allowed(movement,allowedmoves):
        stadsetning = nexttile(movement,location)
    else:
        print('Not a valid direction!')
        printallowed()        


## Function 3 allowed


## Funtion 4 nextTile


if(location == 11):
    printallowed(str11)
    getinput(location,str11)
elif(location == 12):
    printallowed(str12)
    getinput(location,str12)
elif(location == 13):
    printallowed(str13)
    getinput(location,str13)
elif(location == 21):
    printallowed(str21)
    getinput(location,str21)
elif(location == 22):
    printallowed(str22)
    getinput(location,str22)
elif(location == 23):
    printallowed(str23)
    getinput(location,str23)
elif(location == 31):
    printallowed(str31)
    getinput(location,str31)
elif(location == 32):
    printallowed(str32)
    getinput(location,str32)
elif(location == 33):
    printallowed(str32)
    getinput(location,str33)