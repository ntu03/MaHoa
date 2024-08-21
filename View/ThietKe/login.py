import tkinter as tk
from tkinter import messagebox

def check_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "your_username" and password == "your_password":
        messagebox.showinfo("Thông báo", "Đăng nhập thành công!")
    else:
        messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng")

# Tạo cửa sổ
root = tk.Tk()
root.title("Giao diện đăng nhập")

# Tạo các Label và Entry cho tên đăng nhập và mật khẩu
username_label = tk.Label(root, text="Tên đăng nhập:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Mật khẩu:")
password_label.pack()
password_entry = tk.Entry(root, show="*")  # Mật khẩu hiển thị dưới dạng dấu sao
password_entry.pack()

# Tạo nút Đăng nhập
login_button = tk.Button(root, text="Đăng nhập", command=check_login)
login_button.pack()

# Main loop để hiển thị cửa sổ
root.mainloop()
