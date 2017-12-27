# this is a RPG game without graphics
# Star Wars edition!

def instructions():
    print("\t==================================================== \n\tCommands: \n\tgo[direction] \n\tget[item]")
    print('\tLong long ago, in a galaxy far far away \n\tThe Empire is building another Death Star')
    print('\tTo restore the peace and order to the galaxy, \n\tthe rebellion must destory the Death Star')
    print('\tYou need to go to the central control room \n\twith the code breaker and the mechanic')
    print('\t to destroy the Death Star')
    print('\tIf you run into Darth Vedar\n\tyou lose the game ')
    print('\t====================================================')


def status():
    #print the current status
    print('\t----------------------------')
    print('\tYou are in the '+currentRoom)

    #print the current inventory
    print('\tInventory: ', list(inventory))

    #print an item if exists
    if "item" in rooms[currentRoom]:
        print('\tYou see a '+rooms[currentRoom]['item'])
    print('\t----------------------------')

#initialize the inventory array
inventory = []

#link one room to another
rooms = {
        'Training Deck': {
            'north': 'Armery',
            'east': 'Control Room',
            'south': 'Clinic'
        },
        'Clinic': {
            'north': 'Training Deck',
            'east': 'Power Generator',
            'item': 'Darth Vedar'
        },
        'Armery': {
            'south': 'Training Deck',
            'west': 'Testing Room'
        },
        'Testing Room': {
            'east': 'Armery',
            'item': 'mechanic'
        },
        'Power Generator': {
            'north': 'Control Room',
            'west': 'Clinic',
            'item': 'code breaker'
        },
        'Control Room': {
            'south': 'Power Generator',
            'west': 'Training Deck'
        }
}

#start the player in the Hall
instructions()
currentRoom = 'Training Deck'

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
    if currentRoom == 'Control Room' and 'mechanic' in inventory and 'code breaker' in inventory:
        print('You estroyed the death star...\n YOU WON!')
        break
# player loses if the enter a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('Darth Vedar has got you...\n GAME OVER')
        break

