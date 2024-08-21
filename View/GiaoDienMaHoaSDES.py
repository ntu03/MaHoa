import sys
sys.path.append("D:/DETAI_BMHTTT/Control")
from PyQt6.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox #[1]????????????
from ThietKe.ThietKeMaHoaSDES import Ui_Dialog  
import mahoaSDES #???????????
from GiaoDienMaHoaRSA import MyDialogMHRSA#import cửa sổ con [1]
from GiaoDienMaHoaAES import MyDialogMHAES#import cửa sổ con [1]

#========================================================================================
class MyDialogMHSDES(QDialog, Ui_Dialog):#[2]???????????????????????
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Thêm xử lý sự kiện và tuỳ chỉnh giao diện người dùng tại đây
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.c = ''
        self.btnMaHoa.clicked.connect(self.MaHoa)
        self.btnOpenFile.clicked.connect(self.MoFile)
        self.btnSaveFile.clicked.connect(self.GhiFile)
        self.btnClose.clicked.connect(self.Close)
        self.actionRSA_MaHoa.clicked.connect(self.on_MaHoaRSA_click) #[2]
        self.actionAES_MaHoa.clicked.connect(self.on_MaHoaAES_click) #[2]
    def on_MaHoaRSA_click(self):######### [3]
        dialog = MyDialogMHRSA()
        dialog.exec()
    def on_MaHoaAES_click(self):######### [3]
        dialog = MyDialogMHAES()
        dialog.exec()
    def Close(self):
        choice = QMessageBox.question(self, "Xác nhận thoát", "Bạn có chắc muốn thoát ứng dụng?",
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if choice == QMessageBox.StandardButton.Yes:
            self.close()
        else:
            pass #nothing
    def MaHoa(self):
        self.textk = self.txtKey.toPlainText() #lấy dữ liệu trong text key của ThietKeMaHoaVignere
        if not self.textk:
            QMessageBox.information(self, "Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey.setFocus()
        else:
            textpl = self.txtPlaintext.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaVignere
            if not textpl:
                QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.btnOpenFile.setFocus()
            else:
                self.c = mahoaSDES.MaHoa(textpl,self.textk) #gọi hàm mã hoá của đối tượng này
                self.txtCiphertext.setPlainText(self.c) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaVignere
    def MoFile(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlaintext.setPlainText(fileContent)
    def GhiFile(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.c)
                
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.textk)
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
    mainMyDialog = MyDialogMHSDES()
    mainMyDialog.show()
    sys.exit(app.exec())
#========================================================================================
if __name__ == "__main__":
    main()
