#coding=utf-8

import os.path
import time
import pdb
import File


if __name__=="__main__":
    filePath='/data/python-scripts/inspector/AccountInspector/otherInspector/kafka.log'
    f=open(filePath,"r")
    columnNameList=['GROUP','TOPIC','PARTITION','CURRENT-OFFSET','LOG-END-OFFSET','LAG','OWNER']
    result='no topicPartition lag is over allowedRange'
    resultDic={}
    overAllowedLagDic={}
    for line in f:
        #使用命令行处理时有时会得到Consumer group is not exists 或者Consumer group is rebalancing等不正常的结果，这种数据忽略不处理
        if 'Consumer group' not in line:
            line=line.strip('\n')
            lineSplit=line.split(' ')
            dicKey=lineSplit[0]+'_'+lineSplit[1]+'_'+lineSplit[2]
            dicValue={}
            for i in range(0,len(lineSplit),1):
                dicValue[columnNameList[i]]=lineSplit[i]
            #由于我设置的阀值时lag值为1000时就告警，此处LOG-END-OFFSET就是logsize，当logsize小于1000时可以忽略（因为lag总是小于logsize的）
            if dicValue['LOG-END-OFFSET']<='1000':
                dicValue['CURRENT-OFFSET']='0'
                dicValue['LAG']='0'
            resultDic[dicKey]=dicValue
            #使用命令行有缺陷，经常会出现取出来的值为unknown的情况，出现这种情况也当作告警处理
            if dicValue['LAG'] == 'unknown':
                overAllowedLagDic[dicKey]=dicValue
            else:
                if int(dicValue['LAG'])>1000:
                    overAllowedLagDic[dicKey]=dicValue
    if len(overAllowedLagDic)>0:
        result=''
        for key in overAllowedLagDic:
            dicValue=overAllowedLagDic[key]
            lag=dicValue['LAG']
            result=key+':'+lag+'; '+result
    print result