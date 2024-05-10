from dbConnector import Database

class GroupManager:
    def __init__(self, db=Database()):
        self.db = db
        self.conn = db.get_connection()
        
    def searchByUserID(self, uid):
        sql = "SELECT gid FROM usergroup where uid="+str(uid)
        cursor = self.conn.cursor()
        cursor.execute(sql)
        info = cursor.fetchall()
        if info:
            print(info)