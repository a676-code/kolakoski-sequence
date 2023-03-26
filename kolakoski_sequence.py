# kolakoski_sequence.py
# Andrew Lounsbury, with some code adapted from kolakoski.py at https://github.com/w4jbm/Kolakoski-Sequence.git
# 23/3/23
# Purpose: demonstrate that the average of the kolakoski sequence tends to 3/2 as n -> infinity

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# generates the Kolakoski sequence up to the n-th number
# adapted from kolakoski.py at https://github.com/w4jbm/Kolakoski-Sequence.git
def generate_kolakoski(n):
    # we start with three numbers to avoid having to add a partial sequence of 2's
    sequence = [1, 2, 2]
    n1 = sequence[0]
    n2 = sequence[1]
    counter = 2
    while len(sequence) < n:
        for x in range(sequence[counter]):
                sequence.append(n1)
        counter += 1
        # with each iteration, we're either inserting a full set of 1's or a full set of 2's, so we can simply alternate between them
        n1, n2 = n2, n1
    return sequence
    
# scatterplot of 10 numbers
n = 10
sequence = generate_kolakoski(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)

df1 = pd.DataFrame(average_sequence, columns=["Average"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Average", data=df1)
plt.show()
    
# scatterplot of 100 numbers
n = 100
sequence = generate_kolakoski(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)

df1 = pd.DataFrame(average_sequence, columns=["Average"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Average", data=df1)
plt.show()

# scatterplot of 999 numbers (1000 gives an inconspicuous error)
n = 999
sequence = generate_kolakoski(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)

df1 = pd.DataFrame(average_sequence, columns=["Average"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Average", data=df1)
plt.show()