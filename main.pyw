from tkinter.messagebox import showerror, showinfo
import customtkinter
import webbrowser
import tkinter


infotext = """Данный патч отключает рекламу в TLauncher.

После нажатия кнопки "Патч" происходит запись серверов, откуда грузится реклама в файл Hosts.

После патча желательно открыть командную строку и ввести команду "ipconfig /flushdns".

Если реклама осталась - перезагружай ПК, отключай VPN."""

def openavtor():
    webbrowser.open("https://t.me/avencores")

def tllegavy():
    webbrowser.open("https://tlaun.ch/?lang=ru")

def openyt():
    webbrowser.open("https://www.youtube.com/watch?v=XnjADh9xxYI")

def patcher():
    try:
        patchtodir = "C:\Windows\System32\drivers\etc\hosts"

        f = open(patchtodir, "a")
        f.writelines("\n\n# Tlauncher patcher by avencores (Tkinter version)")
        f.writelines("\n127.0.0.1 repo.tlauncher.org")
        f.writelines("\n127.0.0.1 advancedrepository.com")
        f.writelines("\n127.0.0.1 page.tlauncher.org")
        f.writelines("\n127.0.0.1 tmonitoring.com")
        f.writelines("\n127.0.0.1 tlauncher.org/repo/update/downloads/configs/inner_servers.json")
        f.writelines("\n127.0.0.1 tlauncher.org/repo/update/lch/additional_hot_servers.json")
        f.writelines("\n127.0.0.1 tlauncher.org/repo/update/lch/servers/hot_servers-1.0.json")
        f.writelines("\n127.0.0.1 tlauncher.org/repo/update/lch/additional_hot_servers-1.0.json")
        f.writelines("\n127.0.0.1 ad.tlauncher.org")
        f.writelines("\n127.0.0.1 promo.tlauncher.org")
        f.writelines("\n127.0.0.1 stats.tlauncher.org")
        f.writelines("\n127.0.0.1 statistics.tlauncher.org")
        f.writelines("\n127.0.0.1 analytics.tlauncher.org")
        f.writelines("\n# End Tlauncher patcher by avencores (Tkinter version)")
        showinfo(title="Успешно", message="Патч был успешно установлен!")
    except:
        showerror(title="Ошибка", message="Патч не был установлен!")


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x400")
        self.title("Tlauncher RemoveAD")
        self.iconbitmap("tlauncher.ico") # не работает при сборке
        self.resizable(False, False)

        self.frame = customtkinter.CTkTextbox(self, width=350, height=190, border_width=2)
        self.frame.place(x=200, y=130, anchor=tkinter.CENTER)
        self.frame.insert("0.0", infotext)

        self.button = customtkinter.CTkButton(self, text="Патч", width=200, command=patcher)
        self.button.place(x=200, y=250, anchor=tkinter.CENTER)

        self.button = customtkinter.CTkButton(self, text="Автор утилиты", width=200, command=openavtor)
        self.button.place(x=200, y=290, anchor=tkinter.CENTER)

        self.button = customtkinter.CTkButton(self, text="Видео гайд (YouTube)", width=200, command=openyt)
        self.button.place(x=200, y=330, anchor=tkinter.CENTER)

        self.button = customtkinter.CTkButton(self, text="Скачать TLaucnher (TL Legacy)", width=200, command=tllegavy)
        self.button.place(x=200, y=370, anchor=tkinter.CENTER)

if __name__ == "__main__":
    app = App()
    app.mainloop()