from transitions.extensions import GraphMachine

from utils import send_text_message ,send_image,send_inform


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "go to state1"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        reply_token = event.reply_token
        url = "https://i.imgur.com/tbWMm4D.jpg"
        send_image(reply_token,url)
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")
    
    def is_going_to_inform(self,event)
        text = event.message.text
        return text.lower() == "start"
    
    def on_enter_inform(self,event)
        reply_token = event.reply_token
        send_text_message(reply_token,"top office")
        self.go_back()
        

