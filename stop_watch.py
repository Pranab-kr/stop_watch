# Python PyQt5 Stop watch
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton)
from PyQt5.QtCore import QTimer, QTime, Qt

class stop_watch(QWidget): # QWidget added here so dont need to create another QWidget veriable within initUI
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stop Watch")
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout (hbox)
        self.setStyleSheet("""
                           QLabel,QPushButton{
                               padding: 20px;
                               font-family: Calibri;
                           }
                        QPushButton{
                            font-size: 40px;  
                        }
                        QLabel{
                            font-size: 100px;
                            background-color: hsl(181, 100%, 78%);
                            border-radius : 20px;
                        }
                        """)
        
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_time)
      
    def start(self):
        self.timer.start(10)
    
    def stop(self):
        self.timer.stop()
    
    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.formet_time(self.time))
    
    def formet_time(self, time):
        hour = self.time.hour()
        minutes = self.time.minute()
        sec = self.time.second()
        mili_sec = self.time.msec() // 10
        return f"{hour:02}:{minutes:02}:{sec:02}.{mili_sec:02}"
    
    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.formet_time(self.time))
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    watch = stop_watch()
    watch. show()
    sys.exit(app.exec_())