from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class PptControllerUsingPadatiousSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
	self.url = "http://135.222.162.94:8001"
	self.file_opened = False

    @intent_file_handler('ppt.controller.intent')
    def handle_ppt_controller_using_padatious(self, message):
        self.speak_dialog('ppt.controller.using.padatious')

    @intent_file_handler('ppt.open.intent')
    def handle_ppt_open(self, message):
	filename = message.data.get("filename")
	self.enclosure.mouth_text("Nova opening file " + filename)
	self.file_opened = True;
	# Send a rest request
	param = {'filename':filename}
	self.enclosure.mouth_text("Sending request to " + self.url);
	#response = requests.get(self.url, param)
	resp = {'filename' : filename}
	#if response.status_code == requests.codes.ok:
        	self.speak_dialog('ppt.open', data=resp)
	#else: 
	#	self.speak_dialog('ppt.filenotfound')

def create_skill():
    return PptControllerUsingPadatiousSkill()

