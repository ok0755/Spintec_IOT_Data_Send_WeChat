# author:Zhoubin
# 02-04-2020
import requests               
import os                      
import json     
import time               
import itchat                                                   #  微信API官方文档: https://itchat.readthedocs.io/zh/latest/
from time import sleep
from apscheduler.schedulers.blocking import BlockingScheduler   # 定时任务
''' 
程序功能：定时抓取IOT机台运行数据，按自定义规则(本例 totalDownTime > 30)收集指定字段信息,发送至微信指定好友(本例传至"文件传输助手"，即:自己传给自己)
微信实时监控机器运行情况
'''
def get_produce_information(): 
    global itchat
    text = '机台 数量 运行时间^停机时间 报警信息 \t\n'                                     # \t\n 换行 
    url='http://59.40.183.220:8888/realTimeMonitor/update'                              # IOT_system json data 入口
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    response = requests.get(url,headers=header)                                         # get results
    data =response.json()                
    IOT_informations = data.get('serverinformations')
    for x in IOT_informations: 
        if int(x.get('totalDownTime')[:2])*60 + int(x.get('totalDownTime')[3:5]) > 30:  # 定义搜集规则：if 停机时间(分钟) > 30
            text = text + '{} {} {} {}^{} {} {}\t\n'.format(x.get('machineId'),x.get('productName').replace('N/A',''),x.get('producedParts'),x.get('totalRunTime')[:5],x.get('totalDownTime')[:5],x.get('alarmMsg'),x.get('idleMsg'))
    text = text + '_____________________\t\n' + time.ctime(time.time())                 # 消息末行添加日期时间
    if len(text)>70:
        itchat.send(text,toUserName='filehelper')                                       # 发送text至微信文件传输助手,也可以定义为任意微信好友
    else:
        pass

if __name__=='__main__':
    itchat.auto_login(hotReload=True)                               # 弹出二维码，微信扫码登录
    sched = BlockingScheduler()
    sched.add_job(get_produce_information,'interval',seconds=600)    # 每隔600执行一次get_produce_information
    sched.start()                                                
    
'''
网页 http://59.40.183.220:8888/realTimeMonitor/update 为所有已接入IOT机台运行信息，数据如下(以C-40为例),数据每秒实时更新
本程序仅抓取machineId、productName、producedParts、totalRunTime、totalDownTime、alarmMsg、idleMsg，共七个字段值
machineId: "C-40"
states: 4
operatingTimeDay: 12
operatingTimeTime: "19:07:54"
cuttingTimeDay: 382
cuttingTimeTime: "00:40:57"
productName: "3106009"
programName: "N/A"
cycleTime: "00:00:00"
producedParts: 2
ngParts: 0
speed: 0
maxSpeed: 3500
targetSpeed: 0
feedRate: 0
maxFeedRate: 0
targetFeedRate: 0
totalRunTime: "00:00:00"
totalDownTime: "08:35:42"
alarmMsg: ""
idleMsg: ""
planProductionTime: "12:00:00"
lastCycleTime: "00:00:57"
notRead: true
location: null
supposedProducedParts: 0
systemInit: false
ngRate: 0
machineID: "C-40"
opName: null
productName: "3106009"
materialBatch: null
orderBatch: null
productionBatch: null
planStopTime: "00:00:00"
idealCycleTime: "00:00:59"
numberOfTargetParts: 0
targetFeedRate: 0
targetSpindleSpeed: 0
targetNGPercentage: 0
totalNG_Product: 0
shiftDateOfNG_Product: null
nameOfNG_Product: null
idleReasonCode: 0
notRead: false
programName: "N/A"
prototypePeriod: false
'''