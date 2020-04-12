import sys

list_of_players = {}


def register(player_name, player_info, opponent, my_score, his_score, proof):
    status = ""
    point = 0

    if my_score <= 0 and his_score <= 0:
        status = "Egalite"
        point = 1
    elif my_score <= 0:
        status = "Defaite"
        point = 0
    elif his_score <= 0:
        status = "Victoire"
        point = 3
    else:
        status = "Non fini"
        point = 0

    if opponent in player_info["games"]:
        sys.stderr.write(player_name + " and " + opponent + " played twice")
        exit(0)
    
    player_info["total_score"] += point
    player_info["goal_average"] += my_score - his_score
    player_info["games"][opponent] = {}
    player_info["games"][opponent]["result"] = status
    player_info["games"][opponent]["score"] = str(my_score) + " / " + str(his_score)
    player_info["games"][opponent]["proof"] = proof

with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if line is None or len(line) == 0:
            continue
        if line[0:2] == "//":
            continue

        s = line.split(" ")

        if len(s) == 2:
            list_of_players[s[0]] = {}
            list_of_players[s[0]]["job"] = s[1]
            list_of_players[s[0]]["total_score"] = 0
            list_of_players[s[0]]["goal_average"] = 0
            list_of_players[s[0]]["games"] = {}
        elif len(s) >= 4:
            if s[0] not in list_of_players:
                sys.stderr.write(s[0] + "is an unknown player")
                exit(0)
            elif s[0] not in list_of_players:
                sys.stderr.write(s[1] + "is an unknown player")
                exit(0)
            else:
                if len(s) == 4:
                    register(s[0], list_of_players[s[0]], s[1], int(s[2]), int(s[3]), None)
                    register(s[1], list_of_players[s[1]], s[0], int(s[3]), int(s[2]), None)
                elif len(s) == 5:
                    register(s[0], list_of_players[s[0]], s[1], int(s[2]), int(s[3]), s[4])
                    register(s[1], list_of_players[s[1]], s[0], int(s[3]), int(s[2]), s[4])
                else:
                    sys.stderr.write("Unknown line " + str(s))
                    exit(0)
        else:
            sys.stderr.write("Unknown line " + str(s))
            exit(0)


sorted_list_of_players = []

for player_name in list_of_players:
    sorted_list_of_players.append(player_name)

sorted(sorted_list_of_players)

# print(sorted_list_of_players)

import pprint as pp

# pp.pprint(list_of_players)


print('<table class="wikitable" border="1" style="text-align: center; width:90%">')

def print_header():
    s = "<tr><td></td><td>Joués /<br>Total</td>"

    for player_name in sorted_list_of_players:
        s += "<td>" + player_name + " (" + list_of_players[player_name]["job"] + ")</td>"

    s = s + "<td>Score</td><td>Goal Average</td></tr>"
    print(s)


print_header()


resorted_list_of_players = []

for player_name in list_of_players:
    resorted_list_of_players.append(player_name)
    
def key_func(player_name):
    player = list_of_players[player_name]
    
    # Sorts by points for players that played everything and by nick for other
    # I hate it
    #if len(player["games"]) == len(sorted_list_of_players) - 1:
    #    return (0, -player["total_score"], -player["goal_average"], "")
    #else:
    return (1, 0, 0, player_name.lower())


#resorted_list_of_players.sort()


for player_name in resorted_list_of_players:
    player = list_of_players[player_name]

    s = "<tr>"
    s += "<td>" + player_name + " (" + player["job"] + ")</td>"
    s += "<td>" + str(len(player["games"])) + " / " + str(len(sorted_list_of_players) - 1) + "</td>"

    for other_player_name in sorted_list_of_players:
        if other_player_name in player["games"]:
            s += "<td>"
            
            if other_player_name == player_name:
                s += "<em>N/A</em>"
            
            game = player["games"][other_player_name]

            if game["proof"] is not None:
                s += '[' + game["proof"] + ' '

            s += game["result"] + "<br>" + game["score"]
            
            if game["proof"] is not None:
                s += ']'
            
            s += "</td>"
        else:
            s += "<td></td>"


    s += "<td>" + str(player["total_score"]) + "</td><td>" + str(player["goal_average"]) + "</td></tr>"

    print(s)



print("</table>")

