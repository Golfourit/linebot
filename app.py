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
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text 
    if '方舟' in msg:
        message = TextSendMessage(text="__「我要給他們一個終老的家」___"+"\n"+"我們的方舟媽媽謝春蘭女士，為了我們的憨寶貝已經從民國78年忙碌至今了，大家請多多支持阿！！🤗🤗🤗🤗"+"\n"+"如果想做更多公益的也非常歡迎👏到他們官網看更多啦😆😆"+"\n"+"🔗🔗"+"\n"+"https://www.funchao.com.tw/")   
        line_bot_api.reply_message(event.reply_token, message) 
        message = ImageSendMessage(
            original_content_url="https://i.imgur.com/JQmusAr.jpg",
            preview_image_url="https://i.imgur.com/JQmusAr.jpg"
        )   
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
