import pymysql
from dbutils.pooled_db import PooledDB
from dbutils.persistent_db import PersistentDB
from pymysql.constants import CLIENT
class MysqlHelper(object):
    conn = None
    def __init__(self, host, username, password, db=None,charset='utf8',port=3306):
        self.__pool = PooledDB(creator=pymysql,
                               mincached=10,
                               maxcached=0,
                               maxshared=20,
                               maxconnections=200,
                               maxusage=20,
                               blocking=True,
                               user=username,
                               passwd=password,
                               db=db,
                               host=host,
                               port=port,
                               client_flag = CLIENT.MULTI_STATEMENTS
                               )

    def connect(self):
        conn = self.__pool.connection()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # print("connected successfully")
        return conn, cursor

    def close(self):
        conn,cursor=self.connect()
        cursor.close()
        conn.close()

    def get_one(self, sql, params=()):
        result = None
        title = []
        try:
            conn,cursor=self.connect()
            cursor.execute(sql, params)
            result = cursor.fetchone()
            des = cursor.description
            # title = [item[0] for item in des]
            self.close()
        except Exception as e:
            print(e)
        return result

    def get_all(self, sql, params=()):
        list_data = ()
        title=[]
        try:
            conn,cursor=self.connect()
            cursor.execute(sql, params)
            list_data = cursor.fetchall()
            des = cursor.description
            # title = [item[0] for item in des]
            self.close()
        except Exception as e:
            print(e)
        return list_data

    def insert(self, sql, params=()):
        return self.__edit(sql, params)

    def update(self, sql, params=()):
        return self.__edit(sql, params)

    def delete(self, sql, params=()):
        return self.__edit(sql, params)

    def __edit(self, sql, params):
        count = 0
        try:
            conn,cursor=self.connect()
            count = cursor.execute(sql, params)
            conn.commit()
            self.close()
        except Exception as e:
            print(e)
        return count
if __name__=='__main__':
    mysql=MysqlHelper(host='192.168.56.102',db='park',username='root',password='test123',port=3306)
    mysql.connect()
    sql='select username from users limit 0'
    data=mysql.get_all(sql)
    print(data)
    # l1=[]
    # for j in data:
    #     l1.append([j])
    # print(l1)
