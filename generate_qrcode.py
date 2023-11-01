import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode

class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Kod Oluşturucu")

        self.create_widgets()

    def create_widgets(self):
        self.url_label = tk.Label(self.root, text="URL Girin:")
        self.url_label.pack(pady=10)

        self.url_entry = tk.Entry(self.root, width=40)
        self.url_entry.pack()

        self.generate_button = tk.Button(self.root, text="QR Kodu Oluştur", command=self.generate_qr_code)
        self.generate_button.pack(pady=10)

        self.quit_button = tk.Button(self.root, text="Çıkış", command=self.root.quit)
        self.quit_button.pack()

    def generate_qr_code(self):
        input_URL = self.url_entry.get().strip()

        if not input_URL:
            messagebox.showerror("Hata", "Lütfen bir URL girin.")
            return

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=15,
            border=4,
        )

        qr.add_data(input_URL)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if not file_path:
            return

        img.save(file_path)
        messagebox.showinfo("Başarılı", f"QR Kodu başarıyla oluşturuldu ve '{file_path}' konumuna kaydedildi.")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()
