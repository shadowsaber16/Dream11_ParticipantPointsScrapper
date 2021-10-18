import pickle
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time

import pandas as pd
import numpy as np
from openpyxl import load_workbook

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

csk = []
kkr = []
dc = []
rcb = []
mi = []
pbks = []
rr = []
srh = []

with open('./matchLink.txt') as f:
    links = f.read().splitlines()

for link in links:
    print(link)
    team_list=[]
    point_list=[]
    chrome=webdriver.Chrome()
    cookies=pickle.load(open("cookie.txt","rb"))
    chrome.get("https://www.dream11.com/login")
    for cookie in cookies:
        chrome.add_cookie(cookie)
    chrome.get(link)

    res=chrome.execute_script("return document.documentElement.outerHTML")
    page=bs(res,'lxml')
    time.sleep(5) #Change as per expected Internet Speed
    matches = chrome.find_elements(By.CLASS_NAME,"infobarContentLeft_04a34") 
    match = matches[0].text
    match = match.split()
    team1 = match[0]
    team2 = match[2]
    print(team1,' vs ',team2)
    teams=chrome.find_elements(By.CLASS_NAME,"playerUserName_1ac16")
    for el in teams:
        team_list.append(el.text)
    points =chrome.find_elements(By.CLASS_NAME,"pointInfo_22baf") 
    for el in points:
        if(el.text != "POINTS"):
            point_list.append(float(el.text))

    res = dict(zip(team_list,point_list))

    if(team1 == 'MI' or team2 == 'MI'):
        mi.append(res)
    if(team1 == 'SRH' or team2 == 'SRH'):
        srh.append(res)
    if(team1 == 'CSK' or team2 == 'CSK'):
        csk.append(res)
    if(team1 == 'BLR' or team2 == 'BLR'):
        rcb.append(res)
    if(team1 == 'PBKS' or team2 == 'PBKS'):
        pbks.append(res)
    if(team1 == 'RR' or team2 == 'RR'):
        rr.append(res)
    if(team1 == 'DC' or team2 == 'DC'):
        dc.append(res)
    if(team1 == 'KOL' or team2 == 'KOL'):
        kkr.append(res)

participantFile = ''
particpantSheet = '' 
# Upload a file with participant list, with particpants Usernames listed under the header 'Usernames'
participants = pd.read_excel(participantFile,sheet_name=particpantSheet)
count = 0
for mtchs in mi:
      if(count == 0 ):
        df1 = participants.copy(deep=True) 
        count+=1
      df1['Match ' +str(count)+ ' Points'] = df1['Usernames'].map(mtchs) 
      count+=1   
df1.fillna(0, inplace=True)
column_list = list(df1)
column_list.remove('Usernames')
df1["Total"] = df1[column_list].sum(axis=1)
df1 = df1.sort_values(by=['Total'], ascending=False)
with pd.ExcelWriter(participantFile, engine='openpyxl', mode='a') as writer: 
      df1.to_excel(writer, sheet_name = 'mi',index=False)
count = 0
for mtchs in csk:
      if(count == 0 ):
        df2 = participants.copy(deep=True)
        count+=1
      df2['Match ' +str(count)+ ' Points'] = df2['Usernames'].map(mtchs) 
      count+=1 
df2.fillna(0, inplace=True)
column_list = list(df2)
column_list.remove('Usernames')
df2["Total"] = df2[column_list].sum(axis=1)
df2 = df2.sort_values(by=['Total'], ascending=False)
with pd.ExcelWriter(participantFile, engine='openpyxl', mode='a') as writer:       
      df2.to_excel(writer, sheet_name='csk',index=False)
count = 0
for mtchs in rr:
      if(count == 0 ):
        df3 = participants.copy(deep=True)
        count+=1
      df3['Match ' +str(count)+ ' Points'] = df3['Usernames'].map(mtchs) 
      count+=1
df3.fillna(0, inplace=True)
column_list = list(df3)
column_list.remove('Usernames')
df3["Total"] = df3[column_list].sum(axis=1)
df3 = df3.sort_values(by=['Total'], ascending=False)
with pd.ExcelWriter(participantFile, engine='openpyxl', mode='a') as writer:   
      df3.to_excel(writer, sheet_name='rr',index=False)
count = 0
for mtchs in pbks:
      if(count == 0 ):
        df4 = participants.copy(deep=True) 
        count+=1
      df4['Match ' +str(count)+ ' Points'] = df4['Usernames'].map(mtchs) 
      count+=1
df4.fillna(0, inplace=True)
column_list = list(df4)
column_list.remove('Usernames')
df4["Total"] = df4[column_list].sum(axis=1)
df4 = df4.sort_values(by=['Total'], ascending=False)
with pd.ExcelWriter(participantFile, engine='openpyxl', mode='a') as writer: 
      df4.to_excel(writer, sheet_name='pbks',index=False)
count = 0
for mtchs in rcb:
      if(count == 0 ):
        df5 = participants.copy(deep=True) 
        count+=1
      df5['Match ' +str(count)+ ' Points'] = df5['Usernames'].map(mtchs) 
      count+=1   
df5.fillna(0, inplace=True)
column_list = list(df5)
column_list.remove('Usernames')
df5["Total"] = df5[column_list].sum(axis=1)
df5 = df5.sort_values(by=['Total'], ascending=False)
with pd.ExcelWriter(participantFile, engine='openpyxl', mode='a') as writer: 
      df5.to_excel(writer, sheet_name = 'rcb',index=False)
count = 0
for mtchs in kkr:
      if(count == 0 ):
        df6 = participants.copy(deep=True) 
        count+=1
      df6['Match ' +str(count)+ ' Points'] = df6['Usernames'].map(mtchs) 
      count+=1 
df6.fillna(0, inplace=True)
column_list = list(df6)
column_list.remove('Usernames')
df6["Total"] = df6[column_list].sum(axis=1)
df6 = df6.sort_values(by=['Total'], ascending=False)
with pd.ExcelWriter(participantFile, engine='openpyxl', mode='a') as writer:       
      df6.to_excel(writer, sheet_name='kkr',index=False)
count = 0
for mtchs in srh:
      if(count == 0 ):
        df7 = participants.copy(deep=True) 
        count+=1
      df7['Match ' +str(count)+ ' Points'] = df7['Usernames'].map(mtchs) 
      count+=1
df7.fillna(0, inplace=True)
column_list = list(df7)
column_list.remove('Usernames')
df7["Total"] = df7[column_list].sum(axis=1)
df7 = df7.sort_values(by=['Total'], ascending=False)
with pd.ExcelWriter(participantFile, engine='openpyxl', mode='a') as writer:   
      df7.to_excel(writer, sheet_name='srh',index=False)
count = 0
for mtchs in dc:
      if(count == 0 ):
        df8 = participants.copy(deep=True) 
        count+=1
      df8['Match ' +str(count)+ ' Points'] = df8['Usernames'].map(mtchs) 
      count+=1
df8.fillna(0, inplace=True)
column_list = list(df8)
column_list.remove('Usernames')
df8["Total"] = df8[column_list].sum(axis=1)
df8 = df8.sort_values(by=['Total'], ascending=False)
with pd.ExcelWriter(participantFile, engine='openpyxl', mode='a') as writer: 
      df8.to_excel(writer, sheet_name='dc',index=False)

