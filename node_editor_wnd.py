
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from node_graphics_scene import QDMGraphicsScene
from node_graphics_view import QDMGraphicsView

class NodeEditorWnd(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):

        #x-offset, y-offset, height, width
        self.setGeometry(200, 200, 800, 600)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)

        #greate graphics scene
        self.grScene = QDMGraphicsScene()

        # create graphics view
        self.view = QDMGraphicsView(self.grScene, self)
        self.view.setScene(self.grScene)
        self.layout.addWidget(self.view)

        self.setWindowTitle("Node Editor")
        self.show()

        self.addDebugContent()

    def addDebugContent(self):

        greenBrush = QBrush(Qt.green)
        outlinePen = QPen(Qt.black)
        outlinePen.setWidth(2)

        rect = self.grScene.addRect(-100, -100, 80, 100, outlinePen, greenBrush)
        rect.setFlag(QGraphicsItem.ItemIsMovable)

        text = self.grScene.addText("Tacofriday!!") #can add QFont(font) to change font
        text.setFlag(QGraphicsItem.ItemIsSelectable) #makes the item selectable
        text.setFlag(QGraphicsItem.ItemIsMovable) #makes the items moveable
        text.setDefaultTextColor(QColor.fromRgbF(1.0, 1.0, 1.0)) #colors the text white

        widget1 = QPushButton("Hello, its tacofriday")
        proxy1 = self.grScene.addWidget(widget1)
        proxy1.setPos(0, 30)

        line = self.grScene.addLine(-200, -200, 400, -100, outlinePen)
        line.setFlag(QGraphicsItem.ItemIsMovable)
        line.setFlag(QGraphicsItem.ItemIsSelectable)
