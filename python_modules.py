import math
import random
import datetime
from datetime import datetime, date, time, timedelta

# Math module examples
print(math.pow(2, 5))           # 2 raised to the power of 5 → 32.0 (as float)
print(math.cos(0))              # cosine of 0 radians → 1.0
print(math.factorial(5))        # 5! (factorial) → 120

# Random module examples
print(random.random())          # random float between 0.0 and 1.0
print(random.randint(1, 50))    # random integer between 1 and 50 (inclusive)

# Random choice from a list
ls = ['red', 'black', 'blue']
print(random.choice(ls))        # randomly selects one element from ls

# Shuffle a list
ls1 = ['c2', 'c3', 'c1']
random.shuffle(ls1)             # shuffles ls1 in place (original list is changed)
print(ls1)                      # prints the shuffled list

# Show the original color list (unchanged)
print(ls)                       # prints ['red', 'black', 'blue']

# Randomly sample 2 unique elements from ls1
ls2 = random.sample(ls1, 2)     # picks 2 unique random elements from ls1
print(ls2)                      # prints the sampled elements

# DateTime

# c1 = datetime.datetime.now()
# print(c1)
