import time
import random

def print_pause(message_to_print):
  print(message_to_print)
  time.sleep(2)

def intro():
  print_pause("After a drunken night out with friends, you awaken the "
  "next morning in a thick, dank forest. Head spinning and "
  "fighting the urge to vomit, you stand and marvel at your new, "
  "unfamiliar setting. The peace quickly fades when you hear a "
  "grotesque sound emitting behind you. A slobbering orc is "
  "running towards you. You will:")

def first_choice(items):
  option_rock()

def second_choice(items):
  option_run()



def option_rock():
  list = ["A", "B" , "C"]
  print_pause ("\nThe orc is stunned, but regains control. He begins "
  "running towards you again. Will you:")
  print_pause("A. Run")
  print_pause("B. Throw another rock")
  print_pause("C. Run towards a nearby cave")
  print_pause("D. random choice")
  
  
  choice = input(">>> ")
  if choice == 'A':
    option_run()
  elif choice == 'B':
    print ("\nYou decided to throw another rock, as if the first "
    "rock thrown did much damage. The rock flew well over the "
    "orcs head. You missed. \n\nYou died!")
  elif choice == 'C':
    option_cave()
  
  else:
    print(" please enter A,B,C or D")
    option_rock()

list = ["A'", "B", "C"]

def option_cave():
  list = ["A'", "B", "C"]
  print_pause("\nYou were hesitant, since the cave was dark and "
  "ominous. Before you fully enter, you notice a shiny sword on "
  "the ground. Do you pick up a sword. Y/N?")
  choice = input(">>> ").upper()
  if 'y' in choice:
    sword = 1 #adds a sword
  else:
    sword = 0
  print_pause("\nWhat do you do next?")

  print_pause("A. Hide in silence")
  print_pause("B. Fight")
  print_pause("C. Run")
  print_pause ("D. random choice")
  
  choice = input(">>> ").upper()
  if choice == 'A':
    print ("\nReally? You're going to hide in the dark? I think "
        "orcs can see very well in the dark, right? Not sure, but "
        "I'm going with YES, so...\n\nYou died!")
  elif choice == 'B':
    if sword > 0:
        print ("\nYou laid in wait. The shimmering sword attracted "
          "the orc, which thought you were no match. As he walked "
          "closer and closer, your heart beat rapidly. As the orc "
          "reached out to grab the sword, you pierced the blade into "
          "its chest. \n\nYou survived!")
    else: #If the user didn't grab the sword
          print ("\nYou should have picked up that sword. You're "
          "defenseless. \n\nYou died!")
  elif choice == 'C':
        print ("As the orc enters the dark cave, you sliently "
        "sneak out. You're several feet away, but the orc turns "
        "around and sees you running.")
        option_run()
  elif choice == 'D':
    choice == random.choice(list)
        
  else:
        print("please enter A,B,C or D")
        option_cave() 

def option_run():
  print_pause("\nYou run as quickly as possible, but the orc's "
 "speed is too great. You will:")

  print_pause("""  A. Hide behind boulder
  B. Trapped, so you fight
  C. Run towards an abandoned town""")
  choice = input(">>> ").upper()
  if choice == 'A':
    print ("You're easily spotted. "
    "\n\nYou died!")
  elif choice == 'B':
    print ("\nYou're no match for an orc. "
    "\n\nYou died!")
  elif choice == 'C':
    option_town()
  else:
    print("please enter A,B,C")
    option_run()




def option_town():
  print_pause("\nWhile frantically running, you notice a rusted "
  "sword lying in the mud. You quickly reach down and grab it, "
  "but miss. You try to calm your heavy breathing as you hide "
  "behind a delapitated building, waiting for the orc to come "
  "charging around the corner. You notice a purple flower "
  "near your foot. Do you pick it up? Y/N")
  choice = input(">>> ").upper()
  if 'y' in choice:
    flower = 1 #adds a flower
  else:
    flower = 0
  print ("You hear its heavy footsteps and ready yourself for "
  "the impending orc.")
  time.sleep(1)
  if flower > 0:
    print_pause("\nYou quickly hold out the purple flower, somehow "
    "hoping it will stop the orc. It does! The orc was looking "
    "for love. "
    "\n\nThis got weird, but you survived!")
  else: #If the user didn't grab the sword
     print_pause("\nMaybe you should have picked up the flower. "
     "\n\nYou died!")











def choose_one(items):
  print_pause("Please enter 1 or 2: ")
  choice = input("1. Grab a nearby rock and throw it at the orc \n"
                  "2.Run away \n"
                 )
  while True:
    if choice == '1':
      first_choice (items)
    elif choice == '2':
      second_choice(items)
    else:
      print("please enter 1 or 2")
    again = input("would you like to play one more time?"
    "Please say 'yes' or 'no'.\n ")
    if 'y' in again:
      play_again()
    elif 'n' in again:
      print("see you later")
      return 0;

def play_again():
    play_game()

def play_game():
  items = []
  intro()
  choose_one(items)


play_game()








