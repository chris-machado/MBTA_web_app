import pandas as pd
import mysqldb

df = pd.read_csv('mbta.csv', low_memory=False)

mbtaDict = {}
for ind, row in df.iterrows():
    mbtaDict['id'] = row.iloc[2], 
    mbtaDict['latitude'] = row.iloc[3], 
    mbtaDict['longitude'] = row.iloc[4], 
    mbtaDict['bearing'] = row.iloc[5], 
    mbtaDict['current_status'] = row.iloc[6],
    mbtaDict['current_stop_sequence'] = row.iloc[7], 
    mbtaDict['direction_id'] = row.iloc[8],
    mbtaDict['label'] = row.iloc[9], 
    mbtaDict['occupancy_status'] = row.iloc[10],
    mbtaDict['speed'] = row.iloc[11], 
    mbtaDict['updated_at'] = row.iloc[12]

    mysqldb.insertMBTARecord(mbtaDict)