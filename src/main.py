import cv2
import sys
from time import time
start = time()
class MyBar(Bar):
    fill = "+"
    empty_fill = '-'
    suffix="processed %(percent)d%% of the files"
import os
from tkinter import messagebox
from frame import length
import zlib
import pickle

fRate = 0
i = fRate
frames = []
args = sys.argv
count = 0
cc = count
for x in args:
    count = cc+1
    cc = count
if count > 1:
    if os.path.exists(str(args[1])):
        cap = cv2.VideoCapture(str(args[1]))
else:
    input("FOLLOW THE INSTRUCTIONS IN THE README!! \n press any key to exit...")
    raise SystemExit
#WFM stands for Writen Frame Numbers
#so i can delete them if it fails and it wont take up any space
WFM = []
while(fRate <= length):
    ret, frame = cap.read()
    fRate = i+1;
    i = fRate
    if(fRate % 2) == 0:
        frames.append(zlib.compress(frame, 9))
    if(fRate % 500) == 0:
        try:
            pickle.dump(frames, open(str(fRate)+".data", "wb+"))
            WFM.append(str(fRate)+".data")
            frames.clear()
        except:
            for x in WFM:
                os.remove(x)
        
fRate = 0
i = 0
finished = time()-start