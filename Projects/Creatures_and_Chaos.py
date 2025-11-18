#Imports
import random

#Variable definitions
MAP_SIZE = 5

player_x = 0
player_y = 0

player_hp = 20
gold = 0
potions = 0

room_types = ["fun", "merchant", "monster", "treasure"]

dungeon = []

monsters = ["GenericBeast", "Iron Worm", "Evil Clippy the Crab", "Hammertail", "Crazy Cuboid"]#

SillyStuff = ["You see an empty room. *Chilly Silence*",
              "You see a strange green 2 legged lizard thingy singing karaoke in a screechy voice to a red drill tail lizard thingy and a blue dorsal fin lizard thingy. \"Spongebob Squarepants, Spongebob Squarepants...\"",
              "You see a sleeping dragon. You carefully tiptoe past it.",
              "You step on a pressure plate and an axe on a rope swings at you. Luckily, you dodge it...",
              "You see a boxing ring with a tied up person, a nervous person, and a chicken. There is a crate above the chicken. You run out of the room before someone makes a joke aout chicken jockeys.",
              "You see Mickey Mouse petting his dog.",
              "You see a mine full of strange red 2 leg drill tail lizards thingies mining rare minerals and crystals."]
names = ["Bob", "Joe", "Mary", "N00mk1@w", "Bonniebunny777", "Silly Billy"]
for i in range(MAP_SIZE):
    row = []
    for j in range(MAP_SIZE):
        row.append(random.choice(room_types))
    dungeon.append(row)

dungeon[0][0] = "fun"



def print_position():
    print(f"\nYou are now at room ({player_x + 1}, {player_y + 1})")#Change Xy display
    room = dungeon[player_y][player_x]
    print(f"The room is: {room}")
    if room == "monster":
        start_battle()
    elif room == "treasure":
        collect_treasure()
    elif room == "merchant":
        merch()
    else:
        sillything = SillyStuff[random.randint(0, len(SillyStuff)-1)]
        print(sillything)

def move(direction):
    global player_x, player_y
    if direction == "S" and player_y > 0:
        player_y -= 1
    elif direction == "W" and player_y < MAP_SIZE - 1:
        player_y += 1
    elif direction == "D" and player_x < MAP_SIZE - 1:
        player_x += 1
    elif direction == "A" and player_x > 0:
        player_x -= 1
    else:
        print("You can't go that way!")
        return
    print_position()

def collect_treasure():
    global gold, potions
    t = random.choice(["gold", "potion"])
    if t == "gold":
        amount = random.randint(5, 20)
        gold += amount
        print(f"You found {amount} gold! Total gold: {gold}")
    else:
        potions += 1
        print(f"You found a healing potion! Total potions: {potions}")
    dungeon[player_y][player_x] = "fun"

def start_battle():
    global player_hp, gold
    monster_hp = random.randint(5, 15)#Choose HP
    mtype = monsters[random.randint(0, len(monsters)-1)] #Choose monster
    print(f"\nA(n) {mtype} appears with {monster_hp} HP!")
    
    while monster_hp > 0 and player_hp > 0:
        action = input("Attack (A), Run (R), or Use Potion (P)? ").upper()
        
        if action == "A":
            dmg = random.randint(3, 7)
            monster_hp -= dmg
            print(f"You hit for {dmg}! {mtype} HP: {max(monster_hp,0)}")
            
            if monster_hp <= 0:
                print(f"You defeated the {mtype}!")
                print(f"You got {abs(monster_hp) + 2} gold!")
                gold += monster_hp
                dungeon[player_y][player_x] = "fun"
                return
            
            mdmg = random.randint(2, 6)
            player_hp -= mdmg
            print(f"The {mtype} hits you for {mdmg}! Your HP: {player_hp}")
            
            if player_hp <= 0:
                print(f"You died with {gold} gold. Game over.")
                exit()
        
        elif action == "R":
            print("You run away!")
            return
        
        elif action == "P":
            use_potion()
        
        else:
            print("Invalid action.")

def use_potion():
    global player_hp, potions
    if potions == 0:
        print("You have no potions!")
        return
    heal = random.randint(5, 12)
    player_hp += heal
    potions -= 1
    print(f"You heal for {heal}! HP: {player_hp}, Potions left: {potions}")

def merch():#Merchants
    global gold, potions#IMPORTANT!!!
    merchantname = names[random.randint(1, 5)]
    price = random.randint(2, 10)
    print(f"A merchant named {merchantname} walks to you and offers you a healing potion for {price} gold")
    wannit = input("Accept or Decline?(a, other)").upper()
    if wannit == "A":
        if gold >= price:
            potions += 1
            gold = gold - price
            print(f"You buy the potion! Total potions: {potions}")
        else:
            print("You don't have enough gold!")
    else:
        print(f"You decline {merchantname}'s offer.")

def showstats():
    print(f"Your HP: {player_hp} Your Potions: {potions} Your Gold: {gold}")

print("Welcome to Creatures & Chaos!")
print("Move with W A S D.")
print("Press I to show stats.")
print(f"Your HP: {player_hp}")
print_position()

while True:
    command = input("\nWhat do you do? ").upper()
    if command in ["W", "A", "S", "D"]:
        move(command)
    elif command == "I":
        showstats()
    else:
        print("Invalid command!")
