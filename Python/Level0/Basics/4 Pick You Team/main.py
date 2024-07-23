# Notes:
# https://www.notion.so/4-Pick-You-Team-4930034ac06f4cbe8b2df35fa6093fcf

from random import choice
"""
players = [
    'Harry', 'John', 'William', 'Jack', 'James', 'Alex', 'Charles', 'Michael',
    'Daniel'
]
"""

players = []
file = open('./4 Pick You Team/players.txt', 'r')
players = file.read().splitlines()

# print(players)
# print(players[0])
# print(players[1])
# print(len(players))

team_A = []
team_B = []


def pick_player(players, team):
    player = choice(players)
    players.remove(player)
    if player not in team:
        team.append(player)


while len(players) != 0:
    pick_player(players, team_A)

    if players == []:  # Or len(players) == 0
        break

    pick_player(players, team_B)
"""
while len(players) != 0:
    player_A = choice(players)
    #print(player_A)
    players.remove(player_A)

    if player_A not in team_A:
        team_A.append(player_A)
    #print('Players left:', players)

    if players == []:  # Or len(players) == 0
        break

    player_B = choice(players)
    #print(player_B)
    players.remove(player_B)

    if player_B not in team_B:
        team_B.append(player_B)
    #print('Players left:', players)
"""

print('Team A:', ','.join(team_A))
# print('Team A:', team_A)
print('Team B:', ','.join(team_B))
# print('Team B:', team_B)
