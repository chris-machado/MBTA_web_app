import os
import pymysql
import pandas as pd
import datetime 
from haversine import haversine, Unit

host = '127.0.0.1'
port = '3306'
user = 'root'
password = 'MyNewPass'
database = 'MBTAdb'

conn = pymysql.connect(
    host=host,
    port=int(3306),
    user="root",
    passwd=password,
    db=database,
    charset='utf8mb4')


### compile a list of unique buses ### 
busIds = []
for idx, row in df.iterrows():
    if row['id'] in busIds:
        pass
    else:
        busIds.append(row['id'])

### Query DB and and generate DF for each unique bus ###
busDict = {}
for bus in busIds:
    busDict[bus] = pd.read_sql_query(f"SELECT * FROM mbta_buses WHERE id = '{bus}'",conn)      






def calc_speed(list_1, list_2):  # must be in format (Latitude, longitude, time)
    p1 = tuple(list_1[0:2])
    p2 = tuple(list_2[0:2])
    t1 = list_1[2] 
    t2 = list_2[2]
   # print(t1)
    dt = (t2.hour + t2.minute/60 + t2.second/3600) - (t1.hour + t1.minute/60 + t1.second/3600)
   # print(dt)
    
    distance = haversine(p1, p2, unit='mi')
    speed = distance/dt

    return speed

point1 = [-71.1174495, 42.37307976, datetime.datetime.now()]
point2 = []
speedDict = {}
for ind, bus in busDict.items():  
    speedDict[ind] = []
    for inx, row in bus.iterrows():
        if row['current_stop_sequence'] != 1:
            pass
        else:
            point2.append(row['latitude'])
            point2.append(row['longitude'])
            ts = row['updated_at'] 
            point2.append(ts.to_pydatetime(ts))
        
            speedDict[ind].append(calc_speed(point1, point2))
            
            point1 = point2
            point2 = []