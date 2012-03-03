# CS 373 Unit 2.17: Predicting the peak

# insanely hard question?  I guess that means it's not going to be the
# middle, which is what I would say intuition-wise.  If it's the
# higher one, then that means the mean has been averaged but the
# variance has been amplified.
#
# Perhaps I should imagine what should happen in the convolution of
# the measurement and a uniform distribution.  I guess it
# would...lower the mean (towards zero) but fatten the tails?  I'm not
# sure why that's intuitive.  Let me cheat a tiny bit and look at
# convolution on wikipedia to see if the animations lead me anywhere.
#
# Mathworld's animations are great:
# http://mathworld.wolfram.com/Convolution.html and also give the
# answer: the mean has been averaged and the variance has been
# dampened.  But by how much?  I think by a lot from the wolfram page.
# Unless both functions have a mean of >= 1.0, the resulting mean will
# be smaller (err., I mean the value of the function at the mean; ah
# sorry we always take the mean to occur at x=0 so yeah, I mean the
# means should be >= 1.0 for the mean of the convolution to be as big
# or bigger than the smallest function's mean).
#
# No! It's bigger!  Why?
