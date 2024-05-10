import pymysql
conn = pymysql.connect(host='localhost',
                      user='root',
                      passwd='root',
                      charset='utf8',
                      database='imageretrieval')

cursor = conn.cursor()

sql = 'select * from userinfo'
cursor.execute(sql)
a=cursor.fetchall()
print(a)

class Database:
    def __init__(self, host='localhost',
                      user='root',
                      passwd='root',
                      charset='utf8',
                      database='imageretrieval'):
        self.conn = pymysql.connect(
            host=host,
            user=user,
            passwd=passwd,
            charset=charset,
            database=database
        )
    
    def get_connection(self):
        return self.conn
    
    def close_connection(self):
        self.conn.close()

def getConn():
    return Database().get_connection()