from  DBUtils.PooledDB import PooledDB
import pymysql
POOL=PooledDB(
creator=pymysql,
    maxconnections=6,
    mincached=2,
    maxcached=5,
    maxshared=3,
    blocking=True,
    maxusage=None,
    setsession=[],
    ping=0,
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123',
    database='youku',
    charset='utf8',
    autocommit=True

)