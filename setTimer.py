import math
from count1 import*
import time
import threading

curr=0
signals =[]
numberOfSignals=4

min=10
max=60

lanes=3

video_path0 = r"D:\developer\SmartsyncTraffic\SmartSync-Traffic\TRAFFIC TESTCASE 1.mp4"
video_path1 = r"D:\developer\SmartsyncTraffic\SmartSync-Traffic\TRAFFIC TESTCASE 2 .mp4"
video_path2 = r"D:\developer\SmartsyncTraffic\SmartSync-Traffic\TRAFFIC TESTCASE 3.mp4"
video_path3 = r"D:\developer\SmartsyncTraffic\SmartSync-Traffic\TRAFFIC TESTCASE 4.mp4"

timelag=2.5

class trafficSignal:
    def __init__(self,red,yellow,green,min,max) :
        self.red=red
        self.yellow=yellow
        self.green=green
        self.min=min
        self.max=max


def initialize():
    sig1=trafficSignal(0,5,10,10,60)
    signals.append(sig1)
    sig2=trafficSignal(0,5,10,10,60)
    signals.append(sig2)
    sig3=trafficSignal(0,5,10,10,60)
    signals.append(sig3)
    sig4=trafficSignal(0,5,10,10,60)
    signals.append(sig4)
   
def printTime(greenTime):
    while(signals[(curr+1)%numberOfSignals].green!=0):
        print("GREEN TIME: ",signals[(curr+1)%numberOfSignals].green)
        signals[(curr+1)%numberOfSignals].green-=1
        time.sleep(1)
    while(signals[(curr+1)%numberOfSignals].yellow!=0):
        print("YELLOW TIME: ",signals[(curr+1)%numberOfSignals].yellow)
        signals[(curr+1)%numberOfSignals].yellow-=1
        time.sleep(1)

def iterate():
    setTimer(video_path0)
    setTimer(video_path1)
    setTimer(video_path2)
    setTimer(video_path3)
    iterate()


def setTimer(video_path):
    global timelag,lanes,curr
    density,total=count_objects_in_video_frame(video_path)
    greenSignalTime=math.ceil(timelag*((density*60+total)/(lanes+2)))
    if(greenSignalTime<min):
        greenSignalTime=min
    elif(greenSignalTime>max):
        greenSignalTime=max
 
    signals[(curr+1)%numberOfSignals].green=greenSignalTime
    printTime(signals[(curr+1)%numberOfSignals].green)
    curr=curr+1

initialize()
iterate()
