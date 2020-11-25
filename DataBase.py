#===============這些是LINE提供的功能套組，先用import叫出來=============
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
#===============LINEAPI=============================================
#======這裡是匯入資料庫=====
#import firebase_admin 
from firebase import firebase
Product = [{"Name": "原味蛋捲" , "Price": 40},
{"Name": "芝麻蛋捲" , "Price": 40},
{"Name": "牛奶蛋捲" , "Price": 45}         
]

Settings =[{"Type": "營業時間" , "Response": "😼ㄟ果肉蛋捲✖️The Naivest 🤤 目前採線上商店經營，全天候都有營業呦！😼"},
{"Type": "可刷卡嗎" , "Response": "我們付款方式有郵匯跟現金付款！ 郵匯的話可以到我們的訂購單看匯款的帳號呦！ 🤤訂購單在這👇https://docs.google.com/forms/d/e/1FAIpQLScdbpfT8a5uaLut0o7O2kO_N0m9xnrv7O49gVBBdRwMNk16SA/viewform"},
{"Type": "我要預約" , "Response": "如果你有任何需要提前作業的需求都可以跟我們說～～會盡力滿足你的🥰🥰"},
{"Type": "推薦菜色" , "Response": "說到推薦的 我們當然是推薦我們的蛋捲ㄚ！！🤣🤣 有興趣可以去我們官網看看呦！連結在這！！https://handmade-eggroll-3.jimdosite.com/ 也可以直接去訂購單看看ㄛ！https://docs.google.com/forms/d/e/1FAIpQLScdbpfT8a5uaLut0o7O2kO_N0m9xnrv7O49gVBBdRwMNk16SA/viewform"+"\n"+"我們除了line也有粉專~~"+"\n"+"Ig :https://instagram.com/handmade_eggroll?igshid=12wh42cyy9hlz"+"\n"+"Fb :https://m.facebook.com/ㄟ果肉-The-naivest-手工蛋捲-114153793616901"+"ㄟ果肉蛋捲✖️The Naivest有任何問題都可以直接傳訊息通知我們～～我們都會盡快為你服務呦😙😙"},
{"Type": "店家地址" , "Response": "我們ㄟ果肉蛋捲商店的大本營你們想知道嗎🤣🤣 目前設立在中原大學-力行宿舍呦！想找我們的可以來看看ㄛ😝😝😝 https://goo.gl/maps/6B8AyEmgUyvg7jeU7"},
{"Type": "消費價位" , "Response": "說到這個～～"+"\n"+"ㄟ果肉蛋捲✖️The Naivest 😉 蛋捲我本人要給你看看我們設計的海報啦！！有包刮價錢、口味、訂購單QRcode!快來看看吧 可以到我們的訂購單看看～ 🔗https://docs.google.com/forms/d/e/1FAIpQLScdbpfT8a5uaLut0o7O2kO_N0m9xnrv7O49gVBBdRwMNk16SA/viewform 還有IG.FB呦！ 🔗IG:https://instagram.com/handmade_eggroll?igshid=64g5czfwa23l 🔗FB:https://m.facebook.com/ㄟ果肉-The-naivest-手工蛋捲-114153793616901"},
{"Type": "最近車站" , "Response": "我們ㄟ果肉商店最近的車站就是中壢火車站呦！ 俗話說麻雀雖小，五臟俱全。 中壢車站常常有人說他很小很醜～但其實他確實蠻重要的一個車站呢！長知識了💪🧠🧠 Google地圖🔗👇👇 中壢車站 https://goo.gl/maps/rB5nPDYyKyKNb6q4A"},
{"Type": "店家網站" , "Response": "我們官網的連結在這！有興趣的都歡迎上來看看喔～～👏 🔗🔗 https://handmade-eggroll-3.jimdosite.com/"},
{"Type": "可吸菸嗎" , "Response": "吸菸傷身又不環保 不如來吃蛋捲吧！好吃😋又便宜！ 心動不如馬上行動！😝😝"}
]
url = "https://eggrollbase.firebaseio.com/"
fb = firebase.FirebaseApplication(url, None)

for NamePrice in Product:
    fb.post("/Product", NamePrice)
    print("{} 儲存完畢".format(NamePrice))

for Setting in Settings:
    fb.post("/Settings", Setting)
    print("{} 儲存完畢".format(Setting))
#======這裡是匯入資料庫=====
