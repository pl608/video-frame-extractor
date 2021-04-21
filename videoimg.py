import cv2
from progress.bar import Bar
from time import time
start = time()
from progress.bar import Bar as Bar
class MyBar(Bar):
    fill = "+"
    empty_fill = '-'
    suffix="processed %(percent)d%% of the files"
import os
from tkinter import messagebox
from frame import length
import zlib
import pickle
cap = cv2.VideoCapture(input("path: "))
fRate = 0
i = fRate
frames = []

#WFM stands for Writen Frame Numbers
#so i can delete them if it failes

WFM = []
bar = MyBar(max=500/2)
while(fRate <= length):
    ret, frame = cap.read()
    fRate = i+1;
    i = fRate
    if(fRate % 2) == 0:
        frames.append(zlib.compress(frame, 9))
        bar.next()
    if(fRate % 500) == 0:
        try:
            pickle.dump(frames, open(str(fRate)+".data", "wb+"))
            WFM.append(str(fRate)+".data")
            frames.clear()
            bar.finish()
            bar.goto(0)
        except OSError:
            messagebox.showerror("Failed", "Operation failed due to lack of space on this device \n please delete some files to make room \n now deleting extra files")
            delbar = MyBar(maax=WFM.count, )
            for x in WFM:
                os.remove(x)
                delbar.next()
            delbar.finish()
        
fRate = 0
i = 0
finished = time()-start
messagebox.showinfo("Finished", "Completed frame extration \n in "+str(finished)+" seconds")