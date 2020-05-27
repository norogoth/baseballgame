from random import randint
exec(open("./player_dict.py").read())
exec(open("./bb_data.py").read())

# use the "./" if it is in the same directory. The "." means "current directory"



# BASE ADVANCEMENT BEGINS=======================================================================================
single = 1
double = 2
triple = 3
home_run = 4
whose_on_first = [0, 0, 0]
player_pos_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
player_pos_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
player_pos = [player_pos_1, player_pos_2]
runners_on_base = 0
team_up = 0
runs = [0, 0]
batter_up = 0
runs_this_inning = 0
hit_type_list = ["none", "single", "double", "triple", "home run"]

print(player_pos[team_up])

def main():

    team1 = ["yelich", "cain", "shaw", "aguilar", "braun", "arcia", "perez", "pina", "villar"]
    team2 = ["baez", "rizzo", "contreras", "zobrist", "almora", "heyward", "schwarber","russell", "bryant"]
    return [team1,team2]

def set_bases():
    if 3 in player_pos[team_up]:
        whose_on_first[2] = 1
    else:
        whose_on_first[2] = 0
    if 2 in player_pos[team_up]:
        whose_on_first[1] = 1
    else:
        whose_on_first[1] = 0
    if 1 in player_pos[team_up]:
        whose_on_first[0] = 1
    else:
        whose_on_first[0] = 0

set_bases()

# NEW AND EPIC FUNCTION
def bases_advance(number_of_bases, positions, index, type):
    if type=="hit":
         for g in reversed(range(1, 4)):
            for f in range(0, 9):
                if g == positions[f]and type=="hit":
                    runners_advance=randint(number_of_bases, number_of_bases + 2)
                    positions[f] = positions[f] + runners_advance
                    if runners_advance==number_of_bases+1:
                        print(both_team_lineup_labels[team_up][f], " runs extra bases!")
                        if positions[f]>=4:
                            print("And he runs all the way home!")
    elif type=="walk":
        for g in range(1,4):
            if whose_on_first[g-1]!=0:
                for f in range(0,9):
                    if g==positions[f]:
                        positions[f] = positions[f] + number_of_bases
                        if g+1 not in positions:
                            break
    positions[i]=1
        # global i
        # print(player_pos[team_up])
    positions[index] = number_of_bases
    # print(player_pos[team_up])
    # for RUNS
    for f in range(0, 9):
        if positions[f] >= 4:
            runs[team_up] = runs[team_up] + 1
            # print("runs are ",runs)
            positions[f] = 0

    set_bases()

# BASE ADVANCEMENT BEGINS=======================================================================================

print("= = = = = = =\nPLAY BALL!\n= = = = = = =\n\n")
i = 0
i2 = 0
batter_up = i
outs = 0
team_up = 0
randindex = 0


# RUN INNINGS FUNCTION

def run_inning():
    outs=0
    global batter_up
    global i
    global inning
    global whose_on_first
    global team_up
    inning_index = [0, 0]
    fix_skip_error = 0
    win = 0
    teams = main()

    if whose_on_first[0]==1 and whose_on_first[1]==1 and whose_on_first[2]==1:
        print("Bases loaded.")

    while outs < 3:

        # if outs!=0:
        # print("team up is ",team_up," so we should have,", both_team_lineup_labels[team_up][i])
        # print("This is a test of whose on first. whose on first is ",whose_on_first, whose_on_first[0], whose_on_first[1], whose_on_first[2])

        # if 1==1:
        # print("i is",i)
        # print("randinex is", randindex)
        # print("bb is",bb)
        # print("bb_random[randindex is",bb_random[randindex])
        # print("bothteamlineups team up i pa is ",players[teams[team_up][i]][pa],"\n")
        print("\n     ", whose_on_first[1], "\n\n", whose_on_first[2], "       ", whose_on_first[0], "\n\n")
        bbrand=randint(1,1000)
        if (bbrand / 1000) < (players[teams[team_up][i]]["bb"] / players[teams[team_up][i]]["pa"]):
            print("{} gets a walk".format(both_team_lineup_labels[team_up][i]))
            bases_advance(1, player_pos[team_up], i, "walk")
        else:
            rh = randint(1, 1000)
            if rh <= players[teams[team_up][i]]["avg"]:
                hit_type = randint(1, players[teams[team_up][i]]["ab"])
                if 1 <= hit_type <= all_player_bounds[i][0][0]:
                    player_base_pos[i] = 2
                    print("{} gets a DOUBLE!".format(both_team_lineup_labels[team_up][i]))
                    bases_advance(2, player_pos[team_up], i,"hit")
                elif all_player_bounds[i][0][0] < hit_type <= all_player_bounds[i][0][1]:
                    player_base_pos[i] = 3
                    print("A very rare TRIPLE from {}".format(both_team_lineup_labels[team_up][i]))
                    bases_advance(3, player_pos[team_up], i,"hit")
                elif all_player_bounds[i][0][1] < hit_type <= all_player_bounds[i][0][2]:
                    # player_position[i]=4
                    print("{} hits a HOME RUUUUUUUN!!!!!!".format(both_team_lineup_labels[team_up][i]))
                    bases_advance(4, player_pos[team_up], i,"hit")
                elif all_player_bounds[i][0][2] < hit_type <= players[teams[team_up][i]]["ab"]:
                    print("{} hits a single.".format(both_team_lineup_labels[team_up][i]))
                    bases_advance(1, player_pos[team_up], i,"hit")
                else:
                    print(
                        "Error. The value given exceeds the range you need for this function. The hit_type was {}".format(
                            hit_type))
                    print("my ranges are ", all_player_bounds[i][0], )
            else:
                out_random = randint(0, 6)
                if out_random == 0:
                    print(
                        "strike out for {}. That's out number {}".format(both_team_lineup_labels[team_up][i], outs + 1))
                if out_random in range(1, 3):
                    print("{} hits a fly ball for out {}".format(both_team_lineup_labels[team_up][i], outs + 1))
                if out_random == 3:
                    print("{}'s line drive caught by the shortstop for out {}.".format(
                        both_team_lineup_labels[team_up][i], outs + 1))
                if out_random == 4:
                    print(
                        "{} hits a blooper to first for out {}.".format(both_team_lineup_labels[team_up][i], outs + 1))
                if out_random == 5:
                    print("{} gets out number {} on a grounder.".format(both_team_lineup_labels[team_up][i], outs + 1))
                if out_random == 6:
                    print("{} hits and infield fly caught by the catcher for out {}.".format(
                        both_team_lineup_labels[team_up][i], outs + 1))
                outs = outs + 1
            if i <= 2 and outs == 3:
                pitcher_message = randint(0, 2)
                if pitcher_message == 0:
                    print("\n Great inning for the pitcher here.")
                if pitcher_message == 1:
                    print("\n The pitcher is really doing his job well.")
                if pitcher_message == 2:
                    print("\n Great performance from", team_names[team_up], "'s pitching.")
        if outs == 3:
            inning = inning + 1
            whose_on_first = [0, 0, 0]
            player_pos[0] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            player_pos[1] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            # print("the inning is ",inning)
            if inning == 18 and runs[0] != runs[1]:
                if runs[0] > runs[1]:
                    print(team_names[0].upper(), "WIN!")
                    print("\nThe final score is\n", team_names[0], runs[0], "\n", team_names[1], runs[1])
                    win = 1
                    print("==========================\nEND OF GAME\n==========================")
                if runs[1] > runs[0]:
                    print(team_names[1].upper(), " WIN THE GAME!")
                    print("\nThe final score is\n", team_names[0], runs[0], "\n", team_names[1], runs[1])
                    win = 1
                    print("==========================\nEND OF GAME\n==========================")
            if win == 0:
                print("\nNow we head to the {}. The score is\n".format(inning_list[inning]), team_names[0], runs[0],
                      "\n", team_names[1], runs[1])
                print("==========================\n", inning_list[inning], "\n==========================")
            # print (runs)
            if team_up == 0:
                team_up = 1
                inning_index[0] = i
            else:
                team_up = 0
                inning_index[1] = i
                i = 0

            # print("the TEAM UP is ",team_up)

        # print("\n")
        if i <= 7:
            i = i + 1
        else:
            i = 0
        if outs == 3:
            i = 0

team_up=0
while inning < 18:
    run_inning()
    outs = 0
while runs[0] == runs[1]:
    run_inning()
