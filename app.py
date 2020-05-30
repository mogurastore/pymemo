import sys
from PySide2.QtWidgets import QApplication, QFileDialog
from PySide2.QtUiTools import QUiLoader

app = QApplication(sys.argv)

window = QUiLoader().load("memo.ui")

def save():
    filename = QFileDialog.getSaveFileName()[0]
    file = open(filename, mode="w")
    text = window.textEdit.toPlainText()
    file.write(text)
    file.close()

window.actionSave.triggered.connect(save)

window.show()

sys.exit(app.exec_())
