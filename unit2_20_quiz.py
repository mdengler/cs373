# CS 373 Unit 2.20: Separated Gaussians
# Plugging and chugging his formulas is easy enough:

def new_mean(old_means, old_variances):
    numerator = sum([old_variance * old_mean
                     for old_variance, old_mean
                     in zip(old_variances, reversed(old_means))])
    denominator = sum([old_variance for old_variance in old_variances])
    return numerator / denominator

def new_variance(old_variances):
    return 1 / sum([(1 / old_variance)
                    for old_variance in old_variances])

old_means = [10., 13.]
old_variances = [8., 2.]

print new_mean(old_means, old_variances)  # 10.6 argh wrong!  reversed(..) 12.4
print new_variance(old_variances)         # 1.6

