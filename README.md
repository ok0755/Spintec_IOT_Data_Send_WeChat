# Spintec_IOT_Data_Send_WeChat
''' 
程序功能：定时抓取IOT机台运行数据，按自定义规则(本例 totalDownTime > 30分钟)收集指定字段信息,发送至微信指定好友(本例传至"文件传输助手"，即:自己传给自己)
微信实时监控机器运行情况
'''

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
