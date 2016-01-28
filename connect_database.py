#!/ur/bin/env python
#coding:utf-8


import MySQLdb

conn= MySQLdb.connect(
        host='',
        user='root',
        passwd='',
        db ='monitor',
)
cursor = conn.cursor()

#获得表中有多少条数据
cursor.execute("select * from polls_status")
row = cursor.fetchall()
print row

cursor.close()
conn.close()