from tkinter.messagebox import showerror, showinfo
from os import remove, system
from requests import get
from sys import exc_info
import customtkinter
import webbrowser
import tkinter


f=open(r'tlauncher.ico', "wb")
ufr = get("https://raw.githubusercontent.com/AvenCores/tlauncher-removead-python/master/ICO/tlauncher.ico")
f.write(ufr.content)
f.close()


infotext = """Данный патч отключает рекламу в TLauncher.

После нажатия кнопки "Патч" происходит запись серверов, откуда грузится реклама в файл Hosts, а при нажатии кнопки "Удалить патч" файл Hosts вернется к изначальному значению.

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
        f.writelines("\n127.0.0.1 repo.tlauncher.org/update/downloads/configs/inner_servers.json")
        f.writelines("\n127.0.0.1 advancedrepository.com/update/downloads/configs/inner_servers.json")
        f.writelines("\n127.0.0.1 ad.tlauncher.org")
        f.writelines("\n127.0.0.1 promo.tlauncher.org")
        f.writelines("\n127.0.0.1 stats.tlauncher.org")
        f.writelines("\n127.0.0.1 statistics.tlauncher.org")
        f.writelines("\n127.0.0.1 analytics.tlauncher.org")
        f.writelines("\n# End Tlauncher patcher by avencores (Tkinter version)")

        showinfo(title="Успешно", message="Патч был успешно установлен!")
    except:
        showerror(title="Ошибка", message=f"Патч не был установлен!\n\nОшибка: {exc_info()}")

def delpatch():
    try:
        f=open(r'hosts', "wb")
        ufr = get("https://pastebin.com/raw/PN5xTMsm")
        f.write(ufr.content)
        f.close()

        patchtodir = "C:\Windows\System32\drivers\etc\hosts"

        remove(patchtodir)
        system("copy hosts C:\Windows\System32\drivers\etc")

        showinfo(title="Успешно", message="Патч был успешно удален!")
    except:
        showerror(title="Ошибка", message=f"Патч не был удален!\n\nОшибка: {exc_info()}")
    remove("hosts")


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x400")
        self.title("Tlauncher RemoveAD")
        self.iconbitmap("tlauncher.ico")
        self.resizable(False, False)

        self.textbox  = customtkinter.CTkTextbox(self, width=350, height=200, border_width=2)
        self.textbox.place(x=200, y=120, anchor=tkinter.CENTER)
        self.textbox.insert("0.0", infotext)
        self.textbox.configure(state="disabled")

        self.button = customtkinter.CTkButton(self, text="Патч", width=100, command=patcher)
        self.button.place(x=135, y=250, anchor=tkinter.CENTER)

        self.button = customtkinter.CTkButton(self, text="Удалить Патч", width=100, command=delpatch)
        self.button.place(x=245, y=250, anchor=tkinter.CENTER)

        self.button = customtkinter.CTkButton(self, text="Автор утилиты", width=210, command=openavtor)
        self.button.place(x=190, y=290, anchor=tkinter.CENTER)

        self.button = customtkinter.CTkButton(self, text="Видео гайд (YouTube)", width=210, command=openyt)
        self.button.place(x=190, y=330, anchor=tkinter.CENTER)

        self.button = customtkinter.CTkButton(self, text="Скачать Lagacy Launcher", width=210, command=tllegavy)
        self.button.place(x=190, y=370, anchor=tkinter.CENTER)

if __name__ == "__main__":
    app = App()
    app.mainloop()

remove("tlauncher.ico")
