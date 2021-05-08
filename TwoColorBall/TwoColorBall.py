import requests
import configparser
from lxml import etree
import ConnectionToMysql
#配置连接数据库信息
def main():
    conn = ConnectionToMysql.connection()
    cursor = conn.cursor()
    url = "http://datachart.500.com/ssq/history/newinc/history.php?start=18094&end=18094" #双色球开奖结果查询页面，start和end对应的是期数
    response = requests.get(url)
    response = response.text
    selector = etree.HTML(response)
    count=0
    for i in selector.xpath('//tr[@class="t_tr1"]'):
      count=count+1
      datetime = i.xpath('td/text()')[0] #期数
      a = i.xpath('td/text()')[1]#红球1
      b = i.xpath('td/text()')[2]#红球2
      c = i.xpath('td/text()')[3]#红球3
      d = i.xpath('td/text()')[4]#红球4
      e = i.xpath('td/text()')[5]#红球5
      f = i.xpath('td/text()')[6]#红球6
      g = i.xpath('td/text()')[7]#篮球
      print(datetime,a,b,c,d,e,f,g)
      sql = "insert into two_color_ball (stage,red_ball1,red_ball2,red_ball3,red_ball4,red_ball5,red_ball6,blue_ball) values("+datetime+","+a+","+b+","+c+","+d+","+e+","+f+","+g+");"
      print("sql:"+sql)
      try:
       cursor.execute(sql)
       conn.commit()
       print("插入成功")
      except:
       conn.rollback()
       print("插入失败")
    print("总共："+str(count))
    cursor.close()
    conn.close()
def test():
    config=configparser.ConfigParser()
    print("-Empty config %s"%config.sections())
    print("-Load config file")
    config.read("./default.cfg")
    print("----config----")
    print(config)
    print("----end config----")
    print("> config sections : %s"%config.sections())
    print('mysql.connection' in config)
    for section in config:
        print("[{s}]".format(s=section))
        for key in config[section]:
            print("{k} = {v}".format(k=key,v=config[section][key]))
def probability():
    conn=ConnectionToMysql.connection()
    cursor=conn.cursor()
    sql="SELECT * FROM two_color_ball ORDER BY stage DESC LIMIT 100"

    try:
        cursor.execute(sql)
        conn.commit()
        itemList = cursor.fetchall()
        print("red ball probability:")
        red=listToProbaility(itemList,37)
        print(red)
        print("sorted red:")
        sortedRed=sorted(red.items(), key=lambda kv: (kv[1], kv[0]),reverse=True)
        print(sortedRed)
        item=sorted(sortedRed[0:6])
        prob=[]
        for i in item:
            prob.append(i[0])
        print(tuple(prob))
        print("-"*30)
        print("blue ball probability:")
        blue=listToProbaility(itemList,17)
        print ("sorted blue:")
        print(sorted(blue.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))
    except:
        pass
    finally:
        cursor.close()
        conn.close()
def listToProbaility(*args):
    mapping=retMap(1,args[1])
    count=0
    for item in args[0]:
        if args[1]==37:
            for i in range(1,7):
                mapping[item[i]]=mapping[item[i]]+1
        if args[1]==17:
            mapping[item[7]]=mapping[item[7]]+1
    return mapping
def retMap(*args):
    i=args[0]
    mapping={}
    while i<args[1]:
        mapping[i]=0
        i=i+1
    return mapping

if __name__ == '__main__':
#    test()
    probability()