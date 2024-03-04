from pymongo.mongo_client import MongoClient
import pymongo
import mysql.connector
import sqlite3


####========================== MONGODB ===============================================####
#1.Read Data
def mongo_getdata(server,db_name,collect_name,require):
    data_get = {}
    k = 0
    myclient = pymongo.MongoClient(server)

    ### Select Database and Collection
    mydb = myclient[db_name]
    mycol= mydb[collect_name]
    cursor = mycol.find({})
    for x in cursor:
        k+=1
        data_get[k]=x

    data_get['count']= k

    return data_get

####==================================================================================####





####==================================SQLITE==========================================####
###1.Read data
def sqlite_read(server,query):
    dbase = sqlite3.connect(server)
    read = dbase.execute(query)
    data_get = {}
    k = 0

    for record in read:
        k+=1
        data_get[k] = record
        # print(record)

    data_get['count'] = k
    # print(data_get)
    return data_get
    dbase.commit()
    dbase.close()


###2.Update data/DELETE/Query data
def sqlite_query(server,query):
    dbase = sqlite3.connect(server)
    cur = dbase.cursor()
    cur.execute(query)
    dbase.commit()
    dbase.close()



###3.Insert database
def sqlite_insert(server,query,query_data):
    dbase = sqlite3.connect(server)
    cur = dbase.cursor()
    cur.execute(query,query_data)
    dbase.commit()
    dbase.close()

####==================================================================================####




### TEST
##Mongo
# data = mongo_getdata(server='mongodb://10.169.209.99:27017/',db_name='assy_system',collect_name='brower_daily',require='')
# print(data)

###SQLITE
# date = '2021-12-16'
# query_data =  f"""SELECT * FROM qr_lens_epoxy_dry WHERE input_date='{date}' """
# data_sqlite = sqlite_read('D:/Reports/Report2/vendor/db/mp_app.sqlite3',query_data)
# print(data_sqlite)

# query_update = """ DELETE FROM qr_lens_epoxy_dry WHERE no = '35278' """
# sqlite_query('D:/Reports/Report2/vendor/db/mp_app.sqlite3',query_update)