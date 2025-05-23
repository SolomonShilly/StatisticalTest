import numpy as np
from scipy import stats

# Null Hypothesis: Rolling 2 six-sided die would lead to a balanced number of combinations
# Alternative Hypothesis: Rolling 2 six-sided die will not lead to a balanced number of combinations

# Observed Frequencies were taken from playing 2 rounds of board games with my friends
# Expected Frequencies were calculated using total turns / possible combinations

# Loading DiceRoll.csv using numpy loadtxt
diceRolls = np.loadtxt('DiceRolls.csv', delimiter=',', skiprows=1)

#print(diceRolls)

# Assigning the 2nd and 3rd columns to their respective variables
observedFreq = diceRolls[:,1]
expectedFreq = diceRolls[:,2]

# For loop to check if correct data is being displayed
for frequency in observedFreq:
    print(frequency)

print("\n")

# For loop checking if correct data is being displayed
# If the wrong expected frequency, program will print message and exit
for frequency in expectedFreq:
    print(frequency)
    if frequency != 14.90909091:
        print("Wrong file is being used")
        exit()

# Chi-Squared test will be done using SciPy
chiSquared, pVal = stats.chisquare(observedFreq, f_exp=expectedFreq)

print("Chi-squared: ", chiSquared)
print("P-Value: ", pVal)

alpha = .05

if pVal < alpha:
    print("Null hypothesis is rejected.")
else:
    print("Failed to reject the null hypothesis.")