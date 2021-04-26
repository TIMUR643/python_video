import random

player_name = input('Your enemy is Ghost. Enter player name: ')

while True:
    if player_name == "Ghost":
        player_name = input('Your name is the same as enemy name. Enter another player name: ')
    else:
        break

player = {"name": player_name, "health": random.randint(50, 100), "damage": random.randint(5, 30)}
enemy = {"name": "Ghost", "health": random.randint(50, 100), "damage": random.randint(5, 30)}

print(f'Player {player["name"]}: health is {player["health"]}, damage is {player["damage"]}')
print(f'Enemy {enemy["name"]}: health is {enemy["health"]}, damage is {enemy["damage"]}')
input('Press Enter to start ')

def attack(attacker, villain):
    print(f'{attacker["name"]} attacks')
    villain["health"] -= attacker["damage"]
    print(f'{villain["name"]} was hit by {attacker["damage"]}')
    if villain["health"] <= 0:
        print(f"{villain['name']}'s health is now 0")
        print(f'{attacker["name"]} wins!')
    else:
        print(f"{villain['name']}'s health is now {villain['health']}")

while player["health"] > 0 and enemy["health"] > 0:
    attacker = int(input('Who attacks? (1 - player, 2 - enemy) '))
    if attacker == 1:
        attack(player, enemy)
    elif attacker == 2:
        attack(enemy, player)
    else:
        print('Invalid entry!')
else:
    print('The End')
