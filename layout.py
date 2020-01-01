# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 09:48:38 2019

@author: dell
"""

from readmap import geodistance,alldata
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.write('## 计算城市之间直线距离的小工具：')

c1 = None
c2 = None

st.sidebar.markdown('请选择第一个城市：')
city_type1 = st.sidebar.selectbox('选择城市类型：',('省', '直辖市', '其他'),key=1,index=1)
if city_type1 == '省':
    p_type = st.sidebar.selectbox('选择省：',list(alldata['provinces'].keys()))
    city = st.sidebar.selectbox('选择市：',list(alldata['provinces'][p_type].keys()))
    c1 = (city,alldata['provinces'][p_type][city])
if city_type1 == '直辖市':
    city = st.sidebar.selectbox('选择市：',list(alldata['municipalities'].keys()))
    c1 = (city,alldata['municipalities'][city])
if city_type1 == '其他':
    city = st.sidebar.selectbox('选择市：',list(alldata['other'].keys()))
    c1 = (city,alldata['other'][city])

st.sidebar.markdown('请选择第二个城市：')
city_type2 = st.sidebar.selectbox('选择城市类型：',('省', '直辖市', '其他'),key=2,index=2)
if city_type2 == '省':
    p_type2 = st.sidebar.selectbox('选择省：',list(alldata['provinces'].keys()),key=2)
    city2 = st.sidebar.selectbox('选择市：',list(alldata['provinces'][p_type2].keys()),key=2)
    c2 = (city2,alldata['provinces'][p_type2][city2])
if city_type2 == '直辖市':
    city2 = st.sidebar.selectbox('选择市：',list(alldata['municipalities'].keys()),key=2)
    c2 = (city2,alldata['municipalities'][city2])
if city_type2 == '其他':
    city2 = st.sidebar.selectbox('选择市：',list(alldata['other'].keys()),key=2)
    c2 = (city2,alldata['other'][city2])

st.write('选择的第一个城市是:`',c1[0],'`对应的经纬度是：',c1[1])
st.write('选择的第二个城市是:`',c2[0],'`对应的经纬度是：',c2[1])
st.write('两个城市之间的直线距离是：',geodistance(c1[1][0],c1[1][1],c2[1][0],c2[1][1]),'km')
#绘制地图
st.sidebar.markdown('请设置地图样式：')
style = st.sidebar.selectbox('选择地图种类：',['open-street-map','outdoors','light','dark','satellite-streets',
                                'stamen-terrain','stamen-toner','stamen-watercolor'])
pitch = st.sidebar.slider('设定地图俯视角度', 0, 60, 30)
bearing = st.sidebar.slider('设定地图旋转角度', 0, 360, 0)
df = pd.DataFrame([[c1[1][1],c1[1][0],c1[0]],[c2[1][1],c2[1][0],c2[0]]],columns=['lat', 'lon','City'])
#st.write(df)
token = 'pk.eyJ1IjoiZG9uZ3poaXhpYW8iLCJhIjoiY2szeWFvNmtuMGs0bDNqczhneXJhZXdiciJ9.NyUcokTjJeoQxTNowsonkg'
fig = go.Figure(go.Scattermapbox(
    mode = "markers+lines",
    lon = [c1[1][0], c2[1][0]],
    lat = [c1[1][1], c2[1][1]],
    hovertext = [c1[0],c2[0]],
    marker = {'size': 10}))
fig.update_layout(
    margin ={'l':100,'t':0,'b':0,'r':100},
    mapbox = {
        'center': {'lon': (c1[1][0]+c2[1][0])/2, 'lat': (c1[1][1]+c2[1][1])/2},
        'pitch': pitch,
        'bearing':bearing,
        'style': style,
        'accesstoken':token,
        'zoom': 3})
st.plotly_chart(fig)