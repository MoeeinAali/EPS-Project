import random

# Number of simulation
n = 100000
# Range
m = 13
# Keep track of "successes"
num_success = 0

file = open("Q2_Output.txt", "w")
file.truncate(0)
def select_three_random_numbers():
    numbers = random.sample(range(1, m + 1), 3)
    return numbers

for i in range(1, n + 1):
    random_numbers = select_three_random_numbers()
    file.write(str(random_numbers[0])+" "+str(random_numbers[1])+" "+str(random_numbers[2])+"\n")
    if abs(random_numbers[0] - random_numbers[1]) < random_numbers[2] and random_numbers[2] < (random_numbers[0] + random_numbers[1]):
        num_success = num_success + 1
        file.write("Success "+str(num_success)+"!"+"\n")


# Estimated probability
file.write("\n\nnum_success:" + str(num_success)+"\n")
print("\n\nnum_success:" + str(num_success))
file.write("Estimated probability:" + str(num_success / n))
print("Estimated probability:" + str(num_success / n))

# E[x] = 0.45