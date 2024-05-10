from dbConnector import Database


class SystemManager:
    def __init__(self,db=Database()):
        self.db = db
        self.conn = db.get_connection()
        
        
    def userLogin(self, username, password):
        print(str(username))
        sql = "SELECT * FROM userinfo where uname='"+str(username)+"'"
        print(sql)
        cursor = self.db.get_connection().cursor()
        cursor.execute(sql)
        info = cursor.fetchone()
        dbpasswd = info[2]
        if dbpasswd == password:
            return 1, info
        else:
            return 2