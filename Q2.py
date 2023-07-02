import random

# Number of simulation
n = 10000
# Range
m = 13
# Keep track of "successes"
num_success = 0



def select_three_random_numbers():
    numbers = random.sample(range(1, m + 1), 3)
    return numbers

for i in range(1, n + 1):
    random_numbers = select_three_random_numbers()
    print(str(random_numbers[0])+" "+str(random_numbers[1])+" "+str(random_numbers[2]))
    if abs(random_numbers[0] - random_numbers[1]) < random_numbers[2] and random_numbers[2] < (random_numbers[0] + random_numbers[1]):
        print("Success ++")
        num_success = num_success + 1

# Estimated probability
print("num_success:" + str(num_success))
print("Estimated probability:" + str(num_success / n))

# E[x] = 0.145
