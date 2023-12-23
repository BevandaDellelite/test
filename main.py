from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import Qt 
from random import randint
app = QApplication([])

window = QWidget()
window.resize(300,300)
window.move(250,250)

buttom = QPushButton('Taras')
text1 = QLabel('Pisun')
text2 = QLabel('?')

v = QVBoxLayout()
v.addWidget(text1, alignment=Qt.AlignCenter)
v.addWidget(text2,  alignment=Qt.AlignCenter)
v.addWidget(buttom,  alignment=Qt.AlignCenter)

def random_number():
    n = randint(1,101)
    text2.setText(str(n))

random_number()
buttom.clicked.connect(random_number)


buttom.setStyleSheet("""
    background-color: #4CAF50;
    border-radius: 10px;
    font-size: 16px;
    border: none;
    padding: 10px 20px;
""")
window.setLayout(v)
window.show()

app.exec_()
