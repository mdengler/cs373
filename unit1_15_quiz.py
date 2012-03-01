# CS 373 Unit 1.15: Multiple Measurements

#Modify the code so that it updates the probability twice
#and gives the posterior distribution after both
#measurements are incorporated. Make sure that your code
#allows for any sequence of measurement of any length.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def normalize(q):
    sum_values = float(sum(q))
    return [unnormalized / sum_values
            for unnormalized in q]

def sense(p, Z):
    q = []
    for probability, reality in zip(p, world):
        if Z == reality:
            q.append(probability * pHit)
        else:
            q.append(probability * pMiss)
    return normalize(q)

for measurement in measurements:
    p = sense(p, measurement)

print p
