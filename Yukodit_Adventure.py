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

if(character == "archer" or character == "Archer"):
  print("You chose the archer!")

elif(character == "knight" or character == "Knight"):
  print("You chose the knight!")

elif(character == "warrior" or character == "Warrior"):
  print("You chose the warrior!")

elif(character == "mage" or character == "Mage"):
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

  intelligence = int(input("\nWhat would you like your strength to be from 1 - 10?"))

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


#Finally give ask the user what their character's name is!
name = input("\nWhat are you going to call your character? ")

#Now tell the user the choices they have made.

print("\nYou have completed forming your character!")

print("\nTheir name is", name, ". They are a", character, "from the faction", faction)
print("\n\nNow you are ready to go adventuring!")


#Our next task is to use your creativity to create a story for our character.
#Using the print function, give the user some backstory about where their character is and what they are doing.
#Create a conflict or a mission that the character has to go on. 
#Use your variables like name and faction in the story to describe your character.
