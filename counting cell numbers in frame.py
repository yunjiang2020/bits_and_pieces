# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 12:39:06 2021

@author: yunji
"""

import pandas as pd
import os

wells = [1]
treatments = ['Doxo']

pathname = 'C:/Users/yunji/OneDrive/桌面/cytostatic effect paper/PI uptake/total cell control/'

ans = {}
for treatment in treatments:
    ans[treatment]=[]
    
for treatment in treatments:
    for well in wells:
        count = {}
        for i in range(6):
            count[i]=0
        open_direction = pathname+treatment+"/"+str(well)+"/export.csv"
        df = pd.read_csv(open_direction)
        for item in df['FRAME']:
            if type(item)==type(1):
                count[item]+=1
        count_1 = []
        for key in count.keys():
            count_1.append(count[key])
        ans[treatment].append(count_1)
        
print(ans)