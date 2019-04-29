

import numpy as np

list_gen = np.random.permutation(25)
k =list_gen.shape[0]

source = './input.txt'
with open(source,'w') as wf:
    for i in range(k):
        wf.write(str(list_gen[i]))
        if (i+1)%5 == 0:
            wf.write('\n')
        else:
            wf.write(' ')
