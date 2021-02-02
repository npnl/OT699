# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 04:10:42 2021

@author: Chris
"""
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

# The next three lines allow python to import your gui, named 'DemoGui'
#They basically tell python to get that .ui file and convert it to a form
#that can be manipulated and worked with here in the IDE
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('YOUR_UI_NAME.ui', self) #specify the .ui file to use here
  #------------------------------------------------------------------
  
# Everything between the dotted lines will vary with each new GUI.
# You will "connect" buttons to functions here


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