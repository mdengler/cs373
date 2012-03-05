# CS 373 Unit 2.23: Gaussian Motion

# again he's really pushing the intuition that when you move, your
# uncertainty (variance) increases since you have lost information.  I
# don't see where the lost information comes in, since before we could
# say that we "lost information" as we had two amounts of uncertainty.
# I think the ways the uncertainties combine is the intutional step:
# in sensing, we are adding information in the form of two
# observations, but now we are adding uncertainty in the form of two
# ways things could be wrong.  Again, we still have two gaussians and
# we are updating our idea of match-with-the-world / location in both
# situations, so apart from the more basic intuition that sensing
# decreases uncertainty and motion increases uncertainty, I don't see
# how the appeal to intuition explains how the one combination of
# gaussians averages the means and reduces the variance, and the other
# combination adds the means and increases the variance.
#
# But what he's telling us is simple:
#
# new_mean = old_mean + mean of motion
# new_sigmasquared = old_sigma_squared + sigma_squared_of_motion
#
#

old_mean = 8
old_sigma_squared = 4

mean_of_motion = 10
sigma_squared_of_motion = 6

new_mean = old_mean + mean_of_motion
new_sigmasquared = old_sigma_squared + sigma_squared_of_motion

print new_mean
print new_sigmasquared


