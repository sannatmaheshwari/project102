import cv2
import dropbox
import time
import random

startTime = time.time()

def capture():
    number = random.randint(0,100)
    videoCaptureobject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureobject.read()
        imagename = "image"+str(number)+".png"
        cv2.imwrite(imagename,frame)
        startTime = time.time
        result = False
    return imagename
    videoCaptureobject.release()
    cv2.destroyAllWindows()

def uploadfile(imagename):
     token = "sl.BBA5UnNu4_IA_oBf1jIDvbG7Z4kJhBLeZ0hFFnXsiGxnXQheG2Tiwjy61WbS1QfV468rqk01uBfZX_VDvaGVlh6QEY0d5lOKqNzuvRY1-eMV_lFRkBnrwOVBZyGU0quUV_d4FvvRzxu3"
     file = imagename
     filefrom = file
     fileto = "/dropbox/"+imagename
     dbx = dropbox.Dropbox(token)
     
     with open(filefrom,"rb") as x:
         dbx.files_upload(x.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
         print("file uploaded")

def main():
    while(True):
        if((time.time()-startTime)>=10):
            name = capture()
            uploadfile(name)
main()

