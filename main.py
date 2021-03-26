import sys
from PyQt5.QtWidgets import *

from node_editor_wnd import NodeEditorWnd


if __name__ == '__main__':

    #configs the application window, set up
    app = QApplication(sys.argv)

    wnd = NodeEditorWnd()

    #when user closes window the app will exit
    sys.exit(app.exec())

