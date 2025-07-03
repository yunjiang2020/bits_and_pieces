# -*- coding: utf-8 -*-
"""
Created on Thu May 13 13:22:38 2021

@author: yunji
"""

import pandas
#import numpy as np
import matplotlib.pyplot as plt

def pic_import(treatment,well_number,direct_root):
    file_name = direct_root + treatment +'/'+str(well_number)+'/All Spots statistics_1.csv'
    df = pandas.read_csv(file_name)
    #get only data from first 24 hours
    return df

def extract_position(df):
#extract postion of points from the csv file
    position = {}
    track_num_pre = -1    
    
    object_num = len(df)
    position_index=[]
    for i in range(object_num):
        track_num_now=df.TRACK_ID[i]
        if track_num_now != track_num_pre:
            position[track_num_now]=[[df.POSITION_X[i],df.POSITION_Y[i]]]
            track_num_pre = track_num_now
            position_index.append(track_num_now)
        else:
            position[track_num_now].append([df.POSITION_X[i],df.POSITION_Y[i]])    
    return position, position_index

def set_start_point(position,position_index):
                
    for i in position_index:
        end_f = len(position[i])
        for j in range(1,end_f):
            position_x = position[i][j][0]-position[i][0][0]
            position_y = position[i][j][1]-position[i][0][1]
            position[i][j]=[position_x,position_y]                    
        position[i][0]=[0,0]    
    return position

def set_start_point_with_frame_limit(position,position_index,frame):
    index_with_frame_limit = []            
    for i in position_index:
        end_f = len(position[i])
        if end_f < frame:
            continue
        
        #uncomment if only trajectories for one direction is needed
        #if ((position[i][frame-1][1]-position[i][0][1])>0): #<0 for the other direction
         #   continue
        for j in range(1,frame):
            position_x = position[i][j][0]-position[i][0][0]
            position_y = position[i][j][1]-position[i][0][1]
            position[i][j]=[position_x*1.25,position_y*1.25]                    
        position[i][0]=[0,0] 
        index_with_frame_limit.append(i)
    return position,index_with_frame_limit

def spider_plot_well_stacked(treatments,repeats,frame):
    #adjust direction C:/20210614_spider_plot/sort/MA 6-45/1/VID1202_B8_1_2021y06m11d_14h00m.jpg
    direct_root = 'C:/work/data/20210614_spider_plot/sort/'
    for treatment in treatments:
        for well_number in range(repeats):
            df = pic_import(treatment,well_number+1,direct_root)
            #choose if to add a frame limit on tracks or not
            position,position_index = extract_position(df)
            #position_set,position_index = set_start_point(position,position_index)
            position_set,position_index = set_start_point_with_frame_limit(position,position_index,frame)
#            print(position_set[0][0])
            for j in position_index:
                x_points=[]
                y_points = []
                #for jj in range(len(position_set[j])) if no frame limit is required
                for jj in range(frame):
                    
                    x_points.append(position_set[j][jj][0])
                    y_points.append(position_set[j][jj][1])
                plt.plot(x_points, y_points)
            plt.rc('figure', figsize=(8,10))    
            plt.axhline(y=0, color='black')
            plt.axvline(x=0, color='black')
            plt.xlim(-100, 100)
            plt.ylim(-200, 50)
        filesave = direct_root + treatment +'_spider plot for 3 wells 16 hours.png'   
        plt.savefig(filesave)
        plt.close()
    return



treatments = ['DMSO','DMEM','MycB','MA 2-13','MA 6-45','MA 3-09',
                'MA 3-43']
repeats = 6
frame = 13
spider_plot_well_stacked(treatments,repeats,frame)