import numpy as np


"""
Created on Mon Jan 21 15:09:25 2019

@author: jc18548
"""

def power(sample1, sample2, reps, size, alpha):
    complete = np.concatenate((sample1,sample2),axis=None)
    for i in range(len(reps)):
        sample1_new = complete[0:size]
        sample2_new = complete[size:size*2]
        p = (sample1_new.mean() - sample2_new.mean()) / i
        if p < (1-alpha):
            count += 1
        complete = np.random.shuffle(complete)
    percentage = count/reps
    return percentage
