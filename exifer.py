import sys
import os
from lib.tools import *
from pymediainfo import MediaInfo
import json

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

        self.keepName = self.tool.argExist("-kn")
        
        self.extensionAllowed=[".jpg",".cr2",".mp4",".mts"]

    def run(self):
        for root, dirs, files in os.walk(self.sourceFolderPath):
            for filename in files:
                self.rename(root,filename)
        

    def rename(self, root, file):
        oldPath=root+"/"+file
        extension="." + file.split(".")[-1]
        if extension.lower() in self.extensionAllowed:
            
            newName=self.getNewName(root,file) + extension
            newPath=root+"/"+newName

            print("Renaming {} -> {}".format(oldPath,newName))
            try:
                os.rename(oldPath, newPath)
            except:
                print("Error with", file)

        else:
            print("Unallowed :", file)

    def getNewName(self, root, file):
        data=self.getDate(root+"/"+file)
        year=data[:4]
        month=data[5:7]
        day=data[8:10]
        hour=data[11:13]
        minute=data[14:16]
        second=data[17:19]

        newName=year+month+day+"_"+hour+minute+second

        if self.keepName : 
            if "." in file:
                newName += "_" + file[:file.rfind(".")] #suppress the extension
            else:
                newName += "_" + file

        return newName

    def getDate(self,file):
        media_info = MediaInfo.parse(file, output="JSON")
        return(json.loads(media_info)["media"]["track"][0]["File_Modified_Date_Local"])

    def stop(self, msg = ""):
        if msg != "": print(msg)
        exit(0)#stop the program

if __name__ == '__main__':
    prog = program(sys.argv)
    prog.run()