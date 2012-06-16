from utilities import Utilities
import time

class WADebug():
	
	def __init__(self):
		self.enabled = True
		
		cname = self.__class__.__name__
		self.type= cname[:cname.index("Debug")]
		
	
	@staticmethod
	def stdDebug(message,messageType="General"):
		enabledTypes = ["general","sql","conn"];
		allowAll = True
		if allowAll or messageType.lower() in enabledTypes:
			print message;
	
	def formatMessage(self,message):
		#default = "{type}:{time}:\t{message}"
		t = time.time()
		message = "%s:\t%s"%(self.type,message)
		return message

	def debug(self,message):
		if self.enabled:
			WADebug.stdDebug(self.formatMessage(message),self.type)
		
	def d(self,message):#shorthand
		self.debug(message)


class JsonRequestDebug(WADebug):
	pass

class StatusRequestDebug(WADebug):
	pass

class EventHandlerDebug(WADebug):
	pass

class WaxmppDebug(WADebug):
	pass

class SqlDebug(WADebug):
	pass
	
class ConnDebug(WADebug):
	pass

class GeneralDebug(WADebug):
	pass

class ManagerDebug(WADebug):
	pass

class NotifierDebug(WADebug):
	pass

class MessageStoreDebug(WADebug):
	pass
	
class ConnMonDebug(WADebug):
	pass
	
class ContactsDebug(WADebug):
	pass

class UIDebug(WADebug):
	pass

class UpdaterDebug(WADebug):
	pass

class MediaHandlerDebug(WADebug):
	pass
	
class AccountsDebug(WADebug):
	pass
	
class LoginDebug(WADebug):
	pass
	
class WARequestDebug(WADebug):
	pass
	
		
