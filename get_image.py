import os
import requests,json
from datetime import datetime
import csv
import sys
import subprocess
import slack
import time

def run_and_capture(cmd):
    proc=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    buf=[]
    
    while True:
        line=proc.stdout.readline()
        line=line.decode("UTF-8")

        buf.append(line)
        sys.stdout.write(line)

        if proc.poll() is not None:
            break
    return "".join(buf)


while True:   
    start_time = time.perf_counter()
    os.system('raspistill -t 10 -o  predictions.jpg')
    msg = run_and_capture("./darknet detect cfg/yolov2-tiny.cfg yolov2-tiny.weights ./predictions.jpg")


    person_count =msg.count("person")
    print(person_count)
    
    now = str(datetime.now())
    path = "/home/pi/ninja/NNPACK-darknet/darknet-nnpack/predictions.jpg"
    path_aft = "/home/pi/ninja/NNPACK-darknet/darknet-nnpack/predictions"+now+".jpg"
    os.rename(path,path_aft)

    TOKEN = '------my token--------'
    ImagePath = path_aft
    CHANNEL = '------slcak channel name-----'
    TITLE = 'test file'
    files = {'file': open(ImagePath, 'rb')}
    param = {
    'token':TOKEN,
    'channels':CHANNEL,
    'filename':"new picture",
    'title': TITLE
    }
    if person_count >= 1:
        requests.post(url="https://slack.com/api/files.upload",params=param, files=files)

    execution_time = time.perf_counter()-start_time
    print("execution time is ",execution_time," seconds")

    #os.remove("/home/pi/ninja/NNPACK-darknet/darknet-nnpack/*.jpg")

    if execution_time <= 40:
        time.sleep(40 - execution_time)
