# CS 373 Unit 1.18: Inexact Motion 1

# prior distribution:
# 0, 1, 0, 0, 0
#
# U=2; try to move to the right two cells, but succeed with
# probabilities:
#
# p(X_i+2|X_i) = 0.8
# p(X_i+1|X_i) = 0.1
# p(X_i+3|X_i) = 0.1
#
# So my first guess was to just stick the conditional probabilities in
# because there is only one cell with a non-zero probability and it is
# 1, and anyway the conditionals are not defined in terms of X_i but
# simply absolute numbers (though it's not clear to me whether that is
# a shortcut the instructor took because he knew the probability of
# X_i was 1 - more on this in 1.19):
# 0, 0.1, 0.8, 0.1, 0.0.
#
# ...but that was wrong (well the first zero is right, but who cares).
# The last zero is wrong too...really!?
#
# So in coming up with the next guess, are the equations supposed to
# be valid for all i?  I guess so, so now have a convolution, right?
# But it's got to be different, because this implies what I did
# already: p(X_3|X_1) = 0.8...ohhh, I was on the right track first, I
# just stupidly moved by one and not two.  Let's try that again...:
# 0, 0, 0.1, 0.8, 0.1
# Yup, that was it.
# My intution seems to have been totally right.


