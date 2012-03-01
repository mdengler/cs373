# CS 373 Unit 1.32: Cancer Test

# probabilities must sum to 1
# Bayes rule: p(X_i|Z) = (p(Z|X_i) * p(X_i)) / p(Z)

p_C  = 0.001
p_nC = 1 - p_C

p_POS_g_C  = 0.8
p_POS_g_nC = 0.1

p_C_g_POS = None  # find this

# X_i = C
# Z = POS
#
# Bayes: p(C|POS) = p(POS|C) * p(C) / p(POS)
#
# What we know:
# p(POS|C) = 0.8
# p(C) = 0.001
# p(POS|!C) = 0.1
#
# What we need to know:
# p(POS)
#
# What we can infer:
# p(POS|C) + p(POS|!C) = p(POS)
# p(POS) = 0.9
#
# alternately:
# p(POS|C) + p(POS|!C) + p(!POS) = 1
# p(POS) = 1 - p(!POS)
# p(POS) = 0.9
p_POS = p_POS_g_C + p_POS_g_nC
print "p(POS|C) + p(POS|!C) = p(POS) = %s" % p_POS

#
# So now:
# p(C|POS) = p(POS|C) * p(C) / p(POS)
print "p(C|POS) = p(POS|C) * p(C) / p(POS)"

# p(C|POS) = 0.8 * 0.001 / 0.9
p_C_g_POS = (p_POS_g_C * p_C) / p_POS
print "%s = %s * %s / %s" % (p_C_g_POS, p_POS_g_C, p_C, p_POS)

# which is 0.00088888889, rounds to 0.0009, but this is wrong.
# Where did I go wrong?
# Is it p(POS|C) + p(POS|!C) = p(POS) ?
#
# Re-watching the video, we have:
# p(Z) = sum for all i of p(Z|X_i) * p(X_i)
# ...rewritten...
# p(POS) = (p(POS|C) * p(C)) + (p(POS|!C) * p(!C))
#
# so where was my error?  p(POS)?  X_i = C?  TODO
#
# Let's try this:
print "p(POS) = (p(POS|C) * p(C)) + (p(POS|!C) * p(!C))"
p_POS = (p_POS_g_C * p_C) + (p_POS_g_nC * p_nC)
print "p(POS) = (%s * %s) + (%s * %s)" % (p_POS_g_C, p_C, p_POS_g_nC, p_nC)

#
# So now:
# p(C|POS) = p(POS|C) * p(C) / p(POS)
print "p(C|POS) = p(POS|C) * p(C) / p(POS)"

# p(C|POS) = 0.8 * 0.001 / 0.000888888889
p_C_g_POS = (p_POS_g_C * p_C) / p_POS
print "%s = %s * %s / %s" % (p_C_g_POS, p_POS_g_C, p_C, p_POS)

# so this is:
# p(POS) = (p(POS|C) * p(C)) + (p(POS|!C) * p(!C))
# p(POS) = (0.8 * 0.001) + (0.1 * 0.999)
# p(C|POS) = p(POS|C) * p(C) / p(POS)
# 0.00794438927507 = 0.8 * 0.001 / 0.1007
#
# ...which rounded to 4dp is 0.0079, which is correct!
#

