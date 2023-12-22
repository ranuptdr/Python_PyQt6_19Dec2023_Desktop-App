import sys # sys is a built-in module in python
# from top-level module.submodul import  element1,element2,........
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout,  QVBoxLayout,  QGridLayout, QPushButton, QLabel, QLineEdit
from PyQt6.QtGui import QIcon

# classobject = ClassName()
# Creating an instance/object of QApplication
app = QApplication(sys.argv) # app is a external clas object

window = QWidget() # window  is a external clas object
window.showMaximized() # Show the Window in a maximized state
# Setting the window title
window.setWindowTitle('QGridLayout')

iconCo = QIcon('./icon.png')
window.setWindowIcon(iconCo)

# co = ClassName()
# co.method()
button1 = QPushButton("OK")
button2 = QPushButton("How To License")
button3 = QPushButton("Cancle")

fname = QLabel('First Name')
lname = QLabel('Last Name')
email = QLabel('Email')
snumber = QLabel('Serial number')

fname_input = QLineEdit()
lname_input = QLineEdit()
email_input = QLineEdit()
snumber_input = QLineEdit()

layout = QGridLayout()
layout.addWidget(fname, 0,0)
layout.addWidget(fname_input, 0,1) 
layout.addWidget(lname, 1,0)
layout.addWidget(lname_input, 1,1)
layout.addWidget(email, 2,0)
layout.addWidget(email_input, 2,1)
layout.addWidget(snumber, 3,0)
layout.addWidget(snumber_input, 3,1)

window.setLayout(layout)
window.show()

#window.showFullScreen()
# Start the event loop.
app.exec()
