import os
import pymysql
import pandas as pd
import datetime 

def calc_speed(list_1, list_2):  # must be in format (Latitude, longitude, time)
    p1 = list_1[0:2]
    p2 = list_2[0:2]
    t1 = list_1[2] 
    t2 = list_2[2]
    print(p1)
    print(list(dict_2.keys())[2])
    dt = datetime.datetime.hour(t2-t1)
    
    distance = haversine(p1, p2)
    speed = distance/dt
    
    print(f"p1: {p1} p2: {p2} t: {t1}")
    return speed


for ind, bus in busDict.items():  
    speedDict[ind] = []
    for inx, row in bus.iterrows():
        if row['current_stop_sequence'] != 1:
            pass
        else:
            point2.append(row['latitude'])
            point2.append(row['longitude'])
            point2.append(ts.to_pydatetime(row['updated_at'])
        
            speedDict[ind].append(calc_speed(point1, point2))
            
            point1 = point2