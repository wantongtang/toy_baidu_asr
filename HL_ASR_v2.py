# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 18:09:57 2018

@author: Administrator
"""
# 参考：https://www.cnblogs.com/kunixiwa/p/8609843.html

import requests
import wave
import os
import json
import base64

#获取地址
baidu_server = "https://openapi.baidu.com/oauth/2.0/token?"
#获取tokent
grant_type = "client_credentials"
#API Key
client_id = "oRtPNnKGdGeBPokpdQpGnXPN"
#Secret Key
client_secret = "hVj2f4aGfX0SbqOVrupHGUafIqECQ23G" 

#拼url
url ="%sgrant_type=%s&client_id=%s&client_secret=%s"%(baidu_server,grant_type,client_id,client_secret)
#print(url)
#获取token
response=requests.get(url)
#print(res.text)
res = json.loads(response.content)
token=res['access_token']
#print(token)
#24.b891f76f5d48c0b9587f72e43b726817.2592000.1524124117.282335-10958516

#class MyEncoder(json.JSONEncoder):
#    def default(self, obj):
#        if isinstance(obj, bytes):
#            #return str(obj, encoding='utf-8');
#            return  obj.__str__()
#        return json.JSONEncoder.default(self, obj)
#设置格式
RATE = "16000"
FORMAT = "wav"
CUID="11667418"
DEV_PID=1737

#以字节格式读取文件之后进行编码
FILENAME = r'C:\Users\admin\Documents\Tencent Files\1048517841\FileRecv\01B_01BC020D_ORG.wav'
with open(FILENAME, "rb") as f:
    speech = base64.b64encode(f.read()).decode("utf8")
    
size = os.path.getsize(FILENAME)
headers = { 'Content-Type' : 'application/json'} 
url = "https://vop.baidu.com/server_api"
data={

        "format":FORMAT,
        "rate":RATE,
        "dev_pid":DEV_PID,
        "speech":speech,
        "cuid":CUID,
        "len":size,
        "channel":1,
        "token":token,
    }

req = requests.post(url,json.dumps(data),headers)
result = json.loads(req.text)
print(result["result"][0])