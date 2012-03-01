# CS 373 Unit 1.16: Exact Motion

# this was my first try: convolving the distribution with a shifted
# version of itself

p = [1/9., 1/3., 1/3., 1/9., 1/9.]
obs = [1/3., 1/3., 1/9., 1/9.]
q = []
for prior, observation in zip(p, p[1:] + [p[0]]):
    q.append(prior * observation)
s = sum(q)
n = [u / s for u in q]
print [round(x, 3) for x in n]


# http://www.udacity-forums.com/cs373/questions/2687/exact-motion-quiz-question
# Evidently the answer is to shift the distribution to the left by one cell.
#
# I kind of understand why this is, but I'm not confident.  I'm just
# making stuff up to fit the answer: No new observations occured (I
# guess, though moving to the right seems like it could be a kind of
# observation) but the movement was known, so the distribution that
# existed before was shifted because the position shifted.  It's not
# clear to me why we don't shift the distribution after observations,
# too, since we know we have moved.
#
# The answer is just:
p = [1/3., 1/3., 1/9., 1/9., 1/9.]
print p

# In fact it's not, it's shifted the other way: to the right.  So the
# robot moved to the right, and the probability distribution moved to
# the right.  So...that's because the relative probabilities of being
# in any given place haven't changed, but we know we have moved to the
# right.  So if the probability of being in cell 2 was x, now we move
# to the right but no new observations, so the probability of being in
# cell 3 is x.  I guess.  I still have the question above, and it's
# been asked in
# http://www.udacity-forums.com/cs373/questions/2687/exact-motion-quiz-question

