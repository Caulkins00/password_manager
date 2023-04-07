# import sys

# from PyQt6.QtWidgets import (
#     QApplication,
#     QDialog,
#     QDialogButtonBox,
#     QFormLayout,
#     QLineEdit,
#     QVBoxLayout,
#     QLabel
# )

# class Window(QDialog):
#     def __init__(self):
#         super().__init__(parent=None)
#         self.setWindowTitle("QDialog")
#         dialogLayout = QVBoxLayout()
#         formLayout = QFormLayout()
#         formLayout.addRow("Username:", QLineEdit())
#         formLayout.addRow("Password:", QLineEdit())
#         dialogLayout.addLayout(formLayout)
#         button = QDialogButtonBox()
#         button.setStandardButtons(
#             QDialogButtonBox.StandardButton.Ok
#         )
#         dialogLayout.addWidget(button)
#         self.setLayout(dialogLayout)
#         button.clicked.connect(_login)
#         msgLabel = QLabel("")
#         dialogLayout.addWidget(msgLabel)


#     def _login(self):
#         if msgLabel.text():
#             msgLabel.setText("")
#         else:
#             msgLabel.setText("Hello, World!")


# if __name__ == "__main__":
#     app = QApplication([])
#     window = Window()
#     window.show()
#     sys.exit(app.exec())


import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from userLogin import *

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login Form')
        self.resize(500, 120)

        layout = QGridLayout()

        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

    def check_password(self):
        msg = QMessageBox()
        if is_valid_credentials(self.lineEdit_username.text(), self.lineEdit_password.text().encode()):
            msg.setText('Success')
            msg.exec()
        else:
            msg.setText('Incorrect Password')
            msg.exec()

if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = LoginForm()
	form.show()

	sys.exit(app.exec())