# CS 373 Unit 1.25: Sense and move

#Given the list motions=[1,1] which means the robot
#moves right and then right again, compute the posterior
#distribution if the robot first senses red, then moves
#right one, then senses green, then moves right again,
#starting with a uniform prior distribution.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
motions = [1,1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

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


def move(prior, U):

    posterior = [0] * len(prior)

    for i in range(len(p)):
        i_u = (i + (U - 1)) % len(prior)
        i_e = (i +  U     ) % len(prior)
        i_o = (i + (U + 1)) % len(prior)

        posterior[i_u] += pUndershoot * prior[i]
        posterior[i_e] += pExact      * prior[i]
        posterior[i_o] += pOvershoot  * prior[i]

    return posterior


for m, s in zip(measurements, motions):
    p = sense(p, m)
    p = move(p, s)

print p
