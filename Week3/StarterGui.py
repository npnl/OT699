# -*- coding: utf-8 -*-
"""
Starter Gui
Assumes you made a .ui file already
To make life easier, please be sure that the .ui file, this .py file, 
and any image files etc. attached to your design Gui are all together 
in one folder.  Run this program from that folder
Default on windows is ..\spyder-py3 
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
     
#Mac users need to uncomment the app.exec()  after window =Ui() and then coment the rest
#make sure that app.exec() is all the way to the left (no indentation).
#Windows users should uncomment the last three lines but comment the app.exec() afer window=Ui()

app = PyQt5.QtWidgets.QApplication(sys.argv)
window = Ui()
#app.exec()
import os
if not os.environ.get('SPY_UMR_ENABLED'):
    app.exec()    