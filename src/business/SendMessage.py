from src.business.Business import Business
from src.business.LoadFile import LoadFile

class SendMessage(Business):

    def send(self, message):
        #cfg = LoadFile(os.path.dirname(os.path.abspath(__file__))).cfg()
        print(message)