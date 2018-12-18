import os
import json
from src.business.Business import Business

class LoadFile(Business):

    def __init__(self, dirroot):
        self.__dirroot = dirroot

    def cfg(self):
        data = None
        try:
            filename = self.__dirroot + os.sep + 'config.json'
            if(os.path.exists(filename)):
                data = (json.loads(open(filename, 'r').read()))
        except Exception as ex:
            data = None
        return data