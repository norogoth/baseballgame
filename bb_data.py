player = []
bb_random = []
hit_random = []
player_position = []
# below is index for player up
i = 0
inning = 0

pa = 0
ab = 1
bb = 2
h = 3
b2 = 4
b3 = 5
hr = 6
so = 7
sb = 8
avg = 9
obp = 10,

inning_list = ["Top of the 1st", "Bottom of the 1st", "Top of the 2nd", "Bottom of the 2nd", "Top of the 3rd",
               "Bottom of the 3rd", "Top of the 4th", "Bottom of the 4th"]
for e in range (9,55):
    if e%2==1:
        a=(e+1)//2
        message="top of the ",a,"th inning"
        "".join(str(x) for x in message)
        inning_list.append("".join(str(x) for x in message))
    elif e%2==0:
        a = (e + 1) // 2
        message = "bottom of the ",a,"th inning"
        "".join(str(x) for x in message)
        inning_list.append("".join(str(x) for x in message))

# stats team 1=(pa, ab, bb, h, b2, b3, hr, so, sb, avg, obp)
team_names = "the Brewers", "the Cubs"
# yelich should be 326 avg and cain 308
yelich = [651, 574, 68, 187, 34, 7, 36, 135, 22, 326, 402]
cain = [620, 539, 71, 166, 25, 2, 10, 94, 30, 308, 395]
shaw = [587, 498, 78, 120, 23, 0, 32, 108, 5, 241, 345]
aguilar = [566, 492, 58, 135, 25, 0, 35, 143, 0, 274, 352]
braun = [447, 405, 34, 103, 25, 1, 20, 85, 11, 254, 469]
arcia = [366, 348, 15, 103, 25, 1, 20, 87, 7, 236, 268]
perez = [334, 316, 17, 103, 11, 2, 9, 71, 11, 253, 290]
pina = [337, 306, 21, 77, 13, 2, 9, 62, 2, 252, 307]
villar = [279, 257, 19, 67, 10, 1, 6, 80, 14, 261, 315]

# stats team 2=(pa, ab, bb, h, b2, b3, hr, so, sb, avg, obp)
baez = [645, 606, 29, 176, 40, 9, 34, 167, 21, 290, 881]
rizzo = [665, 566, 70, 160, 29, 1, 25, 80, 6, 283, 376]
contreras = [554, 474, 53, 118, 27, 5, 10, 121, 4, 249, 339]
zobrist = [520, 455, 55, 139, 28, 3, 9, 60, 3, 305, 3780]
almora = [479, 444, 24, 127, 24, 1, 5, 83, 1, 286, 323]
heyward = [489, 440, 42, 119, 23, 4, 8, 60, 1, 270, 335]
schwarber = [510, 428, 78, 102, 14, 3, 26, 140, 4, 238, 356]
russell = [465, 420, 40, 105, 21, 1, 5, 99, 4, 250, 317]
bryant = [457, 389, 48, 106, 28, 3, 13, 107, 2, 272, 374]

player_lineup = [yelich, cain, shaw, aguilar, braun, arcia, perez, pina, villar]
player_lineup_opponent = [baez, rizzo, contreras, zobrist, almora, heyward, schwarber, russell, bryant]
player_lineup_label = ["yelich", "cain", "shaw", "aguilar", "braun", "arcia", "perez", "pina", "villar"]
player_lineup_label_opponent = ["baez", "rizzo", "contreras", "zobrist", "almora", "heyward", "schwarber", "russell",
                                "bryant"]
both_team_lineup_labels = [player_lineup_label, player_lineup_label_opponent]
# print(teams[1][1][0])

all_player_names = player_lineup_label + player_lineup_label_opponent
all_player_data = player_lineup + player_lineup_opponent

# some bit of ode to create a nested dictionary from our data structures
#import json
# d = {}
# for i in range(len(all_player_data)):
#     player_name = all_player_names[i]
#     d[player_name] = {}
#     data = all_player_data[i]
#     for j in range(len(stat_fields)):
#         d[player_name][stat_fields[j]] = data[j]
#
# print(json.dumps(d, indent=4))
# exit()

# teams[which team is up][which player is up][which stat is used]
# so you can do players[teams[team_up][i]][stat]

all_player_bounds = []
runs = 0
player_base_pos = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(100):
    bb_random.append(randint(1, 1000))
    hit_random.append(randint(1, 1000))
    # player_position.append(i)

for i in range(9):
    all_player_bounds.append([0])

for i in range(9):
    all_player_bounds[i][0] = player_lineup[i][b2], player_lineup[i][b2] + player_lineup[i][b3], player_lineup[i][b2] + \
                              player_lineup[i][b3] + player_lineup[i][hr], player_lineup[i][ab]
    # print(all_player_bounds[i])

# print that big list for hit chance boundaries
# print(all_player_bounds[0][0][4],"\n\n\n")