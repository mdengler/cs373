# CS 373 Unit 1.17: Move function

#Program a function that returns a new distribution
#q, shifted to the right by U units. If U=0, q should
#be the same as p.

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = p[:]
    for idx in range(len(p)):
        newidx = idx + U
        if newidx > len(p) - 1:
            newidx = 0 + (newidx - len(p))
        q[newidx] = p[idx]
    return q

print move(p, 1)
