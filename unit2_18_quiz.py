# CS 373 Unit 2.18: Parameter update

# here again he is referring to the gaussians being "multiplied" by
# "Bayes rule", but he's actually not talking about convolution.  He
# talks about convolution as adding - is that the "overlap" idea?
#
# Ok so at 1:10 he explicitly says that the new variances are
# unaffected by the means, just related to the sum of the old
# variances, so thus even higher variance.  I don't understand the
# relationship between the decay term (1 / sqrt(2 * pi * sigma^2)) and
# the exponent, because it seems though the decay term is getting
# smaller - aha - the denominator of the exponent is also getting
# smaller.  Since the decay term is getting smaller, does that mean it
# decays faster -- yes, I think.  Hence it's peakier.  Ok, getting
# somewhere.  But doesn't the increase in the denominator cancel that
# out?  Maybe not - the decay is 1/sqrt(2 * pi * (sigma1^2 +
# sigma2^2)), but the exp denominator is 2 * (sigma1^2 + sigma2^2), so
# the square root of 2 pi times the squared sum is ...what to 2 * the
# squared sum.  How do they grow as the variance grows / shrinks.  The
# sqrt of 2 * squared sum is going to be slower in growth than 2 *
# squared sum, so even the additional pi in the squareroot term won't
# help it keep up, right?  so 1/x * exp(1/x)...how is that related to
# exp(1/x)?
#
# Will have to come back to that.
#
# Plus I realised the thing I said about the mean being zero was
# wrong.  He's showing two Gaussians with different means to be
# centered at different parts of the x-axis. I see, what I was
# thinking of was (Mathworld says) a "standard" normal distribution,
# to which every normal distribution can be converted, but not in the
# way that I was thinking of (well actually I think it can be, but I
# don't understand the consequences of Mathworld's Z == (X - mu) /
# sigma well enough.
#
# Plugging and chugging his formulas is easy enough:

def new_mean(old_means, old_variances):
    numerator = sum([old_variance * old_mean
                     for old_variance, old_mean
                     in zip(old_variances, reversed(old_means))])
    denominator = sum([old_variance for old_variance in old_variances])
    return numerator / denominator

def new_variance(old_variances):
    return 1 / sum([(1 / old_variance)
                    for old_variance in old_variances])

old_means = [10., 12.]
old_variances = [4., 4.]

print new_mean(old_means, old_variances)  # 11
print new_variance(old_variances)         # 2

# actually, this code may be overly general.  In new_mean(..), I know
# that reversed(..) is right for the len(old_variances) == 2 case, but
# not sure about more


# oops, I got the formulas (or the inputs :)) wrong for variance,
# because I wrote them as if the inputs were volatility (sqrt
# variance) but he had written them as variance (of course).  Doh.

# coming back to my misunderstanding about the variance of the
# convolution, well it seems to be getting much smaller since both the
# decay and the exponentional are getting smaller, but maybe this is
# the wrong way to think about it; maybe it's just that the variance
# is less because it's the square of the standard deviation, and
# that's smaller because...argh, dunno.  Obviously I understand the
# intution that "we're gaining information", but I don't get the link
# between that and the exact change in the variance (of course
# information is inversely correlated variance in some hand-wavy way,
# but I want to do better than that).

