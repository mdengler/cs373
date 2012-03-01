# CS 373 Unit 1.10: Phit and Pmiss

#Write a code that outputs p after multiplying each entry
#by pHit or pMiss at the appropriate places. Remember that
#the red cells 1 and 2 are hits and the other green cells
#are misses


p=[0.2,0.2,0.2,0.2,0.2]
pHit = 0.6
pMiss = 0.2

#Enter code here
p = [prior * obs for prior, obs
             in zip(p, [pMiss, pHit, pHit, pMiss, pMiss])]

# normalize - not yet
#sum_multiples = sum(p)
#p = [unnormalized / sum_multiples for unnormalized in p]

print p
