import sys
sys.path.append("D:/DETAI_BMHTTT/Control")
from PyQt6.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox,  QWidget, QGraphicsDropShadowEffect, QSizeGrip, QFrame #[1]????????????
from ThietKe.ThietKeMaHoaCeasar import Ui_Dialog
from mahoaceasar_class import CCeasar #???????????
from GiaoDienMaHoaVignere import MyDialogMHVignere
from GiaoDienMaHoaTrithemius import MyDialogMHTrithemius
from GiaoDienMaHoaBelasco import MyDialogMHBelasco
#========================================================================================
class MyDialogMHCeasar(QDialog, Ui_Dialog):#[2]???????????????????????
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Thêm xử lý sự kiện và tuỳ chỉnh giao diện người dùng tại đây
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.btnMaHoa.clicked.connect(self.MaHoa)
        self.btnOpenFile.clicked.connect(self.MoFile)
        self.btnSaveFile.clicked.connect(self.GhiFile)
        self.btnClose.clicked.connect(self.Close)
        self.actionCeasar_MaHoa.clicked.connect(self.on_MaHoaCeasar_click)
        self.actionVignere_MaHoa.clicked.connect(self.on_MaHoaVignere_click)
        self.actionTrithemius_MaHoa.clicked.connect(self.on_MaHoaTrithemius_click)
        self.actionBelasco_MaHoa.clicked.connect(self.on_MaHoaBelasco_click)
    def on_MaHoaCeasar_click(self):######### [3]
        dialog = MyDialogMHVignere()
        dialog.exec()
    def on_MaHoaVignere_click(self):######### [3]
        dialog = MyDialogMHVignere()
        dialog.exec()
    def on_MaHoaTrithemius_click(self):######### [3]
        dialog = MyDialogMHTrithemius()
        dialog.exec()
    def on_MaHoaBelasco_click(self):######### [3]
        dialog = MyDialogMHBelasco()
        dialog.exec()
    def Close(self):
        choice = QMessageBox.question(self, "Xác nhận thoát", "Bạn có chắc muốn thoát ứng dụng?",
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if choice == QMessageBox.StandardButton.Yes:
            self.close()
        else:
            pass #nothing
    def MaHoa(self):
        self.textk = self.txtKey.toPlainText() #lấy dữ liệu trong text key của ThietKeMaHoaCeasar
        if not self.textk:
            QMessageBox.information(self, "Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey.setFocus()
        else:
            textpl = self.txtPlaintext.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaCeasar
            if not textpl:
                QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.btnOpenFile.setFocus()
            else:
                cCeasar= CCeasar(textpl,int(self.textk)) #khai báo đối tượng của lớp CCeasar
                c = cCeasar.MaHoa() #gọi hàm mã hoá của đối tượng này
                self.txtCiphertext.setPlainText(c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaCeasar
    def MoFile(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlaintext.setPlainText(fileContent)
    def GhiFile(self):
        # Lưu file dữ liệu đã mã hoá ciphertext
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtCiphertext.toPlainText())
            QMessageBox.information(self, "Thông báo", "Lưu file mã hoá thành công!!!!")

        # Lưu file KEY
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtKey.toPlainText())
            QMessageBox.information(self, "Thông báo", "Lưu file KEY thành công!!!!")
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
    mainMyDialog = MyDialogMHCeasar()
    mainMyDialog.show()
    sys.exit(app.exec())
#========================================================================================
if __name__ == "__main__":
    main()
