# CS 373 Unit 1.9: Normalize distribution

p=[]
n=5
p = [1/float(n)] * n
observations = [0.2, 0.6, 0.6, 0.2, 0.2]

posterior = []

for prior, obs in zip(p, observations):
    posterior.append(prior * obs)

old_sum = sum(posterior)
posterior = [val / old_sum for val in posterior]

print posterior
print sum(posterior)


