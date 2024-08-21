import sys
sys.path.append("D:/DETAI_BMHTTT/Control")
from PyQt6.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox #[1]????????????
from ThietKe.ThietKeMaHoaXORCeasar import Ui_Dialog  
from mahoaXorCeasar_class import CXORCeasar #???????????
from GiaoDienMaHoaXORVignere import MyDialogMHXORVignere#import cửa sổ con [1]
from GiaoDienMaHoaXORTrithemius import MyDialogMHXORTrithemius#import cửa sổ con [1]
from GiaoDienMaHoaXORBelasco import MyDialogMHXORBelasco#import cửa sổ con [1]
#========================================================================================
class MyDialogMHXORCeasar(QDialog, Ui_Dialog):#[2]???????????????????????
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Thêm xử lý sự kiện và tuỳ chỉnh giao diện người dùng tại đây
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.btnMaHoa.clicked.connect(self.MaHoa)
        self.btnOpenFile.clicked.connect(self.MoFile)
        self.btnSaveFile.clicked.connect(self.GhiFile)
        self.btnClose.clicked.connect(self.Close)
        self.actionXORVignere_MaHoa.clicked.connect(self.on_MaHoaXORVignere_click) #[2]
        self.actionXORTrithemius_MaHoa.clicked.connect(self.on_MaHoaXORTrithemius_click) #[2]
        self.actionXORBelasco_MaHoa.clicked.connect(self.on_MaHoaXORBelasco_click) #[2]
    def on_MaHoaXORVignere_click(self):######### [3]
        dialog = MyDialogMHXORVignere()
        dialog.exec()
    def on_MaHoaXORTrithemius_click(self):######### [3]
        dialog = MyDialogMHXORTrithemius()
        dialog.exec()
    def on_MaHoaXORBelasco_click(self):######### [3]
        dialog = MyDialogMHXORBelasco()
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
                cXORCeasar= CXORCeasar() #khai báo đối tượng của lớp CCeasar
                c = cXORCeasar.MaHoa(textpl,int(self.textk)) #gọi hàm mã hoá của đối tượng này
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
    mainMyDialog = MyDialogMHXORCeasar()
    mainMyDialog.show()
    sys.exit(app.exec())
#========================================================================================
if __name__ == "__main__":
    main()
