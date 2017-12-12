import pymysql
from leaveapp import config


conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    db='leaveapp')

cur = conn.cursor()


