# -*- coding: utf-8 -*-
"""

"""

# Read through code, Mac users may need to comment/uncomment a few lines
# at the very start of the code, and again at the very end. 

#Before running this for the first time run this in the console window:
#           conda install -c conda-forge python-sounddevice

#note: Mac may pretend that basic.ui is basic.xml.  If it does that, 
#actually rename the file to be .ui instead of .xml
#Also, basic.ui and this program, called ToyGui.py,thecount.jpg, and microphone.jpt 
#must all be in the same folder...the one you run this from
#Final note:  I changed button names so that this .ui can't be confused with our previous demo

#need to import some libraries: mainly PyQt5 with a few others used for random things
import sys
import PyQt5 
from PyQt5 import uic #gui building stuff

#for mac, uncomment the next two lines. Otherwise, don't.
#import matplotlib
#matplotlib.use('macosx')

import matplotlib.pyplot as plt #plot library
import sounddevice as sd #sound library
import numpy as np #math library
import time #lets us get current time


#The next three lines allow python to import your gui, named 'basic.ui'
class Ui(PyQt5.QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('basic.ui', self)
        #now we need to enable button presses to run functions
        #Buttons were called Adder, Record, PlayBack, and Plot_wave
        #The associated functions will be AdderPressed, RecordPressed, PlayBackPressed, and Plot_wavePressed
        self.Adder.clicked.connect(self.AdderPressed) # Remember to pass the definition/method, not the return value!
        self.Record.clicked.connect(self.RecordPressed) # Remember to pass the definition/method, not the return value!
        self.PlayBack.clicked.connect(self.PlayBackPressed) # Remember to pass the definition/method, not the return value!
        self.Plot_wave.clicked.connect(self.Plot_wavePressed)
        #tell your gui to show itself.... literally
        self.show()


    def AdderPressed(self):
        # my text box's objectName was "input" in the designer
        newcount= int(self.input.text())+1 #add one
        self.input.setText(str(newcount)) #put new string in input box
        print('counter says:   ' + self.input.text() + '  at time (s):   ' + str(time.time()))
        
        
    def RecordPressed(self):
        self.Record.setChecked(True)# makes sure box stays checked during recording
        S=float(self.duration.text()) # duration was the name of this text box
        #sound device (sd) can record/play, specifying duration, samplerate, 1 or 2 channels of audio
        #and finally, if the program should not move on (blocking=true) until recording is done or not
        self.myrecording = sd.rec(int(S * 44100), samplerate=44100, channels=1,blocking=True)
        self.Record.setChecked(False) #now box can show as unchecked
        
    def PlayBackPressed(self):
        self.PlayBack.setChecked(True) #make box look checked until playback stops
        sd.playrec(self.myrecording,samplerate=44100, channels=1,blocking=True)
        self.PlayBack.setChecked(False) #make box look unchecked
        
        
    def Plot_wavePressed(self):
        S=float(self.duration.text())
        timepoints=np.arange(start=0,stop=S,step=1/44100)#get time per sample
        plt.plot(timepoints,self.myrecording) 

     
app = PyQt5.QtWidgets.QApplication(sys.argv)
window = Ui()
   #Mac users uncomment next line and comment all following lines
app.exec()
#import os
#if not os.environ.get('SPY_UMR_ENABLED'):
#     app.exec() 
    
    



