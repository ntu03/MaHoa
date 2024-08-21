import sys
sys.path.append("D:/DETAI_BMHTTT/Control")
from PyQt6.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox #[1]????????????
from ThietKe.ThietKeGiaiMaXORCeasar import Ui_Dialog  #?????????????????
from mahoaXorCeasar_class import CXORCeasar #???????????
from GiaoDienGiaiMaXORVignere import MyDialogGMXORVignere #[4]
from GiaoDienGiaiMaXORTrithemius import MyDialogGMXORTrithemius #[4]
from GiaoDienGiaiMaXORBelasco import MyDialogGMXORBelasco #[4]
#========================================================================================
class MyDialogGMXORCeasar(QDialog, Ui_Dialog):#[2]???????????????????????
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Thêm xử lý sự kiện và tuỳ chỉnh giao diện người dùng tại đây
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.btnGiaiMa.clicked.connect(self.GiaiMa) #????????????????????????
        self.btnOpenFile.clicked.connect(self.MoFile)
        self.btnSaveFile.clicked.connect(self.GhiFile)
        self.btnClose.clicked.connect(self.Close)
        self.actionXORVignere_GiaiMa.clicked.connect(self.on_GiaiMaXORVignere_click)
        self.actionXORTrithemius_GiaiMa.clicked.connect(self.on_GiaiMaXORTrithemius_click)
        self.actionXORBelasco_GiaiMa.clicked.connect(self.on_GiaiMaXORBelasco_click)
    def on_GiaiMaXORVignere_click(self):
        dialog = MyDialogGMXORVignere()
        dialog.exec()
    def on_GiaiMaXORTrithemius_click(self):
        dialog = MyDialogGMXORTrithemius()
        dialog.exec()
    def on_GiaiMaXORBelasco_click(self):
        dialog = MyDialogGMXORBelasco()
        dialog.exec()
    def Close(self):
        choice = QMessageBox.question(self, "Xác nhận thoát", "Bạn có chắc muốn thoát ứng dụng?",
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if choice == QMessageBox.StandardButton.Yes:
            self.close()
        else:
            pass #nothing
    def GiaiMa(self):
        self.textk=self.txtKey.toPlainText()
        if not self.textk:
            QMessageBox.information(self, "Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey.setFocus()
        else:
            textci = self.txtCiphertext.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaCeasar
            if not textci:
                QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.btnOpenFile.setFocus()
            else:
                cCeasar= CXORCeasar() #khai báo đối tượng của lớp CCeasar
                s = cCeasar.MaHoa(textci,int(self.textk)) #gọi hàm mã hoá của đối tượng này
                self.txtVanBanGoc.setPlainText(s) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaCeasar
    def MoFile(self):
        # Mở file đã mã hoá riêng
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                s=''
                line = file.readline()
                while line:
                    s+=line
                    line = file.readline()
                self.txtCiphertext.setPlainText(s)
        # Mở file KEY riêng
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk = file.read()
                self.txtKey.setPlainText(self.textk)
                
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
    mainMyDialog = MyDialogGMXORCeasar()
    mainMyDialog.show()
    sys.exit(app.exec())
#========================================================================================
if __name__ == "__main__":
    main()
