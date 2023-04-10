import sys
import demo

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__=="__main__":
    app = QApplication(sys.argv)  #创建应用程序对象
    mainWindow = QMainWindow()    #创建主窗口
    ui = demo.Ui_MainWindow()
    ui.setupUi(mainWindow) #向哪个主窗口添加控件
    mainWindow.show()      #显示窗口
    sys.exit(app.exec())   #进入主循环
