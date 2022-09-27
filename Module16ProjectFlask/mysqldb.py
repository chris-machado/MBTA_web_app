import mysql.connector

def insertMBTARecord(mbtaList):
    mydb = mysql.connector.connect(
    host="192.168.1.7",
    user="chris",
    password="E$XiVMs11",
    database="MBTAdb"
    )

    mycursor = mydb.cursor()
    #complete the following line to add all the fields from the table
    sql = '''insert into mbta_buses ( 
                id, 
                longitude, 
                latitude, 
                bearing,
                current_status,
                current_stop_sequence,
                direction_id,
                label,
                occupancy_status,
                speed,
                updated_at
                ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    for mbtaDict in mbtaList:
        #complete the following line to add all the fields from the table
        val = (mbtaDict['id'], mbtaDict['latitude'], mbtaDict['longitude'], mbtaDict['bearing'], mbtaDict['current_status'],
                mbtaDict['current_stop_sequence'], mbtaDict['direction_id'], mbtaDict['label'], mbtaDict['occupancy_status'],
                mbtaDict['speed'], mbtaDict['updated_at'],)
        mycursor.execute(sql, val)

    mydb.commit()