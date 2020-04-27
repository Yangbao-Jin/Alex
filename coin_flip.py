import numpy as np
import dit

p = np.random.random()  # randomly generate the probability of head coming up.
coin_flip = dit.Distribution(['H', 'T'],[p, 1-p])  # create the probability model
print(coin_flip)