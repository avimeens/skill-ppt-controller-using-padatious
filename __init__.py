from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class PptControllerUsingPadatiousSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder().require('PptControllerUsingPadatious'))
    def handle_ppt_controller_using_padatious(self, message):
        self.speak_dialog('ppt.controller.using.padatious')


def create_skill():
    return PptControllerUsingPadatiousSkill()

