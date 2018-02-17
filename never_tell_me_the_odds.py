import random as r
from operator import add

# Ask for user input on how many dice of eacy type to roll
green = int(input("Ability dice?"))
yellow = int(input("Proficiency dice?"))
purple = int(input("Difficulty dice?"))
red = int(input("Challenge dice?"))
blue = int(input("Boost dice?"))
black = int(input("Setback dice?"))

final = 0
s_result = 0
a_sresult = 0
a_fresult = 0
repetitions = 100000

# Each list contains [successes,advantage] for each side of the die
g_success = [[0,0],[0,1],[0,1],[0,2],[1,0],[1,0],[1,1],[2,0]]
y_success = [[0,0],[0,1],[0,2],[0,2],[1,1],[1,1],[1,1],[1,1],[1,0],[1,0],[2,0],[2,0]]
p_success = [[0,0],[0,-1],[0,-1],[0,-1],[0,-2],[-1,0],[-1,-1],[-2,0]]
r_success = [[0,0],[0,-1],[0,-1],[0,-2],[0,-2],[-1,0],[-1,0],[-1,-1],[-1,-1],[-1,-1],[-2,0],[-2,0]]
b_success = [[0,0],[0,0],[0,1],[0,2],[1,0],[1,1]]
s_success = [[0,0],[0,0],[0,-1],[0,-1],[-1,0],[-1,0]]

# Randomly choose a side of each die and add up all successes and advantages
# Chooses a side i times, where i is the user selected number of that die to roll
for i in range(repetitions):
    output = [r.choice(g_success) for i in range(green)] \
             + [r.choice(y_success) for i in range(yellow)] \
             + [r.choice(b_success) for i in range(blue)] \
             + [r.choice(p_success) for i in range(purple)] \
             + [r.choice(r_success) for i in range(red)] \
             + [r.choice(s_success) for i in range(black)]
    # Count all successes, but split up advantage to successful and failed rolls
    if sum([item[0] for item in output]) > 0:
        s_result +=1
        a_sresult += sum([item[1] for item in output])
    else:
        a_fresult += sum([item[1] for item in output])

s_final = s_result / repetitions
a_sfinal = a_sresult / s_result
a_ffinal = a_fresult / (repetitions-s_result)

print("{0:.1f}%".format(s_final*100)+" chance of success")
print("{:.2f}".format(a_sfinal)+" average advantage on successful rolls")
print("{:.2f}".format(a_ffinal)+" average advantage on failed rolls")

input("Press enter to close")