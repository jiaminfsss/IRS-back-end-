from dbConnector import Database

class ImageManager:
    def __init__(self,upload_root_path='./',db=Database()):
        self.db = db
        self.conn = db.get_connection()
        self.upload_root_path=upload_root_path
        
    def getPublicGallery(self, page_num=0, page_size=20):
        return self.selectImagesByGid(0,page_num=0, page_size=20)

    def selectImagesByGid(self, gid, page_num=0, page_size=20):
        page_offset = (page_num - 1) * page_size
        sql = f"""
        SELECT imageinfo.iid,imageinfo.path,userinfo.uname,imageinfo.likes,groupinfo.groupName
        FROM imageinfo
        JOIN userinfo ON userinfo.uid = imageinfo.uploadUid
        JOIN groupinfo ON groupinfo.gid = imageinfo.gid
        WHERE imageinfo.gid = {gid} 
        LIMIT{page_size} OFFSET {page_offset}"""
        cursor = self.conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        result=[]
        for row in rows:
            result.append({'iid':row['id'],'path':row['path'],'owner':row['uname'],'likes':row['likes'],'groupName':groupName})
        return result
    
    def selectImagesByUid(self, uid, page_num=0, page_size=20):
        page_offset = (page_num - 1) * page_size
        sql = f"""
        SELECT imageinfo.iid,imageinfo.path,userinfo.uname,imageinfo.likes,groupinfo.groupName
        FROM imageinfo
        JOIN userinfo ON userinfo.uid = imageinfo.uploadUid
        JOIN groupinfo ON groupinfo.gid = imageinfo.gid
        WHERE imageinfo.uploadUid = {uid} 
        LIMIT{page_size} OFFSET {page_offset}"""
        cursor = self.conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        result=[]
        for row in rows:
            result.append({'iid':row['id'],'path':row['path'],'owner':row['uname'],'likes':row['likes'],'groupName':groupName})
        return result

    def addImageToPublicGallery(self, img_raw, uid):

    

    def addImageToGroupGallery(self, img_raw, uid):



    def userLogin(self, username, password):
        print(str(username))
        sql = "SELECT * FROM userinfo where uname='"+str(username)+"'"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        info = cursor.fetchone()
        if info:
            dbpasswd = info[2]
            if dbpasswd == password:
                return 1, {'uid':info[0],'uname':info[1],'urole':info[3]}
            else:
                return 2,{}
        else: return 2,{}