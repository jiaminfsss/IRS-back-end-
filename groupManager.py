from dbConnector import Database


class GroupManager:
    def __init__(self, db=Database()):
        self.db = db
        self.conn = db.get_connection()

    def searchByUserID(self, uid):
        sql = "SELECT gid FROM usergroup where uid=" + str(uid)
        cursor = self.conn.cursor()
        cursor.execute(sql)
        info = cursor.fetchall()
        if info:
            print(info)

    def createGroup(self, founderUid, groupName, groupImages, groupMembers, groupDescribe):
        values = (
            founderUid, groupName, groupImages, groupMembers, groupDescribe)
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO groupinfo (founderUid, groupName, groupImages, groupMembers, groupDescribe)
            VALUES ( ?, ?, ?, ?, ?);
        """, values)

        # 获取新插入的gid
        new_gid = cursor.lastrowid
        print(f"新插入的群组ID: {new_gid}")
        return new_gid

    def queryGroupByUser(self, uid):
        sql = "SELECT uid FROM usergroup where uid=" + str(uid)
        cursor = self.conn.cursor()
        cursor.execute(sql)
        info = cursor.fetchall()
        if info:
            return info
        return None

    def queryGroupByID(self, gid):
        sql = "SELECT gid FROM groupinfo where gid = " + str(gid)
        cursor = self.conn.cursor()
        cursor.execute(sql)
        info = cursor.fetchall()
        if info:
            return info
        return None

    def applyJoinGroup(self, uid, gid):
       values = (uid, gid)
       cursor = self.conn.cursor()
       cursor.execute("""
            INSERT INTO userjoinapply (uid, gid)
            VALUES ( ?, ?);
        """, values)
       new_gid = cursor.lastrowid
       print(f"新插入的申请ID: {new_gid}")
       return new_gid

    def editGroup(self, gid, founderUid, groupName, groupImages, groupMembers, groupDescribe):
        values = (founderUid, groupName, groupImages, groupMembers, groupDescribe, gid)
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE groupinfo
            SET founderUid = ?, groupName = ?, groupImages = ?, groupMembers = ?, groupDescribe = ?
            WHERE gid = ?;
        """, values)
        print(f"更新群组信息成功")
        return

