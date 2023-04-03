import pandas as pd
import numpy as np


chat_id = 341299061

def solution(p: float, x: np.array) -> tuple:
    fun=lambda x: x-0.017
    x=fun(x) 
    alpha = 1 - p
    loc = x.max()
    return 0.017+loc/(1-alpha/2), \
           0.017+loc/(alpha / 2)
