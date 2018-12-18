import requests
from src.business.Business import Business
from src.business.LoadFile import LoadFile
from src.controller.Controller import Controller

class PostApiByMessage(Controller):

    def post(self, message):
        #cfg = LoadFile(os.path.dirname(os.path.abspath(__file__))).cfg()
        print(message)