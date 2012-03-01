# CS 373 Unit 1.19: Inexact Motion 2

# prior distribution:
prior = [0, 0.5, 0, 0.5, 0]
#
# U=2; try to move to the right two cells, but succeed with
# probabilities:
#
# p(X_i+2|X_i) = 0.8
# p(X_i+1|X_i) = 0.1
# p(X_i+3|X_i) = 0.1
#
# First try: let's convolve the prior with:
convolve_with = [0, 0, 0.1, 0.8, 0.1]

posterior = []

for p in prior:
    posterior.append(sum([p * c for c in convolve_with]))

print posterior
# nope, we just get the prior back...my understanding or my logic is
# wrong

# let's try manually working it out (convolving?), the way I did it
# before:
posterior = [0] * len(prior)

for i in range(len(prior)):
    i_1 = (i + 1) % len(prior)
    i_2 = (i + 2) % len(prior)
    i_3 = (i + 3) % len(prior)
    posterior[i_1] += 0.1 * prior[i]
    posterior[i_2] += 0.8 * prior[i]
    posterior[i_3] += 0.1 * prior[i]

print posterior
# >>> [0.4, 0.05, 0.05, 0.4, 0.1]
#
# ...which is right!  So I guess the conditional probabilities are
# indeed based on X_i being 1, and so we need to multiply them by the
# real value of X_i.  And we need to sum the probabilities, for
# reasons I lack intuition on right now.  Let's watch the followup
# video.
#
# Ok, so yeah my intuition about what was going on was right.  I would
# like to understand the more formal definition of what's happening
# here, both to understand it and to understand what was wrong with my
# convolution approach.



