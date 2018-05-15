import requests
from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.log import getLogger


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
	response = requests.codes.ok
	resp = {'filename' : filename}
	#if response.status_code == requests.codes.ok:
	if response == requests.codes.ok:
        	self.speak_dialog('ppt.open', data=resp)
	else: 
		self.speak_dialog('ppt.filenotfound')

    @intent_file_handler('ppt.next.intent')
    def handle_next_slide(self, message):
	if self.file_opened: 
		# Send a rest request
		nurl = self.url + "/nextpage"
		self.enclosure.mouth_text("Sending request to " + nurl);
		#response = requests.get(nurl)
		response = requests.codes.ok
		#if response.status_code == requests.codes.ok:
		if response == requests.codes.ok:
        		self.speak_dialog('ppt.next')
		else: 
			self.speak_dialog('ppt.filenotfound')
	else: 
		self.speak_dialog('ppt.filenotopen')
	
    @intent_file_handler('ppt.prev.intent')
	if self.file_opened: 
		# Send a rest request
		purl = self.url + "/prevpage"
		self.enclosure.mouth_text("Sending request to " + purl);
		#response = requests.get(purl)
		response = requests.codes.ok
		#if response.status_code == requests.codes.ok:
		if response == requests.codes.ok:
        		self.speak_dialog('ppt.prev')
		else: 
			self.speak_dialog('ppt.filenotfound')
	else: 
		self.speak_dialog('ppt.filenotopen')


    @intent_file_handler('ppt.close.intent')
    def handle_ppt_close(self, message):
	# Send a rest request
	if self.file_opened: 
		purl = self.url + "/close"
		self.enclosure.mouth_text("Sending request to " + purl);
		#response = requests.get(purl)
		response = requests.codes.ok
		#if response.status_code == requests.codes.ok:
		if response == requests.codes.ok:
			self.file_opened = False
        		self.speak_dialog('ppt.close')
		else: 
			self.speak_dialog('ppt.filenotfound')
	else: 
		self.speak_dialog('ppt.filenotopen')

def create_skill():
    return PptControllerUsingPadatiousSkill()

