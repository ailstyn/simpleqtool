import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, 
                             QFileDialog, QAction, QLabel, QScrollArea, QHBoxLayout, 
                             QPushButton, QStatusBar, QToolBar)
from PyQt5.QtGui import QPixmap, QIcon, QTransform
from PyQt5.QtCore import Qt, QTimer
from map_parser import MapParser
from map_renderer import MapCanvas

class MapViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EverQuest Map Viewer")
        self.setGeometry(100, 100, 1200, 800)
        
        self.zoom_level = 1.0
        self.pan_x = 0
        self.pan_y = 0
        self.current_map = None
        
        # Create UI
        self.init_ui()
        
    def init_ui(self):
        """Initialize the user interface"""
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Map canvas
        self.canvas = MapCanvas()
        layout.addWidget(self.canvas)
        
        # Navigation controls
        nav_layout = QHBoxLayout()
        
        zoom_in_btn = QPushButton("🔍+")
        zoom_out_btn = QPushButton("🔍-")
        fit_btn = QPushButton("Fit View")
        reset_btn = QPushButton("Reset")
        
        zoom_in_btn.clicked.connect(self.zoom_in)
        zoom_out_btn.clicked.connect(self.zoom_out)
        fit_btn.clicked.connect(self.fit_view)
        reset_btn.clicked.connect(self.reset_view)
        
        nav_layout.addWidget(zoom_in_btn)
        nav_layout.addWidget(zoom_out_btn)
        nav_layout.addWidget(fit_btn)
        nav_layout.addWidget(reset_btn)
        nav_layout.addStretch()
        
        layout.addLayout(nav_layout)
        
        # Create menu bar
        self.create_menu()
        
        # Create toolbar
        self.create_toolbar()
        
        # Create status bar
        self.statusBar().showMessage("Ready")
        
    def create_menu(self):
        """Create menu bar"""
        menu_bar = self.menuBar()
        
        # File menu
        file_menu = menu_bar.addMenu("&File")
        
        open_action = QAction("&Open Map", self)
        open_action.triggered.connect(self.open_map)
        file_menu.addAction(open_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("E&xit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # View menu
        view_menu = menu_bar.addMenu("&View")
        
        fit_action = QAction("&Fit to Map", self)
        fit_action.triggered.connect(self.fit_view)
        view_menu.addAction(fit_action)
        
        reset_action = QAction("&Reset View", self)
        reset_action.triggered.connect(self.reset_view)
        view_menu.addAction(reset_action)
        
        # Help menu
        help_menu = menu_bar.addMenu("&Help")
        
        about_action = QAction("&About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        
    def create_toolbar(self):
        """Create toolbar"""
        toolbar = self.addToolBar("Navigation")
        
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_map)
        toolbar.addAction(open_action)
        
        toolbar.addSeparator()
        
        zoom_in_action = QAction("Zoom In", self)
        zoom_in_action.triggered.connect(self.zoom_in)
        toolbar.addAction(zoom_in_action)
        
        zoom_out_action = QAction("Zoom Out", self)
        zoom_out_action.triggered.connect(self.zoom_out)
        toolbar.addAction(zoom_out_action)
        
    def open_map(self):
        """Open a map file"""
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self, 
            "Open Map File", 
            "maps/",
            "Map Files (*.txt);;All Files (*)",
            options=options
        )
        
        if file_name:
            self.load_map(file_name)
            
    def load_map(self, file_path):
        """Load and display a map"""
        try:
            parser = MapParser()
            map_data = parser.parse_map_file(file_path)
            
            self.current_map = map_data
            self.canvas.set_map_data(map_data)
            self.fit_view()
            
            zone_name = os.path.basename(file_path).replace('.txt', '')
            self.statusBar().showMessage(f"Loaded: {zone_name} ({len(map_data['lines'])} lines, {len(map_data['points'])} points)")
            
        except Exception as e:
            self.statusBar().showMessage(f"Error loading map: {str(e)}")
            
    def zoom_in(self):
        """Zoom in"""
        self.zoom_level *= 1.2
        self.update_view()
        
    def zoom_out(self):
        """Zoom out"""
        self.zoom_level /= 1.2
        self.update_view()
        
    def fit_view(self):
        """Fit entire map to view"""
        if self.current_map:
            self.canvas.fit_to_view()
            self.zoom_level = 1.0
            self.pan_x = 0
            self.pan_y = 0
            
    def reset_view(self):
        """Reset view to default"""
        self.zoom_level = 1.0
        self.pan_x = 0
        self.pan_y = 0
        self.update_view()
        
    def update_view(self):
        """Update the canvas view"""
        self.canvas.set_zoom(self.zoom_level)
        self.canvas.set_pan(self.pan_x, self.pan_y)
        self.canvas.update()
        self.statusBar().showMessage(f"Zoom: {self.zoom_level:.1f}x | Pan: ({self.pan_x}, {self.pan_y})")
        
    def show_about(self):
        """Show about dialog"""
        from PyQt5.QtWidgets import QMessageBox
        QMessageBox.information(
            self,
            "About EverQuest Map Viewer",
            "Simple QTool - EverQuest Map Viewer\n\n"
            "A PyQt5-based map viewer for EverQuest zones.\n"
            "Maps from: https://github.com/smasherprog/EqTool"
        )


def main():
    app = QApplication(sys.argv)
    viewer = MapViewer()
    viewer.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()