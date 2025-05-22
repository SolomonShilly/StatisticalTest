# Let's say on average, a battery last 24 hours
# After a new manufacturing change, the battery is not 24 hours
# Null Hypothesis: Battery Life = 24 hours
# Alternative Hypothesis: Battery Life != 24 hours

import numpy as np
from scipy import stats

# 2 Random sample datasets I made
# The first will fail to reject the null hypothesis, and the second will reject it
#sample = np.array([23, 24, 24, 25, 26, 22])
sample = np.array([25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35])

# Population mean will be average battery life
population = 24

# Use stats from scipy to get the 1 sample t-test function
tStat, pVal = stats.ttest_1samp(a=sample, popmean=population)

print("T-statistic: ", tStat)
print("P-Value: ", pVal)

# 5 percent confidence interval will be used
alpha = 0.05

# If loop will be used to see if our p-value is less than alpha
# A p-value below .05 indicates a difference between our control and treatment group
# If p-value is low, we are likey to see a value different than the one in the null hypothesis
if pVal < alpha:
    print("Null hypothesis is rejected because the sample mean is significantly different from the population mean.")
else:
    print("Failed to reject the null hypothesis because there is no significant difference between the sample and population means.")