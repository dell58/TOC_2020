import os
# import requests
# from bs4 import BeautifulSoup
from linebot import LineBotApi, WebhookParser
from linebot.models import *
#MessageEvent, TextMessage, TextSendMessage

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
    return "OK"



def send_image(reply_token,url):
    message = ImageSendMessage(
        original_content_url=url,
        preview_image_url=url
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)
    return 'OK'


def send_inform(reply_token):
    message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://png.pngtree.com/png-clipart/20190419/ourlarge/pngtree-movie-play-button-round-png-image_959268.jpg',
        title='Movies',
        text='What would you like to watch?',
        actions=[
            MessageTemplateAction(
                label='Movie trailer',
                text='Intro.'
            ),
            MessageTemplateAction(
                label='Top office',
                text='Recommend'
            ),
            URITemplateAction(
                label='Order Ticket',
                uri='https://www.vscinemas.com.tw/vsweb/'
            )
        ]
        )
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)
    return 'OK'

# def get_topoffice():
#     url = 'https://www.rottentomatoes.com/'
#     r = requests.get(url)
#     web_content = r.text #get the html of the web
#     soup = BeautifulSoup(web_content,'html.parser')
#     top_office = soup.find("div",id="homepage-top-box-office",class_="listings")
#     movies=[]
#     for td in top_office.find_all("td",class_="middle_col"):
#         name = td.find("a")
#         movies.append(name.text)
#     final_list=""
#     for text in movies:
#         final_list += text + "\n"
#     return final_list