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