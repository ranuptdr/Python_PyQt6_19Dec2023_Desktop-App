# import modulName
import sys # sys is a built-in module in python
import  requests # requests is a 3rd party module
# from top-level module.submodul import  element1,element2,........
from PyQt6.QtWidgets import QMessageBox, QApplication, QWidget, QHBoxLayout,  QVBoxLayout,  QGridLayout, QPushButton, QLabel, QLineEdit
from PyQt6.QtGui import QIcon # PyQt6 is a 3rd party module

# classobject = ClassName(actualArgument will go inside constructor)
# Creating an instance/object of QApplication
app = QApplication(sys.argv) # app is a external clas object

window = QWidget() # window  is a external clas object
#window.showMaximized() # Show the Window in a maximized state
# Setting the window title
window.setWindowTitle('idmregistration')

iconCo = QIcon('./icon.png')
window.setWindowIcon(iconCo)

# co = ClassName()
# co.method()
button1 = QPushButton("save")
button2 = QPushButton("Delete")

fname = QLabel("First Name")
lname = QLabel("Last Name")
email = QLabel("Email")
snumber = QLabel("Serial number")

fname_input = QLineEdit()
lname_input = QLineEdit()
email_input = QLineEdit()
snumber_input = QLineEdit()

layout = QGridLayout()

#layout.addWidget(fname,y,x)
layout.addWidget(fname,0,0)
layout.addWidget(fname_input,0,1)
layout.addWidget(lname,1,0)
layout.addWidget(lname_input,1,1)
layout.addWidget(email,2,0)
layout.addWidget(email_input,2,1)
layout.addWidget(snumber,3,0) 
layout.addWidget(snumber_input,3,1) 

layout.addWidget(button1, 4,0)
layout.addWidget(button2, 4,1)

window.setLayout(layout)

def sendData():
    print("Inside sendData function")
    payload = {
        "data": {
            "firstname": fname_input.text(),
            "lastname": lname_input.text(),
            "email": email_input.text(),
            "sno": snumber_input.text()
        }
    }

    api_url = 'http://localhost:1337/api/registrations'
    #module.member
    #return = module.member(actualArgument,  keyword Argument)
    response = requests.post(api_url, json=payload)
    
    pass

#widget.signal.connect(slot_function)
button1.clicked.connect(sendData)

window.show()
#window.showFullScreen()
# Start the event loop.
app.exec()
