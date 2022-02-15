# define enemy
class Enemy:
    def __init__ (self,name,enemy_weapons):
        self.name = name
        self.enemy_weapons = enemy_weapons
        self.number_of_lives = 3
    def weapons_count(self):
        return self.enemy_weapons
    def attack(self):
        print("Ouch!")
        self.number_of_lives = self.number_of_lives - 1
        if self.enemy_weapons > 0:
            self.enemy_weapons = self.enemy_weapons - 1
    def checkLife(self):
        return(self.number_of_lives)

import random

# If the player opts for 9 or more weapons he is guaranteed to win

rewards_list=["King of the world","Emperor","King","Diamond","Emerald","Platinum",\
              "Gold","Silver","Bronze"]
reward=""
player_weapons = int(input("How many weapons do you want? "))
if player_weapons < 9:
    reward=rewards_list[player_weapons]
    reward_info="You have opted for "+reward+" level"
    achieved_info="You have achieved "+reward+" level"
else:
    reward_info="You have opted out of rewards"
    achieved_info="No reward this time"
print(reward_info)


# Loops through a list of enemies.
# Each enemy will be given a random number of weapons (between 0 and 3).
# Every time the player confronts an enemy the weapons count of both the player
# and the enemy will be reduced by 1. The player must have at least the same
# number of weapons as all the enemies combined to complete the game.
enemy_list=['enemy1','enemy2','enemy3']
retired = False
defeated = False
enemies_beaten = 0
for foe in enemy_list:
    if retired or defeated:
        break
    enemy_weapons = random.randint(0,3)
    enemy=Enemy(foe,enemy_weapons)
    print("Created " + foe)
    while True:
        print("You have " + str(player_weapons)+ " weapons remaining")
        answer=""
        while answer not in('Y','N'):
           answer = input("Do you wish to continue? (Y or N) ")
        if answer == "N":
            print("Player retires")
            retired = True
            break
        current_enemy_weapons = enemy.weapons_count()
        if current_enemy_weapons > player_weapons:
            print("Player has less weapons than enemy")
            print("Player loses")
            defeated = True
            break
        # if the current enemy has no weapons left you don't have to use
        # one, as a weaponless player will always defeat a weaponless enemy
        if current_enemy_weapons > 0 and player_weapons > 0:
            player_weapons = player_weapons - 1
        enemy.attack()
        lives_count = enemy.checkLife()
        if lives_count > 1:
            print(str(lives_count)+ " lives remaining")
        elif lives_count == 1:
            print("Only " + str(lives_count)+ " life remaining")
        else:
            print(foe +" is dead")
            enemies_beaten = enemies_beaten + 1
            break
if defeated:
    print("Better luck next time")
elif retired:
    print("Enemies defeated = "+str(enemies_beaten))
else:
    print("You have destroyed all the enemies")
    print(achieved_info)
