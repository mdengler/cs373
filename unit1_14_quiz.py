# CS 373 Unit 1.14: Test Sense Function

#Try using your code with a measurement of 'green' and
#make sure the resulting probability distribution is correct.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'green'
pHit = 0.6
pMiss = 0.2

def normalize(q):
    sum_values = float(sum(q))
    return [unnormalized / sum_values
            for unnormalized in q]

def sense(p, Z):
    q=[]
    for probability, reality in zip(p, world):
        if Z == reality:
            q.append(probability * pHit)
        else:
            q.append(probability * pMiss)
    return normalize(q)

print sense(p,Z)
