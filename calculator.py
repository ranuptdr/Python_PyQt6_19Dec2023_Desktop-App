import sys # sys is a built-in module in python
# from top-level module.submodul import  element1,element2,........
from PyQt6.QtWidgets import QApplication,  QMainWindow
from PyQt6.QtGui import QIcon

# classobject = ClassName()
# Creating an instance/object of QApplication
app = QApplication(sys.argv) # app is a external clas object

window = QMainWindow() # window  is a external clas object
window.showMaximized() # Show the Window in a maximized state

# Setting the window title
window.setWindowTitle("OKLABS Calculator")


#  Set Window Icon
#iconCo = QIcon('icon.png')
#iconCo = QIcon('./icon.png')
iconCo = QIcon('./oklabs.jpg')
window.setWindowIcon(iconCo)

# Create a Calculator Menu bar
menubar = window.menuBar()
Calculator_menu = menubar.addMenu('calculator')
# Create a Calculator subMenu 
Standard_menu = Calculator_menu.addMenu("Standard")
Standard_menu2 = Standard_menu.addMenu('standard_2')
Standard_menu3 = Standard_menu2.addMenu('''standard_3''')
Scientific_menu = Calculator_menu.addMenu('Scientific')
Graphing_menu = Calculator_menu.addMenu('Graphing')
Programmer_menu = Calculator_menu.addMenu('Programmer')
DateCalculation_menu = Calculator_menu.addMenu('Date calculation')

# Create a Converter Menu bar
converter_menu = menubar.addMenu('Converter')
# Create a Converter subMenu
Currency_menu = converter_menu.addMenu('Currency') 
Volume_menu = converter_menu.addMenu('Volume') 
Length_menu = converter_menu.addMenu('Length') 

# Create a Setting Menu bar
Settings_menu = menubar.addMenu('Settings')

#window.show() # classobject.method()
#window.showFullScreen() 

app.exec()