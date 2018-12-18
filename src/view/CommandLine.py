import os
from src.core.variable.shell.Argument import Argument
from src.controller.PostApiByMessage import PostApiByMessage

class CommandLine():

    def __init__(self):
        self.__actions = (['--message'])

    def display(self, argv):
        params = Argument.filter(self.__actions, argv)
        PostApiByMessage().post(params[self.__actions[0]])