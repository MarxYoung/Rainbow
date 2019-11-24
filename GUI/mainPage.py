import sys
from PyQt5.QtWidgets import QWidget, QApplication
from main import Ui_Form


class MyDesiger(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyDesiger, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MyDesiger()
    ui.show()
    sys.exit(app.exec_())
