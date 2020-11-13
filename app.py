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
     #if ('方舟' or '方舟啟智教養院' or '教養院') in msg:
       #   message =ImageSendMessage(
        #   original_content_url="https://www.bing.com/images/search?view=detailV2&insightstoken=bcid_S7TDN7lXjAgCO7LYxM.kuLSQ1mDF.....3M*ccid_tMM3uVeM&form=ANCMS1&iss=SBIUPLOADGET&selectedindex=0&id=-1937829305&ccid=tMM3uVeM&exph=600&expw=348&vt=2&sim=11",
         #  preview_image_url="https://www.bing.com/images/search?view=detailV2&insightstoken=bcid_S7TDN7lXjAgCO7LYxM.kuLSQ1mDF.....3M*ccid_tMM3uVeM&form=ANCMS1&iss=SBIUPLOADGET&selectedindex=0&id=-1937829305&ccid=tMM3uVeM&exph=600&expw=348&vt=2&sim=11"
        #)
       # line_bot_api.reply_message(event.reply_token, message)
    if '方舟' in msg:
        message = TextSendMessage(text="__「我要給他們一個終老的家」___"+"\n"+"我們的方舟媽媽謝春蘭女士，為了我們的憨寶貝已經從民國78年忙碌至今了，大家請多多支持阿！！🤗🤗🤗🤗"+"\n"+"如果想做更多公益的也非常歡迎👏到他們官網看更多啦😆😆"+"\n"+"🔗🔗"+"\n"+"https://www.funchao.com.tw/")
        line_bot_api.reply_message(event.reply_token, message)  
        message =ImageSendMessage(
        original_content_url="https://www.bing.com/images/blob?bcid=S7TDN7lXjAgCO7LYxM.kuLSQ1mDF.....3M",
        preview_image_url="https://www.bing.com/images/blob?bcid=S7TDN7lXjAgCO7LYxM.kuLSQ1mDF.....3M"
        )
        line_bot_api.reply_message(event.reply_token, message)    
    elif '啟智教養院' in msg:
        message = TextSendMessage(text="__「我要給他們一個終老的家」___"+"\n"+"我們的方舟媽媽謝春蘭女士，為了我們的憨寶貝已經從民國78年忙碌至今了，大家請多多支持阿！！🤗🤗🤗🤗"+"\n"+"如果想做更多公益的也非常歡迎👏到他們官網看更多啦😆😆"+"\n"+"🔗🔗"+"\n"+"https://www.funchao.com.tw/")
        line_bot_api.reply_message(event.reply_token, message)  
    elif  '教養院' in msg:
        message = TextSendMessage(text="__「我要給他們一個終老的家」___"+"\n"+"我們的方舟媽媽謝春蘭女士，為了我們的憨寶貝已經從民國78年忙碌至今了，大家請多多支持阿！！🤗🤗🤗🤗"+"\n"+"如果想做更多公益的也非常歡迎👏到他們官網看更多啦😆😆"+"\n"+"🔗🔗"+"\n"+"https://www.funchao.com.tw/")
        line_bot_api.reply_message(event.reply_token, message)  
    elif  '合作' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '活動' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '註冊會員' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '旋轉木馬' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '圖片畫廊' in msg:
        message = test()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能列表' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message) 
    else:
        message = TextSendMessage(text="呵呵想不到吧~還沒設定只能學你說話"+msg)
        line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
