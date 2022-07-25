class Viber:
    chat = {}

    @classmethod
    def add_message(cls, msg):
        cls.chat[id(msg)] = msg

    @classmethod
    def remove_message(cls, msg):
        key = id(msg)
        if key in cls.chat:
            cls.chat.pop(id(msg))

    @classmethod
    def set_like(cls, msg):
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls, num):
        for m in tuple(cls.chat.values())[-num:]:
            print(m, end=' ')

    @classmethod
    def total_messages(cls):
        return len(cls.chat)


class Message:
    def __init__(self, text):
        self.text = text
        self.fl_like = False

msg = Message("Всем привет!")
Viber.add_message(msg)
print(msg.fl_like, msg.text)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)