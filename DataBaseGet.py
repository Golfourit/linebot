#===============這些是LINE提供的功能套組，先用import叫出來=============
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
#===============LINEAPI=============================================
#======這裡是匯入資料庫=====
#import firebase_admin 
from firebase import firebase

url = "https://eggrollbase.firebaseio.com/"
fb = firebase.FirebaseApplication(url, None)
Price = fb.get('/Product', None)
print("資料庫找到以下的價位")
for price in Price:
    print(Price[price]['Name'])
    print(Price[price]['Price'])   

Setting = fb.get('/Settings', None)
print("資料庫找到以下的設定")
for setting in Setting:
    print(Setting[setting]['Type'])
    print(Setting[setting]['Response']) 


#======這裡是匯入資料庫=====
