from PyQt5.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QTreeView, QVBoxLayout, QWidget
import sys

class FileExplorer(QMainWindow):
    """A simple file explorer application."""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Explorer")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.model = QFileSystemModel()
        self.model.setRootPath('')

        self.tree_view = QTreeView(self)
        self.tree_view.setModel(self.model)
        self.tree_view.setRootIndex(self.model.index(''))
        self.layout.addWidget(self.tree_view)

def create_file_explorer():
    app = QApplication(sys.argv)
    explorer = FileExplorer()
    explorer.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    create_file_explorer()
