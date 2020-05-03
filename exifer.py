import sys
import os
from lib.tools import *

class program():
    def __init__(self,args):
        self.tool = tools(args)
        self.setup(args)#process the arguments

    def setup(self,args):
        if self.tool.argHasValue("-a"):
          val = self.tool.argValue("-a")
          self.a = val

    def run(self):
        print("Hey")
        
    def stop(self, msg = ""):
        if msg != "": print(msg)
        exit(0)#stop the program

if __name__ == '__main__':
    prog = program(sys.argv)
    prog.run()