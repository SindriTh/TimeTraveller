# https://github.com/SindriTh/TileTraveller

# Sindri Þór Harðarson, Friðrik Tryggvi Róbertsson, Ólafur Starri Pálsson.

# Við gerðum alorithma á töflu sem var fyrir framan okkur og ákváðum að skipta vandamálinu niður í 4 föll
# Við enduðum með föllin printallowed sem prentar mögulegar hreyfingar.
# getinput sem sækir input frá notanda og kallar í fallið isallowd sem athugar hvort hreyfingin sé lögleg.
# ef isallowed er True þá keyrir getinput fallið nexttile sem skilar nýrri staðsetningu notenda.

# Strengirnir hér fyrir neðan geyma löglegar hreyfingar, því við meigum ekki nota list.
coins_taken = []

str11 = "n"
str12 = "nes"
str13 = "es"
str21 = "n"
str22 = "sw"
str23 = "ew"
str31 = "n"
str32 = "ns"
str33 = "sw"
location = 11
coins = 0
## Function 1 printallowed
# Prentar allar mögulegar hreyfingar í hverjum reit.
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
# Fær input frá notanda og ef það er löglegt, skilar hann því sem nýrri staðsetningu
def getinput(currentloc,allowed_moves):
        movement=input('Direction: ')
        if isallowed(movement,allowed_moves):
            return nextTile(currentloc, movement)
            
        else:
            print('Not a valid direction!')
            coins_taken.append(currentloc)
            return currentloc  


## Function 3 allowed
# Testar hvort input frá notanda sé löglegt
def isallowed(movement,allowed_moves):
    for ch in allowed_moves:
        if ch.lower() == movement.lower():
            return True
    return False

## Funtion 4 nextTile
# Býr til næstu staðsetningu út frá innslátti notanda og núverandi staðsetningu
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
    
def leaver(currentloc,tokens):
    if currentloc not in coins_taken:
        string = input("Pull a lever (y/n): ")
        if string == "y" and currentloc not in coins_taken:
            tokens += 1
            print("You received 1 coin, your total is now {}.".format(tokens))
    
    return tokens
    

while location != 31:

    if(location == 11):
        printallowed(str11)
        location = getinput(location,str11)
        
    elif(location == 12): # Lever
        coins = leaver(location,coins)
        printallowed(str12)
        location = getinput(location,str12)

    elif(location == 13):
        printallowed(str13)
        location = getinput(location,str13)

    elif(location == 21):
        printallowed(str21)
        location = getinput(location,str21)

    elif(location == 22): # Lever
        coins = leaver(location,coins)
        printallowed(str22)
        location = getinput(location,str22)

    elif(location == 23): # Lever
        coins = leaver(location,coins)
        printallowed(str23)
        location = getinput(location,str23)

    elif(location == 31):
        printallowed(str31)
        location = getinput(location,str31)

    elif(location == 32): # Lever
        coins = leaver(location,coins)
        printallowed(str32)
        location = getinput(location,str32)

    elif(location == 33):
        printallowed(str33)
        location = getinput(location,str33)
print("Victory! Total coins {}.".format(coins))
