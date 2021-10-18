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

#defining the teams as a list that will hold data of every match as a dictionary
csk = []
kkr = []
dc = []
rcb = []
mi = []
pbks = []
rr = []
srh = []
# './matchLink.txt' contains the all the links to the leaderboards to be considered, links is a list generated
# containing all the required links
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
        chrome.add_cookie(cookie) #adding cookie helps to login the website
    chrome.get(link)

    res=chrome.execute_script("return document.documentElement.outerHTML")
    page=bs(res,'lxml')
    time.sleep(5)             #Change as per expected Internet Speed
    matches = chrome.find_elements(By.CLASS_NAME,"infobarContentLeft_04a34") 
    match = matches[0].text #get the two teams playing the match
    match = match.split()
    team1 = match[0]
    team2 = match[2]
    print(team1,' vs ',team2) 
    teams=chrome.find_elements(By.CLASS_NAME,"playerUserName_1ac16")
    for el in teams:
        team_list.append(el.text) # adds all the usernames to the list
    points =chrome.find_elements(By.CLASS_NAME,"pointInfo_22baf") 
    for el in points:
        if(el.text != "POINTS"): #Dream11 Website 'POINTS' string also included in the same class, so we discard it
            point_list.append(float(el.text)) #adds all the points to the list
 
    res = dict(zip(team_list,point_list)) # Creating a dictionary out of the usernames and their respective points
    # Now appending the created dictionary to the corresponding team lists  
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

def sheetAppend(teamName):      
      count = 0
      for mtchs in teamName:
            if(count == 0 ):
              df = participants.copy(deep=True) 
              count+=1
            df['Match ' +str(count)+ ' Points'] = df['Usernames'].map(mtchs) 
            count+=1   
      df.fillna(0, inplace=True)
      column_list = list(df)
      column_list.remove('Usernames')
      df["Total"] = df[column_list].sum(axis=1)
      df = df.sort_values(by=['Total'], ascending=False)
      with pd.ExcelWriter(participantFile, engine='openpyxl', mode='a') as writer: 
            df.to_excel(writer, sheet_name = str(teamName),index=False)
sheetAppend(mi)
sheetAppend(csk)
sheetAppend(rcb)
sheetAppend(rr)
sheetAppend(kkr)
sheetAppend(pbks)
sheetAppend(srh)
sheetAppend(dc)
