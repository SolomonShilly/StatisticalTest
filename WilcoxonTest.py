# Fresh N Friendly food store advertises that their checkout waiting times is
# four minutes or less. An angry customer wants to dispute this claim.
# He takes a random sample of shoppers at the peak time and records their checkout times.
# Can he dispute their claim at significance level 10%?
# Source: https://online.stat.psu.edu/stat500/lesson/11/11.1/11.1.2

import numpy as np
from scipy import stats

data = np.array([3.8, 5.3, 3.5, 4.5, 7.2, 5.1])

mu = 4

stat, pVal = stats.wilcoxon(data - mu, alternative="greater")

print(f'Wilcoxon Statistic: {stat}')
print(f'P=Value: {pVal}')

alpha = 0.10
if pVal < alpha:
    print("Null hypothesis is rejected because the sample mean is significantly different from the population mean.")
else:
    print("Failed to reject the null hypothesis because there is no significant difference between the sample and population means.")