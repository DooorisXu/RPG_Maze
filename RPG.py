def instructions():
    #main menu
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

#initialize the inventory
inventory = []

#link one room to another
rooms = {
        'Hall':{
            'south' : 'Kitchen'
        },
        'Kitchen':{
            'north' : 'Hall'
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



