import random
n = int(input("please enter number of Rounds :"))
games_cnt_team1 = int(input("please enter number of Team1 games (3 or 4) :"))
games_cnt_team2 = 7 - games_cnt_team1
probability_win_home_in = float(input("please enter probability of team1 in home (between 0,1) :"))
probability_win_home_out = float(input("please enter probability of team1 out of home (between 0,1) :"))
values = [1, 2]
probabilities_in = [probability_win_home_in, 1 - probability_win_home_in]
probabilities_out = [probability_win_home_out, 1 - probability_win_home_out]

cnt_team1 = 0
cnt_team2 = 0
for i in range(1, n+1):
    wins_team1 = 0
    wins_team2 = 0
    for j in range(1, 9):
        if wins_team2 == 4:
            cnt_team2 = cnt_team2 + 1
            print("team 2")
            break
        elif wins_team1 == 4:
            cnt_team1 = cnt_team1 + 1
            print("team 1")
            break
        which_ground = random.randint(1, 2)
        if which_ground == 1:
            buff = random.choices(values, probabilities_in)[0]
            if buff == 1:
                wins_team1 = wins_team1 + 1
            else:
                wins_team2 = wins_team2 + 1
        else:
            buff = buff = random.choices(values, probabilities_out)[0]
            if buff == 1:
                wins_team1 = wins_team1 + 1
            else:
                wins_team2 = wins_team2 + 1
print("*********************************************")
print("Team 1 wons " + str(cnt_team1) + " times !")
print("Team 2 wons " + str(cnt_team2) + " times !")
print("*********************************************")
print("Probability of Team1 is : "+str(cnt_team1/n))
print("Probability of Team2 is : "+str(cnt_team2/n))