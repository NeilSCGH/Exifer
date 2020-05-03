import sys
import os
from lib.tools import *

class program():
    def __init__(self,args):
        self.tool = tools(args)
        self.setup(args)#process the arguments

    def setup(self,args):
        #the folder for source files
        if self.tool.argHasValue("-sf"):
          val = self.tool.argValue("-sf")
          self.sourceFolderPath = val.replace("\\","/")
        else:
          self.stop("Error, -sf (source folder) is missing !")

    def run(self):
        for root, dirs, files in os.walk(self.sourceFolderPath):
            for filename in files:
                print("File", root + "/" + filename)
        
    def stop(self, msg = ""):
        if msg != "": print(msg)
        exit(0)#stop the program

if __name__ == '__main__':
    prog = program(sys.argv)
    prog.run()