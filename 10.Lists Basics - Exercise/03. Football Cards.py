players_out = input().split(" ")

team_A_out = []
team_B_out = []

for p in players_out:
    team, player = p.split("-")
    if team == "A":
        team_A_out.append(player)
    else:
        team_B_out.append(player)
team_A_out = set(team_A_out)
team_B_out = set(team_B_out)
print(f"Team A - {11 - len(team_A_out)}; Team B - {11 - len(team_B_out)}")
if len(team_A_out) >= 5 or len(team_B_out) >= 5:
    print(f"Game was terminated")
