

def display_information():
    print("information for one player (keys and valus0")
    print(players["yelich"])

    print("all the players")
    for player in players:
        print(player)

    print("all the data without the player names")
    for player_data in players.values():
        print(player_data)

    print("all the data for a single player without the keys (only the numbers");
    data = players["cain"]
    print(",".join([str(x) for x in data.values()]))

    print("Yelichs home runs", players["yelich"]["hr"])

#display_information()

def main():
    team1 = ["yelich", "cain", "shaw", "aguilar", "braun", "arcia", "perez", "pina", "villar"]
    team2 = ["baez", "rizzo", "contreras", "zobrist", "almora", "heyward", "schwarber","russell", "bryant"]
    bases = []
    struck_out = []

    teams = [team1, team2]