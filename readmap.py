import demjson
import json
from math import radians, cos, sin, asin, sqrt

def geodistance(lng1,lat1,lng2,lat2):
    #lng1,lat1,lng2,lat2 = (120.12802999999997,30.28708,115.86572000000001,28.7427)
    lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)]) # 经纬度转换成弧度
    dlon=lng2-lng1
    dlat=lat2-lat1
    a=sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    distance=2*asin(sqrt(a))*6371*1000 # 地球平均半径，6371km
    distance=round(distance/1000,3)
    return distance

def getV(l):
    rd = {}
    for i in l:
        k = i['n']
        v = i['g'].split(',')
        v = (float(v[0]),float(v[1].split('|')[0]))
        rd[k]=v
    return rd

def getP(l):
    rd = {}
    for i in l:
        k = i['n']
        v = getV(i['cities'])
        rd[k]=v
    return rd

with open('BaiduMap_cityCenter.txt','r',encoding='utf-8') as f:
    w = f.read()
    temp = demjson.decode(w)
    
alldata = {}
alldata['municipalities'] = getV(temp['municipalities'])
alldata['other']= getV(temp['other'])
alldata['provinces']= getP(temp['provinces'])  

