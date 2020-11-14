from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('a18WRYNQJzy6om4CV42l50x96M/Bq3nPsKuAHPujEB+NFSI2anS/NBRvX23BCsAeENNkQ8XpaO7WYlQkAWk0/GZ0rXFIgXQQglRTRUKGD2dzlE5Z0KNR1xt7ZSzs/kLm9kH6qFhgqPm8HdQC+ijltQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('5ed0356366d6964f2c6af2d55147b790')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage,message1=TextMessage)
def handle_message(event):
    msg = event.message.text 
    #massage1 =TextMessage #
     #if ('方舟' or '方舟啟智教養院' or '教養院') in msg:
       #   message =ImageSendMessage(
        #   original_content_url="https://www.bing.com/images/search?view=detailV2&insightstoken=bcid_S7TDN7lXjAgCO7LYxM.kuLSQ1mDF.....3M*ccid_tMM3uVeM&form=ANCMS1&iss=SBIUPLOADGET&selectedindex=0&id=-1937829305&ccid=tMM3uVeM&exph=600&expw=348&vt=2&sim=11",
         #  preview_image_url="https://www.bing.com/images/search?view=detailV2&insightstoken=bcid_S7TDN7lXjAgCO7LYxM.kuLSQ1mDF.....3M*ccid_tMM3uVeM&form=ANCMS1&iss=SBIUPLOADGET&selectedindex=0&id=-1937829305&ccid=tMM3uVeM&exph=600&expw=348&vt=2&sim=11"
        #)
       # line_bot_api.reply_message(event.reply_token, message)
    if '方舟' in msg:
        message = TextSendMessage(text="__「我要給他們一個終老的家」___"+"\n"+"我們的方舟媽媽謝春蘭女士，為了我們的憨寶貝已經從民國78年忙碌至今了，大家請多多支持阿！！🤗🤗🤗🤗"+"\n"+"如果想做更多公益的也非常歡迎👏到他們官網看更多啦😆😆"+"\n"+"🔗🔗"+"\n"+"https://www.funchao.com.tw/")      
        line_bot_api.reply_message(event.reply_token, message)  
    elif '貓咪' in msg:
        message =ImageSendMessage(
           original_content_url="data:image/jpeg;base64,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",
           preview_image_url="data:image/jpeg;base64,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" )
           line_bot_api.reply_message(event.reply_token, message)        
    elif '啟智教養院' in msg:
        message = TextSendMessage(text="__「我要給他們一個終老的家」___"+"\n"+"我們的方舟媽媽謝春蘭女士，為了我們的憨寶貝已經從民國78年忙碌至今了，大家請多多支持阿！！🤗🤗🤗🤗"+"\n"+"如果想做更多公益的也非常歡迎👏到他們官網看更多啦😆😆"+"\n"+"🔗🔗"+"\n"+"https://www.funchao.com.tw/")
        line_bot_api.reply_message(event.reply_token, message)  
    elif  '教養院' in msg:
        message = TextSendMessage(text="__「我要給他們一個終老的家」___"+"\n"+"我們的方舟媽媽謝春蘭女士，為了我們的憨寶貝已經從民國78年忙碌至今了，大家請多多支持阿！！🤗🤗🤗🤗"+"\n"+"如果想做更多公益的也非常歡迎👏到他們官網看更多啦😆😆"+"\n"+"🔗🔗"+"\n"+"https://www.funchao.com.tw/")
        line_bot_api.reply_message(event.reply_token, message)  
    elif  'help' in msg:
        message = TextSendMessage(text="本系統可以自動回覆一般基本疑問。"+"\n"+"稍微複雜的疑問，則會由客服人員為您回覆。"+"\n"+"您可以立即詢問以下問題，例如："+"\n"+"・營業時間？"+"\n"+"・可刷卡嗎？"+"\n"+"・我要預約"+"\n"+"・推薦菜色？"+"\n"+"・店家地址？"+"\n"+"・消費價位？"+"\n"+"・最近車站？"+"\n"+"・店家網站？"+"\n"+"・可吸菸嗎？")
        line_bot_api.reply_message(event.reply_token, message)
    elif  '設定' in msg:
        message = TextSendMessage(text="本系統可以自動回覆一般基本疑問。"+"\n"+"稍微複雜的疑問，則會由客服人員為您回覆。"+"\n"+"您可以立即詢問以下問題，例如："+"\n"+"・營業時間？"+"\n"+"・可刷卡嗎？"+"\n"+"・我要預約"+"\n"+"・推薦菜色？"+"\n"+"・店家地址？"+"\n"+"・消費價位？"+"\n"+"・最近車站？"+"\n"+"・店家網站？"+"\n"+"・可吸菸嗎？")
        line_bot_api.reply_message(event.reply_token, message)
    elif '營業' in msg:
        message = TextSendMessage(text="😼ㄟ果肉蛋捲✖️The Naivest 🤤"+"\n"+"目前採線上商店經營，全天候都有營業呦！😼")
        line_bot_api.reply_message(event.reply_token, message)
    elif '時間' in msg:
        message = TextSendMessage(text="😼ㄟ果肉蛋捲✖️The Naivest 🤤"+"\n"+"目前採線上商店經營，全天候都有營業呦！😼")
        line_bot_api.reply_message(event.reply_token, message)
    elif '刷卡' in msg:
        message = TextSendMessage(text="我們付款方式有郵匯跟現金付款！"+"\n"+"郵匯的話可以到我們的訂購單看匯款的帳號呦！"+"\n"+"🤤訂購單在這👇https://docs.google.com/forms/d/e/1FAIpQLScdbpfT8a5uaLut0o7O2kO_N0m9xnrv7O49gVBBdRwMNk16SA/viewform")
        line_bot_api.reply_message(event.reply_token, message)
    elif '預約' in msg:
        message = TextSendMessage(text="如果你有任何需要提前作業的需求都可以跟我們說～～會盡力滿足你的🥰🥰")
        line_bot_api.reply_message(event.reply_token, message)
    elif '推薦' in msg:   
        message = TextSendMessage(text="說到推薦的 我們當然是推薦我們的蛋捲ㄚ！！🤣🤣"+"\n"+"有興趣可以去我們官網看看呦！連結在這！！https://handmade-eggroll-3.jimdosite.com/"+"\n"+"也可以直接去訂購單看看ㄛ！https://docs.google.com/forms/d/e/1FAIpQLScdbpfT8a5uaLut0o7O2kO_N0m9xnrv7O49gVBBdRwMNk16SA/viewform"+"\n"+"我們除了line也有粉專~~"+"\n"+"Ig :https://instagram.com/handmade_eggroll?igshid=12wh42cyy9hlz"+"\n"+"Fb :https://m.facebook.com/ㄟ果肉-The-naivest-手工蛋捲-114153793616901"+"ㄟ果肉蛋捲✖️The Naivest有任何問題都可以直接傳訊息通知我們～～我們都會盡快為你服務呦😙😙")
        line_bot_api.reply_message(event.reply_token, message)
    elif '菜色' in msg:   
        message = TextSendMessage(text="說到推薦的 我們當然是推薦我們的蛋捲ㄚ！！🤣🤣"+"\n"+"有興趣可以去我們官網看看呦！連結在這！！https://handmade-eggroll-3.jimdosite.com/"+"\n"+"也可以直接去訂購單看看ㄛ！https://docs.google.com/forms/d/e/1FAIpQLScdbpfT8a5uaLut0o7O2kO_N0m9xnrv7O49gVBBdRwMNk16SA/viewform"+"\n"+"我們除了line也有粉專~~"+"\n"+"Ig :https://instagram.com/handmade_eggroll?igshid=12wh42cyy9hlz"+"\n"+"Fb :https://m.facebook.com/ㄟ果肉-The-naivest-手工蛋捲-114153793616901"+"ㄟ果肉蛋捲✖️The Naivest有任何問題都可以直接傳訊息通知我們～～我們都會盡快為你服務呦😙😙")
        line_bot_api.reply_message(event.reply_token, message)
    elif '地址' in msg:
        message = TextSendMessage(text="我們ㄟ果肉蛋捲商店的大本營你們想知道嗎🤣🤣"+"\n"+"目前設立在中原大學-力行宿舍呦！想找我們的可以來看看ㄛ😝😝😝"+"\n"+"https://goo.gl/maps/6B8AyEmgUyvg7jeU7")
        line_bot_api.reply_message(event.reply_token, message)
    elif '價位' in msg:
        message = TextSendMessage(text="說到這個～～"+"\n"+"ㄟ果肉蛋捲✖️The Naivest 😉\n"+"蛋捲我本人要給你看看我們設計的海報啦！！有包刮價錢、口味、訂購單QRcode!快來看看吧"+"\n"+"可以到我們的訂購單看看～"+"\n"+"🔗https://docs.google.com/forms/d/e/1FAIpQLScdbpfT8a5uaLut0o7O2kO_N0m9xnrv7O49gVBBdRwMNk16SA/viewform"+"\n"+"還有IG.FB呦！"+"\n"+"🔗IG:https://instagram.com/handmade_eggroll?igshid=64g5czfwa23l"+"\n"+"🔗FB:https://m.facebook.com/ㄟ果肉-The-naivest-手工蛋捲-11415379361690")
        line_bot_api.reply_message(event.reply_token, message)   
    elif '車站' in msg:
        message = TextSendMessage(text="我們ㄟ果肉商店最近的車站就是中壢火車站呦！"+"\n"+"俗話說麻雀雖小，五臟俱全。"+"\n"+"中壢車站常常有人說他很小很醜～但其實他確實蠻重要的一個車站呢！長知識了💪🧠🧠"+"\n"+"Google地圖🔗👇👇"+"\n"+"中壢車站"+"\n"+"https://goo.gl/maps/rB5nPDYyKyKNb6q4A")
        line_bot_api.reply_message(event.reply_token, message)    
    elif '網站' in msg:
        message = TextSendMessage(text="我們官網的連結在這！有興趣的都歡迎上來看看喔～～👏"+"\n"+"🔗🔗"+"https://handmade-eggroll-3.jimdosite.com/")
        line_bot_api.reply_message(event.reply_token, message)     
    elif '官網' in msg:
        message = TextSendMessage(text="我們官網的連結在這！有興趣的都歡迎上來看看喔～～👏"+"\n"+"🔗🔗"+"https://handmade-eggroll-3.jimdosite.com/")
        line_bot_api.reply_message(event.reply_token, message) 
    elif '官方網站' in msg:
        message = TextSendMessage(text="我們官網的連結在這！有興趣的都歡迎上來看看喔～～👏"+"\n"+"🔗🔗"+"https://handmade-eggroll-3.jimdosite.com/")
        line_bot_api.reply_message(event.reply_token, message) 
    elif '吸菸' in msg:
        message = TextSendMessage(text="吸菸傷身又不環保"+"\n"+"不如來吃蛋捲吧！好吃😋又便宜！"+"\n"+"心動不如馬上行動！😝😝")
        line_bot_api.reply_message(event.reply_token, message)  
    elif '掰' in msg:
        message = TextSendMessage(text="掰掰👋記得有空回來找我喔～～")
        line_bot_api.reply_message(event.reply_token, message)  
    elif '8' in msg:
        message = TextSendMessage(text="掰掰👋記得有空回來找我喔～～")
        line_bot_api.reply_message(event.reply_token, message)  
    elif 'bye' in msg:
        message = TextSendMessage(text="掰掰👋記得有空回來找我喔～～")
        line_bot_api.reply_message(event.reply_token, message) 
    elif '先走' in msg:
        message = TextSendMessage(text="掰掰👋記得有空回來找我喔～～")
        line_bot_api.reply_message(event.reply_token, message) 
    elif '再見' in msg:
       message = TextSendMessage(text="掰掰👋記得有空回來找我喔～～")
       line_bot_api.reply_message(event.reply_token, message)       
    #elif '合作' in msg:
       # message = imagemap_message()
       # line_bot_api.reply_message(event.reply_token, message)
    #elif '活動' in msg:
    #    message = buttons_message()
    #    line_bot_api.reply_message(event.reply_token, message)
    #elif '註冊會員' in msg:
    #    message = Confirm_Template()
    #    line_bot_api.reply_message(event.reply_token, message)
    #elif '旋轉木馬' in msg:
    #    message = Carousel_Template()
     #   line_bot_api.reply_message(event.reply_token, message)
    #elif '圖片畫廊' in msg:
     #   message = test()
    #    line_bot_api.reply_message(event.reply_token, message)
   # elif '功能列表' in msg:
    #    message = function_list()
     #   line_bot_api.reply_message(event.reply_token, message) 
    else:
        message = TextSendMessage(text="本系統可以自動回覆一般基本疑問。"+"\n"+"稍微複雜的疑問，則會由客服人員為您回覆。"+"\n"+"您可以立即詢問以下問題，例如："+"\n"+"・營業時間？"+"\n"+"・可刷卡嗎？"+"\n"+"・我要預約"+"\n"+"・推薦菜色？"+"\n"+"・店家地址？"+"\n"+"・消費價位？"+"\n"+"・最近車站？"+"\n"+"・店家網站？"+"\n"+"・可吸菸嗎？")
        line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
