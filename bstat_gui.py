import datetime

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import bstat

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

icon = QIcon("battery_full.png")

tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

menu = QMenu()
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

tray.setContextMenu(menu)


def update_time():
    stat_data = bstat.battery_data()
    if stat_data.get('power_plugged', True):
        bat_value = 'On charge'
        current_icon = QIcon('battery_charge.png')
    else:
        bat_value = f'Left time: {stat_data.get("left_time")}'
        percentage = stat_data.get('percent')
        if percentage < 10:
            current_icon = QIcon('battery_empty.png')
        elif percentage < 40:
            current_icon = QIcon('battery_03.png')
        elif percentage < 80:
            current_icon = QIcon('battery_07.png')
        else:
            current_icon = QIcon('battery_full.png')
    tray_info = f'{stat_data.get("percent", "-1")}%, {bat_value}'
    print(f'update on {datetime.datetime.now()}')
    tray.setToolTip(tray_info)
    tray.setIcon(current_icon)


update_time()
timer = QtCore.QTimer()
timer.setInterval(10000)
timer.timeout.connect(update_time)
timer.start()

app.exec_()
