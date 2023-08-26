from bs4 import BeautifulSoup as bs
import requests as r
import os
import numpy as np
import pandas as pd
import datetime as dt
import urllib.request
import time
dics=[]
smallest_year=2016
biggest_year=2023
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

########################################################################    
def select_date():
    while True:
        try:
            syear=int(input("enter start year between {} and {}".format(smallest_year,biggest_year)))
            if smallest_year<=syear<=biggest_year:
                break
            else:
                print("enter valid year")
        except:
            print("enter valid year")
        
    while True:
        try:
            smonth=int(input("enter start month between 1 and 12"))
            if 1<=smonth<=12:
                break
            else:
                print("enter valid month")
        except:
            print("enter valid month")        
    
    if smonth in [1,3,5,7,8,10,12]:
        while True:
            try:
                sday=int(input("enter start day between 1 and 31"))
                if 1<=sday<=31:
                    break
                else:
                    print("enter valid day")
            except:
                print("enter valid day")        
       
               
    if smonth in [4,6,9,11]:
        while True:
            try:
                sday=int(input("enter start day between 1 and 30"))
                if 1<=sday<=30:
                    break
                else:
                    print("enter valid day")
            except:
                print("enter valid day")
                        
    if smonth ==2 and syear%4==0:
        while True:
            try:
                sday=int(input("enter start day between 1 and 29"))
                if 1<=sday<=29:
                    break
                else:
                    print("enter valid day")
            except:
                print("enter valid day")        
    if smonth ==2 and syear%4!=0:
        while True:
            try:
                sday=int(input("enter start day between 1 and 28"))
                if 1<=sday<=28:
                    break
                else:
                    print("enter valid day")
            except:
                print("enter valid day")
        ##from here we get end date#

    while True:
        try:
            eyear=int(input("enter end year between {} and {}".format(syear,biggest_year)))
            if syear<=eyear<=2023:
                break
            else:
                print("enter valid year")
        except:
                print("enter valid year")        
    if eyear==syear:    
        while True:
            try:
                emonth=int(input("enter end month between {} and 12".format(smonth)))
                if smonth<=emonth<=12:
                    break
                else:
                    print("enter valid month")
            except:
                print("enter valid month")        

    if eyear>syear:    
        while True:
            try:
                emonth=int(input("enter end month between 1 and 12"))
                if 1<=emonth<=12:
                    break
                else:
                    print("enter valid month")
            except:
                print("enter valid month")          
###############################################################################################
    if emonth in [1,3,5,7,8,10,12] and eyear>syear:
        while True:
            try:
                eday=int(input("enter end day between 1 and 31"))
                if 1<=eday<=31:
                    break
                else:
                    print("enter valid day")
            except:
                print("enter valid day")
    if emonth in [4,6,9,11] and eyear>syear:
        while True:
            try:
                eday=int(input("enter end day between 1 and 30"))
                if 1<=eday<=30:
                    break
                else:
                    print("enter valid day")
            except:
                print("enter valid day")
    if emonth ==2 and eyear%4==0 and eyear>syear:
        while True:
            try:
                eday=int(input("enter end day between 1 and 29"))
                if 1<=eday<=29:
                    break
                else:
                    print("enter valid day")
            except:
                print("enter valid day")
    if emonth ==2 and eyear%4!=0 and eyear>syear:
        while True:
            try:
                eday=int(input("enter end day between 1 and 28"))
                if 1<=eday<=28:
                    break
                else:
                    print("enter valid day")
            except:
                print("enter valid day")
##########################################################################
    if emonth in [1,3,5,7,8,10,12] and eyear==syear and emonth>smonth:
        while True:
            try:
                eday=int(input("enter end day between 1 and 31"))
                if 1<=eday<=31:
                    break
                else:
                    print("enter valid day")
            except:
                print("enter valid day")
    if emonth in [4,6,9,11] and eyear==syear and emonth>smonth:
        while True:
            try:
                eday=int(input("enter end day between 1 and 30"))
                if 1<=eday<=30:
                    break
                else:
                    print("enter valid day")
            except:
                print("enter valid day")
    if emonth ==2 and eyear%4==0 and eyear==syear and emonth>smonth:
        while True:
            try:
                eday=int(input("enter end day between 1 and 29"))
                if 1<=eday<=29:
                    break
                else:
                    print("enter valid day")
            except:
                print("enter valid day")
    if emonth ==2 and eyear%4!=0 and eyear==syear and emonth>smonth:
        while True:
            try:
                eday=int(input("enter end day between 1 and 28"))
                if 1<=eday<=28:
                    break
                else:
                    print("enter valid day")
            except:
                print("enter valid day")


##########################################################################
    if emonth in [1,3,5,7,8,10,12] and emonth==smonth and eyear==syear:
        while True:
            try:
                eday=int(input("enter end day between {} and 31".format(sday)))
                if sday<=eday<=31:
                    break
                else:
                    print("enter valid day")
            except:
                print("enter valid day")
    if emonth in [4,6,9,11] and emonth==smonth and eyear==syear:
        while True:
            try:
                eday=int(input("enter end day between {} and 30".format(sday)))
                if sday<=eday<=30:
                    break
                else:
                    print("enter valid day")
            except:
                print("enter valid day")
    if emonth ==2 and eyear%4==0 and emonth==smonth and eyear==syear:
        while True:
            try:
                eday=int(input("enter end day between {} and 29".format(sday)))
                if sday<=eday<=29:
                    break
                else:
                    print("enter valid day")
            except:
                print("enter valid day")
    if emonth ==2 and eyear%4!=0 and emonth==smonth and eyear==syear:
        while True:
            try:
                eday=int(input("enter end day between {} and 28".format(sday)))
                if sday<=eday<=28:
                    break
                else:
                    print("enter valid day")            
            except:
                print("enter valid day")
    return syear,smonth,sday,eyear,emonth,eday

###############################################################################
def trans_date(syear,smonth,sday,eyear,emonth,eday):
    runs=dt.datetime(eyear,emonth,eday)-dt.datetime(syear,smonth,sday)
    if runs.days==0:
        runs=runs.days+1
    else:
        runs=runs.days+1
    start_date=dt.datetime(syear,smonth,sday)
    return start_date,runs
##################################################################################
def scrape(start_date,runs):
    for i in range(runs):
    
        date=start_date.strftime("20%y-%m-%d")
        source = r.get("https://www.thesportsman.com/football/results/{}".format(date))
        page=source.content
        soup=bs(page,"lxml")
        target=soup.find_all("div",class_="flc-comp-contain")
        if len(target)==0:
            country="-"
            league="-"
            team_a="-"
            team_b="-"
            team_a_s="-"
            team_b_s="-"
            status="-"
            penalties="-"
            dics.append({"date":date,"region":country,"league":league,"team_a":team_a,"team_b":team_b,
                         "team_a_score":team_a_s,"team_b_score":team_b_s,"status":status,"penalties":penalties})
        else:
            for i in range(len(target)):
                country=target[i].find("div",class_="flc-comp-title").contents[0].text.strip()
                league=target[i].find("div",class_="flc-comp-title").contents[1].text.strip()
                matches=target[i].find_all("div",class_="flc-match-item-v2")
                for ii in range(len(matches)):
                    try:
                        status=matches[ii].find("div",class_="left").contents[1].text.strip()
                    except IndexError:
                        status="NA"    
                    team_a=matches[ii].find("div",class_="left").contents[0].text.strip()
                    team_b=matches[ii].find("div",class_="right").contents[0].text.strip()
                    try:
                        team_a_s=matches[ii].find("div",class_="l-score").text.strip()
                    except AttributeError:
                        team_a_s="NA"

                    try:        
                        team_b_s=matches[ii].find("div",class_="r-score").text.strip()
                    except AttributeError:
                        team_b_s="NA"   
                    try:
                        penalties=matches[ii].find("div",class_="flc-middle flc-match-has-pens").text.strip()
                    except:
                        penalties="NA"         
                    dics.append({"date":date,"region":country,"league":league,"team_a":team_a,"team_b":team_b,
                         "team_a_score":team_a_s,"team_b_score":team_b_s,"status":status,"penalties":penalties})
        start_date+=dt.timedelta(1)
######################################################################################
def df():
    daf=pd.DataFrame(dics)
    x=input("do you want to see a randome sample the mathces yes/no").lower()
    while True:
        if x=="yes":
            if daf.shape[0]<5:
                while True:
                    if x =="yes":
                        print(daf.sample(1))
                        x=input("do you want to see another randome sample the mathces yes/no").lower()
                    elif x=="no":
                        break
                    else:
                        print("please enter yes or no")
            else:
                while True:
                    if x =="yes":
                        print(daf.sample(5))
                        x=input("do you want to see another randome sample the mathces yes/no").lower()
                    elif x=="no":
                        break
                    else:
                        x=input("please enter yes or no").lower()
        elif x=="no":
            break
        else:
            x=input("please enter yes or no").lower()

    return daf            
###############################################################################################
def csv(df,syear,smonth,sday,eyear,emonth,eday):
    while True:
        x=input("do you like to creat a csv? yes/no").lower()
        if x=="yes":
            df.to_csv(f"form{syear}-{smonth}-{sday} to {eyear}-{emonth}-{eday}.csv")
            break
        elif x=="no":
            break
        else:
            print("please enter yes or no")


                    
###################################################################################################
def main():
    if connect():
        print("welcome to soccer matches web scraper".title())
        syear,smonth,sday,eyear,emonth,eday=select_date()
        start_date,runs=trans_date(syear,smonth,sday,eyear,emonth,eday)
        scrape(start_date,runs)
        daf=df()
        csv(daf,syear,smonth,sday,eyear,emonth,eday)
        
    else:
        print("please connect to the internet and try again")
        print("close in")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("0")


def restart():

    while True:
        restart=input("do you want to rerun? yes/no").lower()
        if restart=="yes":
            main()

        if restart=="no":
            break

        if restart not in ["yes","no"]:
            print("please enter yes or no")             

if __name__=="__main__":
        try:
            main()
            restart()
        except:
            print("please connect to the internet and try again")
            print("close in")
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            print("0")
            restart()       
                
