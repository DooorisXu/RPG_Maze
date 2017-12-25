def instructions():
    print("RPG Game \n ======= \n Commands: \n go[direction] \n get[item]")


def status():
    #print the current status
    print('----------------------------')
    print('You are in the '+currentRoom)

    #print the current inventory
    print('Inventory: ', str(inventory))

    #print an item if exists
    if "item" in rooms [currentRoom]:
        print('You see a '+rooms[currentRoom]['item'])
    print('----------------------------')

#initialize the inventory array
inventory = []

#link one room to another
rooms = {
        'Hall': {
            'south': 'Kitchen',
            'west': 'Dining Room',
            'item': 'key'
        },
        'Kitchen': {
            'north': 'Hall',
            'south': 'Basement',
            'item': 'ration',
            'item': 'knives'
        },
        'Dining Room': {
            'east': 'Hall',
            'item': 'piano'
        },
        'Basement': {
            'north': 'Kitchen'
        }
}

#start the player in the Hall
currentRoom = 'Hall'

instructions()

#loop infinitely
while True:
    status()
#get the player's move
#.split breaks it up into an list array
#eg: typing 'go east' would give the list ['go','east']

move = ''
while move == '':
    move = input ('>')
    # player loses if the enter a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you...\n GAME OVER')
        break

move = move.lower().split()

#if they type 'go' first
if move[0] == 'go':
    #check if the move is allowed
    if move [1] in rooms [currentRoom]:
        #set the current room to the new room
        currentRoom = rooms [currentRoom][move[1]]
        #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

#if they type 'get' first
if move [0] == 'get':
    #if the move is allowed
    if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
        #add the item to the inventory
        inventory += move[1]
        #display a movement complete message
        print (move[1] + ' got!')
        #delete the item from the room
        del rooms[currentRoom]['item']
    #otherwise (the item is not there to get)
    else:
        print('Can\'t get ', move[1], ' !')




