# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 02:29:46 2021

@author: Chris
"""

#First, we need to import some things
import sys
import PyQt5
from PyQt5 import uic
from PyQt5 import QtWidgets
import time #I'll use this for a print statement later on

# The next three lines allow python to import your gui, named 'DemoGui'
#They basically tell python to get that .ui file and convert it to a form
#that can be manipulated and worked with here in the IDE
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('DemoGui.ui', self) #specify the .ui file to use
  #------------------------------------------------------------------
  
# Everything between the dotted lines will vary with each new GUI.
# You will "connect" buttons to functions here
# We are calling the app "self" and connecting everything to it.
# This is a way make sure all subparts of the GUI communicate
        #1st, when the counter button is clicked, run a function
        #counter is the objectName, while counter_function refers
        #to the function name, as defined below.
        self.add_one.clicked.connect(self.counter_function)
        # last thing after connecting buttons: tell your gui to show itself.... literally
        self.show()
        
    #now define what to do on button push
    #note the indent... still within "class Ui"    
    def counter_function(self):
        # take in whatever text is in the text box called current_count
        #convert that text to an integer (int..a whole number) then add one
        newcount = int(self.current_count.text()) + 1  
        #now set the text in current_count again, as text (aka a 'string' or str)
        self.current_count.setText(str(newcount))
        #print the couunter value and the current time (using the time.time() function)
        print('counter says:   ' + self.current_count.text() + '  at time (s):   ' + str(time.time()))
        
      
       
 #------------------------------------------------------------------------       
#these last lines launch the app.      
#It turns out the very last line, app.exec has some issues in spyder
#for now we can comment it (quick fix, not ideal) or replace it with
#the last three lines 
#Mac users may will probably need to uncomment the last line ( app.exec() )
#Windows users should uncomment the last three lines and use them instead.
if __name__ == "__main__":
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    window = Ui()
#    app.exec()
 
#    import os
#    if not os.environ.get('SPY_UMR_ENABLED'):
#       app.exec()    