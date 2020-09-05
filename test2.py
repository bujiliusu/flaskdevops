import time,MySQLdb
conn = MySQLdb.connect(host='localhost', user='root',passwd='123456', db='devops',charset='utf8')

cursor = conn.cursor()

sql = "drop table if exists user"
cursor.execute(sql)

sql = "create table if not exists user(name varchar(128) primary key, created int(10))"
cursor.execute(sql)

sql = "insert into user(name, created) values(%s, %s)"
param = ('aaa', int(time.time()))
n = cursor.execute(sql, param)
print('insert',n)

sql = "insert into user(name, created) values(%s, %s)"
param = (("bbb", int(time.time())),("ccc", 33), ("ddd", 44))
n = cursor.executemany(sql, param)
print('insertmany',n)

sql = "update user set name=%s where name='aaa'"
param = ("zzz",)
n = cursor.execute(sql,param)
print('update', n)

n = cursor.execute("select * from user")
a = dict(row for row in cursor.fetchall())
print(a)
sql = "delete from user where name=%s"
param = ("bbb",)
n = cursor.execute(sql,param)
print('delete',n)

# 多行查询结果格式化成json串
fields = ['name', 'created']
sql = "select name,created from user"
n = cursor.execute(sql)
result_set = cursor.fetchall()
result = [dict((k, row[i]) for i,k in enumerate(fields)) for row in result_set ]
print(result)
n = cursor.execute("select * from user")
print(cursor.fetchall())

cursor.close()
conn.commit()
conn.close()

