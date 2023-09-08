import random

p = 0.6  # Probability of Won of Team1
n = 1000000  # Number of Matches
values = [1, 2]  # List of values
probabilities = [p, 1 - p]  # List of probabilities

wons_team1 = 0  # Counter of Wons of Team1
wons_team2 = 0  # Counter of Wons of Team2

for j in range(1, n + 1):
    team1 = 0
    team2 = 0
    for i in range(1, 9):
        if team1 == 4:
            wons_team1 = wons_team1 + 1
            break
        if team2 == 4:
            wons_team2 = wons_team2 + 1
            break

        buff = random.choices(values, probabilities)[0]
        if buff == 1:
            team1 = team1 + 1
        else:
            team2 = team2 + 1

print("Team 1 wons " + str(wons_team1) + " times !")
print("Team 2 wons " + str(wons_team2) + " times !")
print("*********************************************")
print("p = "+str(p))
print("Probability of Team1 is : "+str(wons_team1/n))
print("Probability of Team2 is : "+str(wons_team2/n))