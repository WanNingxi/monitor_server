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
cursor.execute("select * from polls_ip_address")
row = cursor.fetchall()

a= dict(row)
print a

for x in a.values():
	filename = open('ip.txt','a+')
	filename.write(x)
	filename.close()

cursor.close()
conn.close()