# CS 373 Unit 1.34: Coin Flip Quiz

# Bayes rule: p(X_i|Z) = (p(Z|X_i) * p(X_i)) / p(Z)
# Total probability rule: P(A) = sum for all B of P(A|B) * P(B)
# weighted sum = convolution

p_T = p_H = 0.5

p_final_H = None # find this

#p_final_H = P(A)
#P(A|B) = probability of final heads given prior heads, prior tails
#p_first_H = p_H = P(B)
#p_first_T = p_T = P(B)

p_H_g_first_T = 0.0
p_H_g_first_H = (p_H * p_first_H) + (p_T * p_first_H) /    #TODO: this I don't understand

p_first_H = p_H
p_first_T = p_T
p_final_H = (p_first_T * p_H_g_first_T) + (p_first_H * p_first_H_g_first_H)  # TODO: I wrote this but it's wrong, why (did I write it and why is it wrong?)
p_final_H = (p_first_T * p_H_g_first_T) + (p_first_H * p_H_g_first_H)




# I just guessed 0.25, which was right, because I reasoned about the
# possibilities of what could happen and the final head was 1/4 of
# them; first tail was 1/2, and first head last tail was 1/4
