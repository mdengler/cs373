# CS 373 Unit 1.7: Probability Answer Sense

#In this question, we want to modify our prior uniform probability
#distribution. We want to make red cells more likely than green by
#multiplying the red cell probabilities by 0.6 and the green cell
#probabilities by 0.2.


p=[]
n=5
p = [1/float(n)] * n
observations = [0.2, 0.6, 0.6, 0.2, 0.2]

posterior = []

for prior, obs in zip(p, observations):
    posterior.append(prior * obs)

print posterior

