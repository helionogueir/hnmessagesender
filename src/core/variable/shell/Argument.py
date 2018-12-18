import re

class Argument(object):

    @staticmethod
    def filter(keys, values):
        data = {}
        if((type(keys) is list) and (type(values) is list)):
            for key in keys:
                if(key in values):
                    data = {key: Argument.__getValid(key, values)}
        return data

    @staticmethod
    def __getValid(key, values):
        value = None
        valuePos = (values.index(key))+1
        valuesLen = len(values)
        if(len(values) >= valuePos):
            value = values[valuePos];
        return value