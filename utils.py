import os

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


def send_inform(reply_token,url):
    message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url=url,
        title='Menu',
        text='What would you like to watch?',
        actions=[
            PostbackTemplateAction(
                label='Recommend List',
                text='recommend',
                data='action=buy&itemid=1'
            ),
            MessageTemplateAction(
                label='Recommend List',
                text='recommend'
            ),
            URITemplateAction(
                label='Browswer',
                uri='https://www.rottentomatoes.com/'
            )
        ]
        )
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)
    return 'OK'