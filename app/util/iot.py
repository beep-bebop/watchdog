#coding=utf-8
import json
from flask import jsonify
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import time

client = AcsClient('LTAI4FibaEMFDdTEn52ZVknq', 'cVcZycw7BYEDGYBELNFjhwdgUnDEsA', 'cn-shanghai')

request = CommonRequest()
request.set_accept_format('json')
request.set_domain('iot.cn-shanghai.aliyuncs.com')
request.set_method('POST')
request.set_protocol_type('https') # https | http
request.set_version('2018-01-20')
request.set_action_name('QueryDevicePropertiesData')

request.add_query_param('RegionId', "cn-shanghai")
request.add_query_param('DeviceName', "repi")
# request.add_query_param('StartTime', "1585142175744")
# request.add_query_param('EndTime', "1585142201252")
request.add_query_param('Asc', "0") #倒叙查询
# request.add_query_param('PageSize', "10")
request.add_query_param('Identifier.1', "Temp")
request.add_query_param('Identifier.2', "Humi")
request.add_query_param('ProductKey', "a1LzScM0N1F")

def print_data():
    response = client.do_action(request)
    print(str(response, encoding = 'utf-8'))

#返回一条数据
def single_data():
    start_time = int(round(time.time() * 1000))
    end_time = start_time-10000 #以10秒为间隔进行向前查询
    request.add_query_param('StartTime', str(start_time))
    request.add_query_param('EndTime', str(end_time))
    request.add_query_param('PageSize', 1) #返回结果数
    response = client.do_action(request)
    #为了使用测试数据 注释掉返回实际数据的部分
    # print(str(response, encoding = 'utf-8'))
    # return str(response, encoding = 'utf-8')
    test = '{"NextValid":false,"RequestId":"CC4CAC00-ED4C-4004-9E8D-E8B4A78552FA","PropertyDataInfos":{"PropertyDataInfo":[{"List":{"PropertyInfo":[{"Value":"32.46","Time":1579249151178}]},"Identifier":"Temperature"},{"List":{"PropertyInfo":[{"Value":"48","Time":1579249151178}]},"Identifier":"Humidity"}]},"Success":true}'
    return test