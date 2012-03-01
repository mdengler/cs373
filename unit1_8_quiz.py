# CS 373 Unit 1.8: Compute Sum

p=[]
n=5
p = [1/float(n)] * n
observations = [0.2, 0.6, 0.6, 0.2, 0.2]

posterior = []

for prior, obs in zip(p, observations):
    posterior.append(prior * obs)

print sum(posterior)


