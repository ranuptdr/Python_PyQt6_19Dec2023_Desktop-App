import sys # sys is a built-in module in python
# from top-level module.submodul import  element1,element2,........
from PyQt6.QtWidgets import QApplication, QHBoxLayout,  QVBoxLayout,  QGridLayout, QPushButton, QWidget
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
button1 = QPushButton("Widget 1")
button2 = QPushButton("Widget 2")
button3 = QPushButton("Widget 3")
button4 = QPushButton("Widget 4")

layout = QGridLayout()
layout.addWidget(button1, 0,0)
layout.addWidget(button2, 0,1)
layout.addWidget(button3, 1,0)
layout.addWidget(button4, 1,1)

window.setLayout(layout)
window.show()

#window.showFullScreen()
# Start the event loop.
app.exec()