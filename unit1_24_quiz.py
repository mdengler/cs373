# CS 373 Unit 1.24: Move 1000 Times

#Write code that moves 1000 times and then prints the
#resulting probability distribution

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
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

for i in range(1000):
    p = move(p, 1)

print p

