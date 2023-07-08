# by of probability of win out of house
import random
import matplotlib.pyplot as plt


def func(probability_win_home_out):
    n = 1000
    games_cnt_team1 = 4
    games_cnt_team2 = 7 - games_cnt_team1

    probability_win_home_in = 0.9
    values = [1, 2]
    probabilities_in = [probability_win_home_in, 1 - probability_win_home_in]
    probabilities_out = [probability_win_home_out, 1 - probability_win_home_out]

    cnt_team1 = 0
    cnt_team2 = 0
    for i in range(1, n + 1):
        wins_team1 = 0
        wins_team2 = 0
        ground_team1 = 0
        ground_team2 = 0
        for j in range(1, 9):
            if wins_team2 == 4:
                cnt_team2 = cnt_team2 + 1
                break
            elif wins_team1 == 4:
                cnt_team1 = cnt_team1 + 1
                break
            which_ground = random.randint(1, 2)
            if ground_team2 == 3:
                if games_cnt_team1 == 4:
                    which_ground = 1
                else:
                    which_ground = 2
            if j == 1:
                which_ground = 2
            if which_ground == 1:
                ground_team1 = ground_team1 + 1
                buff = random.choices(values, probabilities_in)[0]
                if buff == 1:
                    wins_team1 = wins_team1 + 1
                else:
                    wins_team2 = wins_team2 + 1
            else:
                ground_team2 = ground_team2 + 1
                buff = buff = random.choices(values, probabilities_out)[0]
                if buff == 1:
                    wins_team1 = wins_team1 + 1
                else:
                    wins_team2 = wins_team2 + 1
    return cnt_team1 / n


for i in range(1, 400):
    x = random.randint(1, 100) / 100
    y = func(x)
    plt.plot(x, y)
    plt.scatter(x, y)

plt.xlabel('probability_win_home_in')
plt.ylabel('probability_win_team1')
plt.title('first game for team 2')
plt.grid(True)
plt.show()
