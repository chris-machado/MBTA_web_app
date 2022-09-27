import pandas as pd
import mysqldb

df = pd.read_csv('mbta.csv', low_memory=False)
mbtaDictList = []
mbtaDict = {}
for ind, row in df.iterrows():
    mbtaDict['id'] = row.iloc[2]
    mbtaDict['latitude'] = float(row.iloc[3]) 
    mbtaDict['longitude'] = float(row.iloc[4]) 
    mbtaDict['bearing'] = int(row.iloc[5]) 
    mbtaDict['current_status'] = row.iloc[6]
    mbtaDict['current_stop_sequence'] = int(row.iloc[7])
    mbtaDict['direction_id'] = int(row.iloc[8])
    mbtaDict['label'] = row.iloc[9],
    mbtaDict['occupancy_status'] = row.iloc[10]
    mbtaDict['speed'] = row.iloc[11] 
    mbtaDict['updated_at'] = row.iloc[12]

    mbtaDictList.append(mbtaDict)

    mysqldb.insertMBTARecord(mbtaDict)