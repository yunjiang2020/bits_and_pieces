# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import shutil

#C:/Users/yunji/OneDrive/桌面/incu 20210809/VID1252_B2_1_2021y08m08d_00h00m.jpg
#orinigal path
pathname_ori = 'C:/Users/yunji/OneDrive/桌面/incu 20210809/'
#new path
pathname_des = 'C:/Users/yunji/OneDrive/桌面/incu 20210809/sort/'
#os.mkdir(pathname_des)
if not os.path.isdir(pathname_des):
    os.mkdir(pathname_des)
   
#get all file names from fold
#C:/Users/yunji/OneDrive/桌面/0510 incu/plate 1 green/VID1177_E4_1_2021y05m10d_00h52m.jpg
#VID1177_E4_1_2021y05m10d_00h52m.jpg
file_name = os.listdir(pathname_ori) 
#plate map
sample_arrange={}
'''
sample_arrange['DMEM']=['B2','C2','D2']
sample_arrange['DMSO']=['E2','F2','G2']

sample_arrange['MycB']=['B3','C3','D3']
sample_arrange['MA 2-13']=['E3','F3','G3']

sample_arrange['MA 5-14']=['B4','C4','D4']
sample_arrange['BVP 3-01']=['E4','F4','G4']

sample_arrange['MA 5-14']=['B4','C4','D4']
sample_arrange['BVP 3-01']=['E4','F4','G4']

sample_arrange['BVP 3-22']=['B5','C5','D5']
sample_arrange['BVP 3-15']=['E5','F5','G5']

sample_arrange['MA 6-36']=['B6','C6','D6']
sample_arrange['MA 6-45']=['E6','F6','G6']

sample_arrange['MA 6-42']=['B7','C7','D7']
sample_arrange['BVP 10-50']=['E7','F7','G7']

sample_arrange['BVP 10-49']=['B8','C8','D8']
sample_arrange['BVP 7-86']=['E8','F8','G8']

sample_arrange['BVP 7-48']=['B9','C9','D9']
sample_arrange['BVP 7-36']=['E9','F9','G9']
'''
sample_arrange['BVP 7-35']=['B10','C10','D10']
sample_arrange['BVP 7-45']=['E10','F10','G10']

sample_arrange['BVP 9-16']=['B11','C11','D11']
sample_arrange['BVP 9-17']=['E11','F11','G11']

well_number = {}
well_number['B']=1
well_number['C']=2
well_number['D']=3
well_number['E']=1
well_number['F']=2
well_number['G']=3

for name in file_name:
    if len(name)<20:
        continue

    fold_name = 'None'
    well_name = name[8:11]
#   print(well_name)
#    row_name = well_name[1:3]
#    if well_name[2]=='_':
#        well_name = well_name[:2]
        
    row_name = well_name[0]    
    for key in sample_arrange.keys():
        if well_name in sample_arrange[key]:
            fold_name = key
            break
    if fold_name =='None':
        continue
    well_count = well_number[row_name]
            
    
    file_org = pathname_ori+ name
    file_des = pathname_des + fold_name + '/'+str(well_count)+'/'+name
    if not os.path.isdir(pathname_des + fold_name):
        os.mkdir(pathname_des + fold_name)
    if not os.path.isdir(pathname_des + fold_name + '/'+str(well_count)):
        os.mkdir(pathname_des + fold_name + '/'+str(well_count))
    try:
        os.rename(file_org, file_des)
        shutil.move(file_org, file_des)
        os.replace(file_org, file_des)    
    except:
        print(fold_name)
    

            
