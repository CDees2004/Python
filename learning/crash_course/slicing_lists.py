players = ['charles', 'martina', 'michael', 'florence']
print(players[0:3])

# Everything until fifth item
print(players[:4])
# Everthing third item and after
print(players[2:])

# Can loop through a subset of elements with slice
for player in players[:3]:
    print(player.title())