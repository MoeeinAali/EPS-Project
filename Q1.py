import random

# number of simulations
n = 100000
# number of flips in each simulation
n_flips = 10
# Keep track of "successes"
num_success = 0
cnt = 0

file = open("Q1_Output.txt", "w")
file.truncate(0)

buff1 = random.randint(0, 1)
file.write(str(buff1)+"\n")
for i in range(2, n + 1):
    if cnt >= n_flips - 1:
        num_success = num_success + 1
        file.write("Success "+str(num_success)+"!"+"\n")
    buff2 = buff1
    buff1 = random.randint(0, 1)
    file.write(str(buff1)+"\n")
    if buff1 == buff2:
        cnt = cnt + 1
    else:
        cnt = 0
print("\nnum_success:" + str(num_success))
print("Estimated probability:" + str(num_success / n))



# E[x] = 0.002