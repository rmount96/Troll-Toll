from unit import Unit, Player, Troll
from item import Item, Potion
from menu import Menu
from subprocess import call
import os
def clear():
    call('clear' if os.name =='posix' else 'cls')

name = input("What is your name champion? ")
player = Player(name, [5,5])
invalid_choice = print("Guess again champion...")

enemies = [
    Unit("Orc", [4,4], 10, 5),
    Unit("Goblin", [6,6], 10, 2),
    Troll("Troll", [6,3])
]

items = [
    Item("Treasure", [7,3]),
    Potion("Health Potion", [3,3])
]

menu = ["Move up", "Move Down", "Move Left", "Move Right"]
sub_menu = ["Attack", "Sneak Past"]

def show_menu():
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")
    i += 2
    for item in player.inventory:
        print(f"{i}. Use {item.name}")
        i += 1

def show_menu2():
    for i in range(len(sub_menu)):
        print(f"\n{i+1}. {sub_menu[i]}")
    i += 2

def play_again():
    play = input("Would you like to play again? Y/N\n")
    if play == "Y":
        playing = True
        player.health = 15
        player.position = [5, 5]
        clear()
    else:
        playing = False

playing = True
counter = 15
clear()
while playing == True or counter != 0:
    
    print(player)
    print("""\t %s Turns Left 
    """ % counter)
    show_menu()
    
    try:
        action = int(input("\nWhat would you like to do, %s?\n\n" % player.name))
    except ValueError:
        print(invalid_choice)
        action = None
    clear()
    if action:
        if action == 1:
            player.move("up")
        elif action == 2:
            player.move("down")
        elif action == 3:
            player.move("left")
        elif action == 4:
            player.move("right")
        else:
            if action-4 <= len(player.inventory):
                player.inventory[action-5].use()
                print("\nYou feel your vitality increase!")
            elif action > len(menu):
                print(invalid_choice)

    counter -= 1
    
    if counter == 0:
        print("You've run out of turns! You lose!")
        play_again()   

    if player.health <= 0:
        print("Oh no! you have died...")
        play_again() 
    
    for enemy in enemies:
        if enemy.position == player.position:
            if enemy.name == "Troll":
                clear()
                show_menu2()
                print("\nThere's a sleeping troll guarding the treasure...")
                try:
                    encounter = int(input("I might be able to kill him before he wakes up! Or should I try to sneak past the Troll?\n"))
                except ValueError:
                    print(invalid_choice)
                    encounter = None
                
                if encounter == 1:
                    clear()
                    player.troll_encounter(enemy)
                    enemy.smash(player)
                if encounter == 2:
                    print("Phew... that was a close one.")
                    player.position = [7, 3] 
            
            else:    
                print("You've stumbled across %s!" % enemy.name)
                print("You attack!")
                player.attack(enemy)
                print("They attack back!")
                enemy.attack(player)

    for item in items:
        if item.position == player.position:
            if item.name == "Treasure":
                print("You found the treasure! You win!")
                counter = 15
                play_again()
            else:
                print(f"You have come across {item.name}")
                player.pickup_item(item)