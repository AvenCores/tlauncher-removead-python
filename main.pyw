from tkinter.messagebox import showerror, showinfo
from os import remove, system, path
from requests import get
from sys import exc_info
import customtkinter
import webbrowser
import tkinter


ufr = get("https://raw.githubusercontent.com/AvenCores/tlauncher-removead-python/master/ICO/tlauncher.ico")
with open(r'tlauncher.ico', "wb") as f:
    f.write(ufr.content)


HOSTS_PATH = "C:\Windows\System32\drivers\etc\hosts"
HOSTS_ID_COMM = "Tlauncher patcher"


infotext = """Данный патч отключает рекламу в TLauncher.

После нажатия кнопки "Патч" происходит запись серверов, откуда грузится реклама в файл Hosts, а при нажатии кнопки "Удалить патч" файл Hosts вернется к изначальному значению.

После патча желательно открыть командную строку и ввести команду "ipconfig /flushdns".

Если реклама осталась - перезагружай ПК, отключай VPN."""

def openauthor():
    webbrowser.open("https://t.me/avencores")

def tllegacy():
    webbrowser.open("https://tlaun.ch/?lang=ru")

def openyt():
    webbrowser.open("https://www.youtube.com/watch?v=XnjADh9xxYI")

def patcher():
    try:
        with open(HOSTS_PATH, "a") as f:
            f.write(f"""\n\n# {HOSTS_ID_COMM} by avencores (Tkinter version)
127.0.0.1 repo.tlauncher.org
127.0.0.1 advancedrepository.com
127.0.0.1 page.tlauncher.org
127.0.0.1 tmonitoring.com
127.0.0.1 tlauncher.org/repo/update/downloads/configs/inner_servers.json
127.0.0.1 tlauncher.org/repo/update/lch/additional_hot_servers.json
127.0.0.1 tlauncher.org/repo/update/lch/servers/hot_servers-1.0.json
127.0.0.1 tlauncher.org/repo/update/lch/additional_hot_servers-1.0.json
127.0.0.1 repo.tlauncher.org/update/downloads/configs/inner_servers.json
127.0.0.1 advancedrepository.com/update/downloads/configs/inner_servers.json
127.0.0.1 ad.tlauncher.org
127.0.0.1 promo.tlauncher.org
127.0.0.1 stats.tlauncher.org
127.0.0.1 statistics.tlauncher.org
127.0.0.1 analytics.tlauncher.org
# End {HOSTS_ID_COMM} by avencores (Tkinter version)\n\n""")

        showinfo(title="Успешно", message="Патч был успешно установлен!")
    except:
        showerror(title="Ошибка", message=f"Патч не был установлен!\n\nОшибка: {exc_info()}")

def delpatch():
    try:
        with open(HOSTS_PATH, 'r') as f:
            original_hosts = f.read()
        
        # Находит начало по комментарию в файле
        start = original_hosts.find(f"# {HOSTS_ID_COMM}")
        # Сначала ищет заканчивающий "# End", а затем находит конец этой линии
        end = original_hosts.find("\n", original_hosts.find("# End", start)) + 1
        
        with open('hosts', 'w+') as f:
            f.write(original_hosts[:start] + original_hosts[end:])
        remove(HOSTS_PATH)
        system(f"copy hosts {path.dirname(HOSTS_PATH)}")

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
        self.title("TLauncher RemoveAD")
        self.iconbitmap("tlauncher.ico")
        self.resizable(False, False)

        self.textbox  = customtkinter.CTkTextbox(self, width=350, height=200, border_width=2)
        self.textbox.insert("0.0", infotext)
        self.textbox.configure(state="disabled")
        self.textbox.place(x=200, y=120, anchor=tkinter.CENTER)

        self.button_patch = customtkinter.CTkButton(self, text="Патч", width=100, command=patcher)
        self.button_patch.place(x=135, y=250, anchor=tkinter.CENTER)

        self.button_unpatch = customtkinter.CTkButton(self, text="Удалить Патч", width=100, command=delpatch)
        self.button_unpatch.place(x=245, y=250, anchor=tkinter.CENTER)

        self.button_tg = customtkinter.CTkButton(self, text="Автор утилиты", width=210, command=openauthor)
        self.button_tg.place(x=190, y=290, anchor=tkinter.CENTER)

        self.button_yt = customtkinter.CTkButton(self, text="Видео гайд (YouTube)", width=210, command=openyt)
        self.button_yt.place(x=190, y=330, anchor=tkinter.CENTER)

        self.button_legacy = customtkinter.CTkButton(self, text="Скачать Lagacy Launcher", width=210, command=tllegacy)
        self.button_legacy.place(x=190, y=370, anchor=tkinter.CENTER)

if __name__ == "__main__":
    app = App()
    app.mainloop()

remove("tlauncher.ico")
