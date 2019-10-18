import os
import subprocess
import sys

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

#cmd = "ps x|grep python3|grep get_image.py|wc -l"
cmd = "ps x|grep python3|grep \"python3 get_image.py\"|grep -v grep|wc -l"
count = int(run_and_capture(cmd))
print(count)

if count >= 1:
    print("the process is alive")
    
    os.system("rm -f /home/pi/ninja/NNPACK-darknet/darknet-nnpack/*.jpg") 
else:
    os.chdir("ninja/NNPACK-darknet/darknet-nnpack")
    os.system("nohup python3 get_image.py &")
    #subprocess.check_call(['python3','get_image.py'])

