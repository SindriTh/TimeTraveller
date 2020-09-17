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
stadsetning = 12

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


## Function 3 allowed


## Funtion 4 nextTile


if(stadsetning == 11):
    printallowed(str11)
 #   getinput(str11)
elif(stadsetning == 12):
    printallowed(str12)
  #  getinput(str12)
elif(stadsetning == 13):
    printallowed(str13)
    getinput(str13)
elif(stadsetning == 21):
    printallowed(str21)
    getinput(str21)
elif(stadsetning == 22):
    printallowed(str22)
    getinput(str22)
elif(stadsetning == 23):
    printallowed(str23)
    getinput(str23)
elif(stadsetning == 31):
    printallowed(str31)
    getinput(str31)
elif(stadsetning == 32):
    printallowed(str32)
    getinput(str32)
elif(stadsetning == 33):
    printallowed(str32)
    getinput(str33)