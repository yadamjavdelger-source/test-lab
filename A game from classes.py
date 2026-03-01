import random
import time 
def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def heal(self, me):
        random_heal = random.randint(1, 10)
        if me.hp <= 50:
            me.hp += random_heal
        print(f"{self.name} chose to heal themself")
        slow_print(f"Heal: {random_heal}")

        if me.hp >= 50:
            me.hp = 50
            print("Hp cannot exceed 50!")
        print(f"{me.name}'s Hp:",me.hp)
    def attack(self, enemy):
        random_atk = random.randint(5, 15)   
        enemy.hp -= random_atk
        print(f"{self.name} chose to attack")
        slow_print(f"{self.name}'s Damage: {random_atk}")
        print(f"{enemy.name}'s Hp - {enemy.hp}\n {enemy.name}'s Turn!")

    def is_alive(self):
        if self.hp <= 0:
            return False
        else:
            return True

def play():
    player_name = input("Please type your name:\n - ")
    p1 = Player(player_name, 50)
    p2 = Player("Usukhuu(bot)", 50)
    players = [p1,p2]           # keep forgetting that i created this...for what?
    start = int(input("Press '1' to make the computer start or press '2' to start yourself - "))


    


    if start == 1:
        active_player = p2    
        other = p1
    else:
        active_player = p1     
        other = p2 


    while True:
        if not active_player.is_alive():
            slow_print(f"Game Over! The loser is: {active_player.name}")
            break
        if active_player == p1:
            choice = input("Press '1' to attack or press '2' to heal - ")
            if choice == "1":
                active_player.attack(other)
            elif choice == "2":
                active_player.heal(active_player)
        else:
            bot_brain = [1, 2, 3]
            bot_choice = random.choice(bot_brain)
            if bot_choice == 1:
                p2.heal(p2)
            elif bot_choice == 2:
                p2.attack(p1)
              
            elif bot_choice == 3:
                if p2.hp <= 20:
                    p2.heal(p2)
                else:
                    p2.attack(p1)
                    
        active_player, other = other, active_player  # switch turns liek this
    
    restart = input("Play again? (y/n): ").lower()
    if restart == "y":
        slow_print("Gonna restart in\n" \
        "3...\n" \
        "2...\n" \
        "1...")
        play()
    else:
        slow_print("Thanks for playing")
    
    # while True:
    #     for loser in players:
    #         if not loser.is_alive():
    #             print(f"Game Over! The loser is: {loser.name}")
    #             return
        
        
    #     if start == 1:
    #        print(f"{players[0].name} starts!")
    #        p1.attack(players[1]) or p1.heal(players[0])
    #     if start == 2:
    #         choice_1 = input("Press '1' to attack or press '2' to heal - ")
    #         if choice_1 == "1":
    #             players[1].attack(players[0])
    #         elif choice_1 == "2":
    #             players[1].heal(players[1])
    #     restart = input("Play again? (y/n): ").lower()
    #     if restart == "y":
    #         print("Gonna restart in\n" \
    #     "3...\n" \
    #     "2...\n" \
    #     "1...")
    #         play()
    #     else:
    #         print("Thanks for playing") soooooooo this is where my stupidity ends, the very first assignment came into clutch when making branches likethis.... a = b, b = a go brrr

play()