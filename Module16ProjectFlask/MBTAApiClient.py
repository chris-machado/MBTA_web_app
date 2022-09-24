import urllib.request, json
import mysqldb

def callMBTAApi():
    mbtaDictList = []
    mbtaUrl = 'https://api-v3.mbta.com/vehicles?filter[route]=1&include=trip'
    with urllib.request.urlopen(mbtaUrl) as url:
        data = json.loads(url.read().decode())
        for bus in data['data']:
            busDict = dict()
            # complete the fields below based on the entries of your SQL table
            busDict['id'] = bus['id']
            busDict['longitude'] = bus['attributes']['longitude']
            busDict['latitude'] = bus['attributes']['latitude']
            busDict['bearing'] = bus['attrubutes']['bearing']
            busDict['current_status'] = bus['attrubutes']['current_status']
            busDict['current_stop_sequence'] = bus['attrubutes']['current_stop_sequence']
            busDict['direction_id'] = bus['attrubutes']['direction_id']
            busDict['label'] = bus['attrubutes']['label']
            busDict['occupancy_status'] = bus['attrubutes']['occupancy_status']
            busDict['speed'] = bus['attrubutes']['speed']
            busDict['updated_at'] = bus['attrubutes']['updated_at']

            mbtaDictList.append(busDict)
    mysqldb.insertMBTARecord(mbtaDictList) 

    return mbtaDictList  