from TwoColorBall import ConnectionToMysql

def createStage():
    head="ST"

    sql="SELECT MAX(stage) FROM two_color_ball WHERE forecast_or_not =1"
    fetchone,fetchall=ConnectionToMysql.execute(sql,None)
    maxStage=fetchone[0]
    if maxStage==None:
        maxStage="ST0"
    numberStage=maxStage[2:len(maxStage)]
    intNumber=int(numberStage)+1
    return head+repair0(intNumber,7)

    #print(int(stageNumber))
def repair0(arg,count):
    number=count-len(str(arg))
    return "0"*number+str(arg)

if __name__ == '__main__':
    print(createStage())

