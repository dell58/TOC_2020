from transitions.extensions import GraphMachine

from utils import send_text_message,send_inform_btn


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_video(self, event):
        text = event.message.text
        return text.lower() == "video"

    def is_going_to_recommend(self, event):
        text = event.message.text
        return text.lower() == "recommend"

    def on_enter_video(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "video Trending")
        self.go_back()

    def on_exit_video(self):
        print("Leaving video")

    def on_enter_recommend(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "Recommend list")
        self.go_back()

    def on_exit_recommend(self):
        print("Leaving recommend")
    
    def  on_enter_inform(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token,"What would you like to watch?")
        send_inform_btn(reply_token)

