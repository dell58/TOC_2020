import os
import pandas as pd
from bs4 import BeautifulSoup 

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
    return "OK"


def send_inform_btn(reply_token):
    message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://imgur.com/tbWMm4D',
        title='Menu',
        text='Please select',
        actions=[
            PostbackTemplateAction(
                label='postback',
                text='postback text',
                data='action=buy&itemid=1'
            ),
            MessageTemplateAction(
                label='message',
                text='message text'
            ),
            URITemplateAction(
                label='uri',
                #uri='http://example.com/'
            )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)

def send_list():
    url = 'https://www.rottentomatoes.com/'
    r = requests.get(url)
    web_content = r.text #get the html of the web
    soup = BeautifulSoup(web_content,'html.parser')
    top_office = soup.find("div",id="homepage-top-box-office",class_="listings")
    scores = top_office.find_all("span",class_="tMeterScore")
    scores_num = [e.text for e in scores]
    movies=[]
    for td in top_office.find_all("td",class_="middle_col"):
        name = td.find("a")
        movies.append(name.text)
    dict = {
        "Rating":scores_num,
        "Movie Name":movies
    }
    df  = pd.DataFrame(dict)
    return df
