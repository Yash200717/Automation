from multiprocessing import Condition
from os import access
import cv2
import time
import random
import dropbox
from numpy import source

startTime=time.time()

def Capture():
    number = random.randint(0,100)
    capture = cv2.VideoCapture(0)
    condition = True
    while (condition):
        ret,frame = capture.read()
        imageName = "image"+str(number)+".jpg"
        cv2.imwrite(imageName,frame)
        condition = False
    return imageName

def uploadFile(imageName):
    accessToken = "bwt-nsDdFP4AAAAAAAAAAWe183hGWi5S4CVkURyno_Dz9b9cghquv8qrsjzzQLsv"
    source = imageName
    destination = "/securitySystem/"+imageName
    dbx = dropbox.Dropbox(accessToken)
    with open (source,"rb") as file:
        dbx.files_upload(file.read(),destination,mode = dropbox.files.WriteMode.overwrite)
        print("File is uploaded Successfully")

def main():
    while True:
        currentTime = time.time()
        if(currentTime-startTime>=5):
            name = Capture()
            uploadFile(name)

main()

