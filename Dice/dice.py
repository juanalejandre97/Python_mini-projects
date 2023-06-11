                                            ## DADO ##

import numpy as np

def dado():
    num = np.random.randint(1,6,1)[0]
    print(f'%-----%\n'
          f' - {num} - \n'
          f'%-----%')
dado()
