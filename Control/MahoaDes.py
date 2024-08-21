from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
#===========================================================
# Mã hóa
def Encrypt(plaintext,key):
    cipher = DES.new(key, DES.MODE_ECB)
    data = plaintext.encode('utf-8')
    padded_data = pad(data, 8)
    ciphertext = cipher.encrypt(padded_data)
    return ciphertext
# Giải mã
def Decrypt(ciphertext,key):
    decipher = DES.new(key, DES.MODE_ECB)
    decrypted_text= unpad(decipher.decrypt(ciphertext), 8)
    return decrypted_text.decode('utf-8')
#=============================================================
def Run():
    plaintext = input('Mời nhập chuỗi cần mã hoá: ')
    print("Plaintext:", plaintext)
    key = get_random_bytes(8)
    ciphertext = Encrypt(plaintext,key)
    print("Ciphertext:", ciphertext)
    decrypted_text = Decrypt(ciphertext,key)
    print("Decrypted Text:", decrypted_text)
'''
Hãy nhớ rằng DES không nên được sử dụng trong ứng dụng thực tế
vì nó đã bị phá vỡ bởi nhiều phương pháp tấn công.
AES là một lựa chọn mã hóa tốt hơn cho các ứng dụng hiện đại.
'''
#==============================================================
if __name__ =='__main__':
    Run()
