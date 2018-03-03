#Now we are going to begin to create a game
#First we must choose our character
#You can choose to be either a knight, warrior, mage, or archer
#First tell the user about the role playing game they are about to play
#Then ask the user which character they would like to be
#Then print the character they chose. If they didn't select the knight, mage, warrior or archer,
#give them an error and exit!

import sys, traceback #To use exit functions

print("This is a role playing game where you choose what type of character you would like to be. Your choices are: ")
print("\nKnight\nWarrior\nMage\nArcher")

character = input("\nWhich character would you like to be?") 


#using if statements to get their character choices
#if their choice does not = the choices give them an error and exit
#When they pick a character, assign them a weapon that makes sense for their class

if(character == "archer" or character == "Archer"):
  weapon = "Bow"
  print("You chose the archer!")

elif(character == "knight" or character == "Knight"):
  weapon = "Sword"
  print("You chose the knight!")
  
elif(character == "warrior" or character == "Warrior"):
  weapon = "Axe"
  print("You chose the warrior!")
  
elif(character == "mage" or character == "Mage"):
  weapon = "Wand"
  print("You chose the mage!")
  
else:
  print("You must select either the knight, warrior, mage, or archer! Program Error!")
  quit()
  
  
#Now we are going to pick the skills for our character!
#The potential skills are strength, speed, intelligence, and charisma
#Create these four variables and ask the user what their value should be 
#They should have a rating from 1-10, but there is a catch. You can only assign a total of 30 points spread among all four traits.

#So also create a variable called total_skill_points that will decrease everytime you assign them to a skill
#If they give the skills a rating that is not between 1 and 10, give them an error and exit!


print("\nNow we are going to assign your character some skills. The four skills are:")
print("\nStrength\nSpeed\nIntelligence\nCharisma")
print("\nYou have a total of 30 skill points to use amongst each skill. They can only range from 1 - 10.")

total_skill_points = 30  # variable to make sure they use a certain number of points


#loop to make sure skill points equals 0
while(total_skill_points > 0):
  
  strength = int(input("\nWhat would you like your strength to be from 1 - 10?"))
  
  #check that each input is 1 - 10 otherwise exit
  if(strength < 1 or strength > 10):
    print("\nInvalid skill rating. You can only choose a rating between 1 and 10. Program Error!")
    sys.exit(0)
  
  #subtract skill points used from total skill points
  total_skill_points = total_skill_points - strength
  
  print("\nSkill points left:" , total_skill_points)
  
  speed = int(input("\nWhat would you like your speed to be from 1 - 10?"))
  
  if(speed < 1 or speed > 10):
     print("\nInvalid skill rating. You can only choose a rating between 1 and 10. Program Error!")
     sys.exit(0)
  
  total_skill_points = total_skill_points - speed
  
  print("Skill points left:" , total_skill_points)
  
  intelligence = int(input("\nWhat would you like your intelligence to be from 1 - 10?"))
  
  
  if(intelligence < 1 or intelligence > 10):
      print("Invalid skill rating. You can only choose a rating between 1 and 10. Program Error!")
      sys.exit(0)
  
  total_skill_points = total_skill_points - intelligence
  
  print("\nSkill points left:" , total_skill_points)
  
  charisma = int(input("\nWhat would you like your charisma to be from 1 - 10?"))
  
  if(charisma < 1 or charisma> 10):
      print("Invalid skill rating. You can only choose a rating between 1 and 10. Program Error!")
      sys.exit(0)
  
  total_skill_points = total_skill_points - charisma
  
  if(total_skill_points!= 0):
    print("\nYou didn't allocate all your skill points! Try again!")
    skill_points = 30
  
print("\nYou have " , total_skill_points, "skill points left.")
print("Your final skill values are:")
print("Strength: " , strength)
print("Speed: ", speed)
print("Intelligence: " , intelligence )
print("Charisma: " , charisma)

#Now ask the user which faction they would like to represent
#Create four different factions for your game. Call them whatever you would like.
#Then ask the user which faction their character is apart of.

print("\nThere are four factions in the world. Their names are Capricorns, Libras, Gemenis and Leos!")

faction = input("\nWhich faction would you like to be in?")

if (faction == "capricorns" or faction == "Capricorns"):
  print("\nYou chose the Capricorns!")
  
elif (faction == "Libras" or faction == "libras"):
  print("\nYou chose the Libras!")
  
elif(faction == "Gemenis" or faction == "gemenis"):
  print("\nYou chose the Gemenis!")
  
elif(faction == "Leos" or faction == "leos"):
  print("\nYou chose the Leos!")
  
  #error for invaliid input
else:
  print("\nYou must select either the Capricorns, Libras, Gemenis or Leos! Error!")
  sys.exit(0)


# Finally give ask the user what their character's name is!
name = input("\nWhat are you going to call your character? ")

# Now tell the user the choices they have made.

print("\nYou have completed forming your character!")

print("\nTheir name is", name, ". They are a", character, "from the faction", faction)
print("\n\nNow you are ready to go adventuring!")


# Our next task is to use your creativity to create a story for our character. 
# Using the print function, give the user some backstory about where their character is and what they are doing. Create a conflict or a mission that the character has to go on. Use your variables like name and faction in the story to describe your character.

print("\n\nOur guy", name, "has got some adventuring to do. He is on his way to the forbidden forest in search of his lost iPhone 4s. The only problem is this forest is filled with potential threats like goblins and ghouls. His mission is to find his lost phone, eliminate these threats, and make it home before Jeopardy. The forbidden forest awaits!\n\n")

#In order to have RPG elements to our game, we need to create some enemies. Please create 3 enemy types. They each should have different names. And they should have properties such as health power, attack power, and a level. Lets start our goblin at level 1. A good data structure to use would be a dictionary! Here is an example how to use it:

# pizza = {'Size': "large", 'Cheese': "Mozzarella", "Topping 1": "Pepperoni", "Price": 14.99}

enemy_1 = {'Enemy': 'Goblin', 'HP': 20, 'AP' : 5, 'Level': 1}

enemy_2 = {'Enemy': 'Wolf', 'HP': 25, 'AP': 5, 'Level': 1}

enemy_3 = {'Enemy': 'Badger', 'HP': 15, 'AP': 7, 'Level': 1}

# Now that we have experience with the dictionary data structure, lets create a dictionary for our character! First calculate their attack power by making it equal to their strength.Then calculate their health power by  multiplying their speed by 10.

health_power = speed * 10
attack_power = strength 


# Now that we have those important properties, create a dictionary for your character using all the information that we know about them! The properties should be name, faction, character, health power, attack power, strength, speed, intelligence, and charisma.

player_character = {'Name': name, 'Faction': faction, 'Class': character,'Weapon': weapon, 'AP': attack_power, 'HP': health_power, 'Strength': strength, 'Speed': speed, 'Intelligence': intelligence, 'Charisma': charisma}


# Create a scenario where an enemy attacks your character!

print("Your character is strolling through the forest with their", weapon, " in hand. When suddenly a ", enemy_1['Enemy'], " comes jumping from the bushes! A battle commences!")

# The enemy should attack your character first, each time doing the amount of damage that is equal to their attack power. Each time they attack, your health power should go down by that amount. Then your character should attack, using the same scenario. Your attack power should lower that HP by that amount. The fight ends when either character has no more HP. 

while player_character['HP'] > 0 or enemy_1['HP'] > 0:
  print("Goblin attack!\n")
  player_character['HP'] = player_character['HP'] - enemy_1['AP']
  print(name, " attack!")
  
  print("Enemy HP:", enemy_1['HP'])
  print("Player HP:", player_character['HP'])
  enemy_1['HP'] = enemy_1['HP'] - player_character['AP']
  
  if enemy_1['HP'] <= 0:
    print("The ", enemy_1["Enemy"], " has been defeated! ", player_character["Name"], " lives another day!")
    break
    
  if player_character['HP'] <= 0:
    print("You have been defeated! Game Over!")
    sys.exit(0)
    
  # Continue the story, creating more battles and situations for the character
print(name, "continues exploring the forest, ready to take down whatever comes his way!")
