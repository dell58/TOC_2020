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
                text='trailer'
            ),
            MessageTemplateAction(
                label='Top office',
                text='topoffice'
            ),
            URITemplateAction(
                label='Search',
                uri='https://www.rottentomatoes.com/'
            )
        ]
        )
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)
    return 'OK'