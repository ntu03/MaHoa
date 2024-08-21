import sys
sys.path.append("D:/DETAI_BMHTTT/Control")
from PyQt6.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox,QWidget, QGraphicsDropShadowEffect, QSizeGrip, QFrame #[1]????????????
from ThietKe.ThietKeGiaiMaAES import Ui_Dialog  
from mahoaAES_class import CAES #???????????
#========================================================================================
class MyDialogGMAES(QDialog, Ui_Dialog):#[2]???????????????????????
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Thêm xử lý sự kiện và tuỳ chỉnh giao diện người dùng tại đây
        self.s = '' #khai báo toàn cục của lớp THIS => datamember
        self.k = ''
        self.btnGiaiMa.clicked.connect(self.GiaiMa)
        self.btnOpenFile.clicked.connect(self.MoFile)
        self.btnSaveFile.clicked.connect(self.GhiFile)
        self.btnClose.clicked.connect(self.Close)
    def Close(self):
        choice = QMessageBox.question(self, "Xác nhận thoát", "Bạn có chắc muốn thoát ứng dụng?",
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if choice == QMessageBox.StandardButton.Yes:
            self.close()
        else:
            pass #nothing
    def GiaiMa(self):
        textci = self.txtCiphertext.toPlainText() #lấy dữ liệu trong text ciphertext của ThietKeMaHoaVignere
        if not textci:
            QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.btnOpenFile.setFocus()
        else:
            cAES = CAES()
            s = cAES.GiaiMa(self.s,self.k)
            self.txtVanBanGoc.setPlainText(s) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile(self):
        #Mở file dữ liệu đã mã hoá
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'rb') as file:
                self.s = file.read()
                self.txtCiphertext.setPlainText(self.s.decode('utf-8'))
        #Mở file dữ liệu đã KEY
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'rb') as file:
                self.k = file.read()
                #self.txtKey.setPlainText(self.k.decode('utf-8'))

    def GhiFile(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtVanBanGoc.toPlainText())
 ###################################################################################################################
     #Tìm QFrame trong cấu trúc UI
        self.head = self.findChild(QFrame, "head")
        if self.head is not None:  
            self.draggable = False
            self.dragPos = None
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton and self.head is not None and self.head.geometry().contains(event.pos()):
            self.draggable = True
            self.dragPos = event.globalPosition().toPoint() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.draggable:
            new_pos = event.globalPosition().toPoint() - self.dragPos
            self.move(new_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.draggable = False
            event.accept()
                 
    def slideLeftMenu(self):
     if self.isFrameHidden:
                # Hiển thị frame
                self.slide_menu_container.setVisible(True)
                self.isFrameHidden = False
               
     else:
                # Ẩn frame
                self.slide_menu_container.setVisible(False)
                self.isFrameHidden = True
####################################################################               
#========================================================================================
def main():
    app = QApplication(sys.argv)
    mainMyDialog = MyDialogGMAES()
    mainMyDialog.show()
    sys.exit(app.exec())
#========================================================================================
if __name__ == "__main__":
    main()
