#Now we are going to begin to create a game
#First we must choose our character
#You can choose to be either a knight, warrior, mage, or archer
#First tell the user about the role playing game they are about to play
#Then ask the user which character they would like to be
#Then print the character they chose. If they didn't select the knight, mage, warrior or archer,
#give them an error and exit!

import sys, traceback #To use exit functions


#using if statements to get their character choices
#if their choice does not = the choices give them an error and exit
#When they pick a character, assign them a weapon that makes sense for their class

  
  
#Now we are going to pick the skills for our character!
#The potential skills are strength, speed, intelligence, and charisma
#Create these four variables and ask the user what their value should be 
#They should have a rating from 1-10, but there is a catch. You can only assign a total of 30 points spread among all four traits.

#So also create a variable called total_skill_points that will decrease everytime you assign them to a skill
#If they give the skills a rating that is not between 1 and 10, give them an error and exit!


#Now ask the user which faction they would like to represent
#Create four different factions for your game. Call them whatever you would like.
#Then ask the user which faction their character is apart of.


# Finally give ask the user what their character's name is!


# Now tell the user the choices they have made.


# Our next task is to use your creativity to create a story for our character. 
# Using the print function, give the user some backstory about where their character is and what they are doing. Create a conflict or a mission that the character has to go on. Use your variables like name and faction in the story to describe your character.

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

    
  # Continue the story, creating more battles and situations for the character
print(name, "continues exploring the forest, ready to take down whatever comes his way!")
