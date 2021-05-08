
import pymysql
import configparser


def connection():
    config=configparser.ConfigParser()
    config.read("../default.cfg")
    host=config['mysql.connection']['host']
    user=config['mysql.connection']['user']
    passwd=config['mysql.connection']['passwd']
    db=config['mysql.connection']['database']
    return pymysql.connect(host=host,user=user,password=passwd,db=db,port=3306)
def execute(sql,value):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(sql,value)
    conn.commit()
    data0 = cursor.fetchone()
    data1 = cursor.fetchall()
    cursor.close()
    conn.close()
    return data0,data1
if __name__ == '__main__':
    conn=connection()
    cursor=conn.cursor()
    cursor.execute("select version()")
    data=cursor.fetchone()
    print ("Database version : %s " % data)
    conn.close()