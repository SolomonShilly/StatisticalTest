# A car manufacturer claims that no more than 10% of their cars are unsafe.
# 15 cars are inspected for safety,
# 3 were found to be unsafe. Test the manufacturer’s claim:
# Source: https://docs.scipy.org/doc/scipy-1.15.2/reference/generated/scipy.stats.binomtest.html

# Null Hypothesis: No more than 10% of cars produced are unsafe
# Alternative Hypothesis: More than 10% of cars produced are unsafe

from scipy import stats

# Using the binomial test function from the scipy.stats library
result = stats.binomtest(3, n=15, p=0.1, alternative="greater")

# The p-value and statistics will be calculated in the list of results
pVal = result.pvalue
stat = result.statistic

# The statistics is 3/15, or the percentage of cars that were unsafe in the sample dataset
print(f'Based on sample: {stat * 100}% of cars were unsafe')

# alpha will be 5%
alpha = .05

if pVal < alpha:
    print("Null hypothesis is rejected.")
else:
    print("Failed to reject the null hypothesis.")

# The confidence interval with lower and upper bounds on the proportion estimates of our dataset (% of unsafe cars)
ci = result.proportion_ci(confidence_level=0.95)

print(ci)

# Based on the results, we failed to reject the null hypothesis even though 20% of cars in our sample were unsafe.
# This is because our sample size if 15, which is not large enough to make a baseline conclusion on our data
# The true population mean is between 5.7% and 100% at a 95% confidence interval