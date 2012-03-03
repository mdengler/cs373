# CS 373 Unit 2.22: New Mean Variance

# keep around just to check
def new_mean2(old_means, old_variances):
    numerator = sum([old_variance * old_mean
                     for old_variance, old_mean
                     in zip(old_variances, reversed(old_means))])
    denominator = sum([old_variance for old_variance in old_variances])
    return numerator / denominator

def new_variance2(old_variances):
    return 1 / sum([(1 / old_variance)
                    for old_variance in old_variances])

old_means = [10., 13.]
old_variances = [8., 2.]

print new_mean2(old_means, old_variances)  # 10.6 argh wrong!  reversed(..) 12.4
print new_variance2(old_variances)         # 1.6

def update(mean1, var1, mean2, var2):
    new_mean = ((mean1 * var2) + (mean2 * var1)) / (var1 + var2)
    new_var = 1 / sum([1 / old_variance for old_variance in [var1, var2]])
    return [new_mean, new_var]

print update(10.,8.,13., 2.)


# yup, right, 12.4 and 1.6
