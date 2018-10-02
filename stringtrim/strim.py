from burp import IBurpExtender
from burp import IIntruderPayloadGenerator
from burp import IIntruderPayloadGeneratorFactory

class BurpExtender(IBurpExtender, IIntruderPayloadGeneratorFactory):
	def registerExtenderCallbacks(self,callbacks):
		self._callbacks = callbacks
		self._helpers = callbacks.getHelpers()
		callbacks.setExtensionName('Recursive String Trimmer')
		callbacks.registerIntruderPayloadGeneratorFactory(self)
		return

	def getGeneratorName(self):
		return "Recursive String Trimmer"
	
	def createNewInstance(self, attack):
		return StringTrimmer(self, attack)

class StringTrimmer(IIntruderPayloadGenerator):
	def __init__(self, extender, attack):
		self._extender = extender
		self._helpers = extender._helpers
		self._attack = attack
		self.trim_len = 0
		self.max_trim = -1
		return
	
	def hasMorePayloads(self):
		return self.trim_len != self.max_trim
	
	def getNextPayload(self, current_payload):
		payload = "".join(chr(x) for x in current_payload)
		if self.max_trim == -1:
			self.max_trim = len(payload)
		payload = self.trim_payload(payload)
		self.trim_len += 1
		return payload
	
	def reset(self):
		self.trim_len = 0
		self.max_trim = -1
		return
	
	def trim_payload(self, original_payload):
		if self.trim_len == 0:
			return original_payload
		return original_payload[:-self.trim_len]
