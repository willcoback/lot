
import pymysql
import configparser


def connection():
    config=configparser.ConfigParser()
    config.read("./default.cfg")
    host=config['mysql.connection']['host']
    user=config['mysql.connection']['user']
    passwd=config['mysql.connection']['passwd']
    db=config['mysql.connection']['database']
    print(__name__)
    return pymysql.connect(host=host,user=user,password=passwd,db=db,port=3306)
if __name__ == '__main__':
    conn=connection()
    cursor=conn.cursor()
    cursor.execute("select version()")
    data=cursor.fetchone()
    print ("Database version : %s " % data)
    conn.close()