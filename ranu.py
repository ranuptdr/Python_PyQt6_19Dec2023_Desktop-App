#import module
import sys # sys is a built-in module in python
import requests
# from top-level module.submodul import  element1,element2,........
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt6.QtGui import QIcon, QDesktopServices
from PyQt6.QtCore import QUrl

# classobject = ClassName()
# Creating an instance/object of QApplication
app = QApplication(sys.argv) # app is a external clas object

window = QWidget() # window  is a external clas object
#window.showMaximized() # Show the Window in a maximized state
# Setting the window title
window.setWindowTitle('QGridLayout')

iconCo = QIcon('./icon.png')
window.setWindowIcon(iconCo)

# co = ClassName()
# co.method()
button1 = QPushButton("save")
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
layout.addWidget(button1, 4, 0)
layout.addWidget(button2, 4, 1)
layout.addWidget(button3, 4, 2)

window.setLayout(layout)

def on_ok_clicked():
    fname_value = fname_input.text().strip()
    lname_value = lname_input.text().strip()
    email_value = email_input.text().strip()
    snumber_value = snumber_input.text().strip()

    # Check if any of the required fields are empty
    if not fname_value or not lname_value or not email_value or not snumber_value:
        ranu("Error", "Please fill in all the fields.")
        return

    api_url = "http://localhost:1337/api/registrations"

    headers = {
        "Content-Type": "application/json",
        # Add any additional headers or authentication details here
    }

    # Modify the payload structure
    payload = {
        "data": {
            "FNAME": fname_value,
            "LNAME": lname_value,
            "EMAIL": email_value,
            "SNO": snumber_value
        }
    }

    # Print the payload and headers for debugging
    print("Request payload:", payload)
    print("Request headers:", headers)

    try:
        response = requests.post(api_url, json=payload, headers=headers)

        # Print the response content
        print("Response content:", response.text)

        parsed_response = response.json()  # Parse the JSON content
        print("Parsed response:", parsed_response)

        if response.status_code == 200:
            ranu("Success", "Registration successful.")
            reset_inputs()
        elif response.status_code == 405:
            ranu("Error", "Entry with the same values already exists.")
        else:
            print(f"Registration failed. Status code: {response.status_code}")
            ranu("Error", f"Registration failed. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

def ranu(title, text):
    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setText(text)
    msg_box.setIcon(QMessageBox.Icon.Information)
    msg_box.exec()

def reset_inputs():
    fname_input.clear()
    lname_input.clear()
    email_input.clear()
    snumber_input.clear()

def open_google_link():
    google_url = "https://www.google.com"
    QDesktopServices.openUrl(QUrl(google_url))

def on_cancel_clicked():
    window.close()

button1.clicked.connect(on_ok_clicked)
button2.clicked.connect(open_google_link)
button3.clicked.connect(on_cancel_clicked)


window.show()

#window.showFullScreen()
# Start the event loop.
app.exec()
