# CS 373 Unit 1.35: Two Coin Quiz

# Bayes rule: p(X_i|Z) = (p(Z|X_i) * p(X_i)) / p(Z)
# Total probability rule: P(A) = sum for all B of P(A|B) * P(B)
# weighted sum = convolution


# p(H|fair) = 0.5
# p(H|loaded) = 0.1
# p(fair|H) = ??

# p(fair|H) = p(H|fair)p(fair) / p(H)
# = 0.5*0.5/0.5

# nope, that's not it (0.5)



p(fair|take) = 0.5
p(!fair|take) = 0.5

p(fairtake|H) = p(H|fairtake) * p(fairtake) / p(H)
p(H) != 0.5!!!!
p(H) = p(H|fairtake) + p(H|!fairtake) # maybe
better, it's alpha
alpha = unnorm_p(fairtake|H) + unnorm_p(!fairtake|H)
unnorm_p(fairtake|H) = p(fairtake) * p(H) = 0.5 * 0.5 = 0.25
unnorm_p(!fairtake|H) = p(!fairtake) * p(H) = 0.5 * 0.5 = 0.25


No, this is not Bayes, this is total probability:

P(A) = sum for all B of P(A|B) * P(B)

A here is picking fair coin
B can be: heads, tails
B is the tricky one
heads come up: fair * fair_heads + loaded * loaded_heads = 0.5 * 0.5 + 0.5 * 0.1 = 0.25 + 0.05 = 0.3 times
tails come up: fair * fair_tails + loaded * loaded_tails = 0.5 * 0.5 + 0.5 * 0.9 = 0.25 + 0.45 = 0.7 times

P(fair|H) = 0.5 * 0.3 = 0.15
P(fair|T) = 0.5 * 0.7  # actually I don't understand why these numbers should be chosen: specifically the 0.5s
0.15 + 0.35 = 0.5

nope, it's not 0.6 nor 0.4.  nor 0.5


0.6 = H, T = 1.4; H = 0.3, T = 0.7


nope, it's not 0.15


p(fair|H) * p(H) + p(fair|T) * p(T)
print (0.15 * 0.3) + (0.35) * (0.7)
# 0.29, but it's not that


