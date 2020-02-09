# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 14:36:34 2020

@author: VX418GA
"""

# In[1]

import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt 
from datetime import datime
from pandas import Series
#%matplolib inline
import warnings
warnings.filterwarnings("ignore")

# In[2]
# load datasets

train = pd.read_csv("../data/Train_SU63ISt.csv") 
test = pd.read_csv("../data/Test_0qrQsBZ.csv")

 
