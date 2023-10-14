import cv2 as cv
import datetime
import os
import time

def camera_shoot():
    camera=cv.VideoCapture(0)
    r,frame = camera.read()
    folder='images/'
    if not os.path.exists(folder):
        os.makedirs(folder)
    if r:
        filename = f"Login_on_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.jpg"
        path=os.path.join(folder,filename)
        cv.imwrite(path,frame)
        #printf("Image Saved");

        #Video record
        format=cv.VideoWriter_fourcc(*'mp4v')
        out=cv.VideoWriter(f"{folder}Login_on_{filename}.mp4",format,30.0,(640,480))
        start_time=time.time()
        while True:
            r,frame = camera.read()
            out.write(frame)
            remain_time = time.time()-start_time
            if remain_time >= 10:
                out.release()
                break
    camera.release()
    cv.destroyAllWindows()

camera_shoot()
