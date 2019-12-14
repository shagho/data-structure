import sys
import networkx as nx
from gui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QImage, QBrush, QPalette, QPixmap
from PyQt5.QtCore import QSize
import pandas as pd
from nash_contact import nash_contact
from datetime import datetime
from nash_person import nash_person

# s = nash_person("navid", "shaghozahi", "3660826200", datetime(1378, 10, 26), "zabol", "isfahan", "salam")
# d = nash_person("mohammadreza", "kooh", "083456789", datetime(2000, 12, 20), "tabas", "isfahan", "salam")
#
# g = nx.Graph()
# g.add_node(s.key, data=s)
# g.add_node(d.key, data=d)
# print(g.nodes['3660826200']['data'].key)
# nx.draw_networkx(g)

# df = pd.read_csv("cars.csv")
# g = nx.Graph()
# nx.from_pandas_dataframe()
# libraries
"""it is a joke"""
# import pandas as pd
# import numpy as np
# import networkx as nx
# import matplotlib.pyplot as plt
#
# # Build a dataframe with 4 connections
# df = pd.read_csv("cars.csv")
#
#
# # Build your graph
# G = nx.from_pandas_edgelist(df, 'model', 'color')
#
# # Plot it
# nx.draw(G, with_labels=True)
# plt.show()
"""it is a joke"""


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setupUi(self)
        oImage = QImage("journal-big-data.png")
        sImage = oImage.scaled(QSize(1058, 732))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        self.node_csv_files = None
        self.edge_csv_files = None
        self.actionopen.triggered.connect(self.open_files)

    def open_files(self):
        filter = "CSV (*.csv)"
        file_name = QFileDialog()
        file_name.setFileMode(QFileDialog.ExistingFiles)
        self.node_csv_files = file_name.getOpenFileNames(self, "Please open node files", "C\\Desktop", filter)
        self.node_csv_files[0].sort()
        print(self.node_csv_files)
        self.edge_csv_files = file_name.getOpenFileNames(self, "Please open edge files", "C\\Desktop", filter)
        self.edge_csv_files[0].sort()
        print(self.edge_csv_files)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
