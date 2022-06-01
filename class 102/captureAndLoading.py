from email.mime import image
import cv2
import dropbox 
import time
import random

start_time=time.time()
def takeSnapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        image_name="img"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        start_time=time.time
        result=False
    return image_name
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFile(image_name):
    access_token= "sl.BGeMSclPBZy35cpf9JLMSlLaUsz4MeS2SeM_mM-8kPO66DcaBeEd0fFqreUVVmK_v2Qwbj7JIO2kYZfFrJkuwgHN9RZwBfXcfvO_QoeWyZfXuerXwIcfvT-KsBEOt9z8g83CoFa_ytaD"
    file=image_name
    file_from=file
    file_to='/newfolder1/'+(image_name)
    dbx=dropbox.Dropbox(access_token)

    with open (file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=300): 
            name=takeSnapshot()
            uploadFile(name)

main()
    