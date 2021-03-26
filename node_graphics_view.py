from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QDMGraphicsView(QGraphicsView):

    def __init__(self, grScene, parent = None):
        super().__init__(parent)
        self.grScene = grScene
        self.initUI()
        self.setScene(self.grScene)

    def initUI(self):
        #smooths out objects
        self.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform)

        #fixes issue when moving items around background is cached and not changed
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)