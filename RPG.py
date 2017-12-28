# the problem with the end of the game is caused by the break statement in the last two if statements
# probably the indentation
# this is to show Skittles the git shortcut
def instructions():
    print("\t==================================================== \n\tCommands: \n\tgo[direction] \n\tget[item]")
    print('\tYou have to escape the house \n\tusing the commands above. ')
    print('\tTo escape, you need to go to the garden \n\twith a key and a magic.')
    print('\tIf you walk into a room with a monster in it, \n\tyou lose the game ')
    print('\t====================================================')



def status():
    #print the current status
    print('\t----------------------------')
    print('\tYou are in the '+currentRoom)

    #print the current inventory
    print('\tInventory: ', list(inventory))

    #print an item if exists
    if "item" in rooms [currentRoom]:
        print('\tYou see a '+rooms[currentRoom]['item'])
    print('\t----------------------------')

#initialize the inventory array
inventory = []

#link one room to another
rooms = {
        'Hall': {
            'north': 'Kitchen',
            'east': 'Garden',
            'south': 'Bedroom'
        },
        'Bedroom': {
            'north': 'Hall',
            'east': 'Basement',
            'item': 'monster'
        },
        'Kitchen': {
            'south': 'Hall',
            'west': 'Living Room'
        },
        'Living Room': {
            'east': 'Kitchen',
            'item': 'magic'
        },
        'Basement': {
            'north': 'Garden',
            'west': 'Bedroom',
            'item': 'key'
        },
        'Garden':{
            'south': 'Basement',
            'west': 'Hall'
        }
}

#start the player in the Hall
instructions()
currentRoom = 'Hall'

while True:
    status()
#get the player's move
#.split breaks it up into an list array
#eg: typing 'go east' would give the list ['go','east']
    move = ''
    while move == '':
        move = input('>')
    move = move.lower().split()

    #if they type 'go' first
    if move[0] == 'go':
        #check if the move is allowed
        if move[1] in rooms [currentRoom]:
            #set the current room to the new room
            currentRoom = rooms [currentRoom][move[1]]
            #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get':
        #if the move is allowed
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to the inventory
            inventory.append(move[1])
            #display a movement complete message
            print(move[1] + ' got!')
            #delete the item from the room
            del rooms[currentRoom]['item']
        #otherwise (the item is not there to get)
        else:
            print('Can\'t get ', move[1], ' !')

# player wins if they get to the garden with a key and the magic
    if currentRoom == 'Garden' and 'key' in inventory and 'magic' in inventory:
        print('You escaped the house...\n YOU WON!')
        break
# player loses if the enter a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you...\n GAME OVER')
        break

