# CS 373 Unit 1.20: Inexact Motion 3

# assume uniform distribution:
prior = [0.2] * 5

posterior = [0] * len(prior)

for i in range(len(prior)):
    i_1 = (i + 1) % len(prior)
    i_2 = (i + 2) % len(prior)
    i_3 = (i + 3) % len(prior)
    posterior[i_1] += 0.1 * prior[i]
    posterior[i_2] += 0.8 * prior[i]
    posterior[i_3] += 0.1 * prior[i]

print posterior
# >>> [0.20000000000000007, 0.20000000000000004, 0.20000000000000007, 0.20000000000000007, 0.20000000000000007]
#
# So if we could have been anywhere to start, we could be anywhere at
# the end (because our over and undershoot probability was the same, I
# guess).  Let's see if that was right, and if so I want to see how
# the distribution changes if the over- and under-shoot probabilities
# are not the same.
#
# Yes, this is the right answer.
#
# Ok, so now I'll try some unequal distribution of over- and
# under-shoot probabilities.
posterior = [0] * len(prior)

for i in range(len(prior)):
    i_1 = (i + 1) % len(prior)
    i_2 = (i + 2) % len(prior)
    i_3 = (i + 3) % len(prior)
    posterior[i_1] += 0.1 * prior[i]
    posterior[i_2] += 0.7 * prior[i]
    posterior[i_3] += 0.2 * prior[i]

print posterior

# wow, it's still the same.  I guess each...box gets 0.1 of one, 0.7
# of another, and 0.2, so as long as they all add up to one, 0.2 will
# always accumulate in each cell.





