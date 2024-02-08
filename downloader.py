
from tkinter import filedialog, Scrollbar
from ttkbootstrap import (Button, Window, Entry, Canvas, Label, Progressbar, Combobox,
                          Frame, VERTICAL, HORIZONTAL, LabelFrame, PhotoImage, Toplevel, Menu,
                          Scrollbar)
import ssl
from utils.get_path_donwload import get_download_folder
from utils.helpers import DownloadYt, generate_title
from threading import Thread
from pytube.exceptions import AgeRestrictedError
import os
import sys

ssl._create_default_https_context = ssl._create_stdlib_context


class Downloader:

    def __init__(self) -> None:
        self.path_download = get_download_folder()
        self.window: Window = Window(title="My Application", themename="superhero")
        self.window.title("Youtube_Downloader")
        self.window.resizable(0, 0)
        self.downloads = {}
        self.window.geometry('640x480+300+200')
        self.load_statics()
        self.load_menu()
        self.load_frames()
        self.load_widgets()
        self.label_path_download = Label(self.frame4, text='Caminho para download: ' + self.path_download)
        self.label_path_download.pack(side='bottom')
        self.window.mainloop()
    
    def load_statics(self) -> None:
        resource_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        self.img_logo: PhotoImage = PhotoImage(file=os.path.join(resource_dir, "img/1x/youtube_logo_white.png"))

    def load_frames(self) -> None:
        self.frame: Frame = Frame(self.window)
        self.frame.pack(fill="x")
        self.frame2: Frame = Frame(self.window)
        self.frame2.pack(pady=20)
        self.frame3: Frame = Frame(self.window)
        self.frame3.pack(fill='both', expand=True)
        self.frame4: Frame = Frame(self.window)
        self.frame4.pack(pady=2)
    
    def load_menu(self):
        self.menu_main = Menu(self.window)
        self.menu_file = Menu(self.menu_main, tearoff=0)

        self.menu_file.add_command(label="Caminho para download", command=self.get_path_donwload, accelerator="Ctrl+D")
        self.window.bind("<Control-d>", self.get_path_donwload_event)
        self.menu_main.add_cascade(label='Arquivo', menu=self.menu_file)

        self.window.config(menu=self.menu_main)
    
    def load_widgets(self):
        self.label_logo: Label = Label(self.frame, image=self.img_logo)
        self.label_logo.pack()

        self.label_insert: Label = Label(self.frame2, text=" Insert link: ", font='arial 12')
        self.label_insert.pack(side='left')

        self.link: Entry = Entry(self.frame2, font="arial 12", width=50)
        self.link.pack(side="left")

        self.button_download: Button = Button(self.frame2, text='Download', width=70, command=self.info_file)
        self.button_download.pack(side="left", padx=10)

        label_frame_downloads = LabelFrame(self.frame3, bootstyle="light", text="Downloads")
        label_frame_downloads.pack(fill='both', padx=10, expand=True)

        self.list_donwload_canvas = Canvas(label_frame_downloads)
        self.list_donwload_canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar = Scrollbar(label_frame_downloads, orient=VERTICAL, command=self.list_donwload_canvas.yview)
        self.scrollbar.pack(side="right", fill="y", padx=4, pady=2)
        self.list_donwload_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.list_donwload_canvas.bind("<Configure>", self.on_canvas_configure)
        self.inner_frame = Frame(self.list_donwload_canvas, width=610)
        self.inner_frame.pack(fill="both", expand=True)
        self.list_donwload_canvas.create_window((0, 0), window=self.inner_frame, anchor="center", tags='inner_frame')
        self.list_donwload_canvas.update_idletasks()
        self.list_donwload_canvas.itemconfigure('inner_frame')
        self.list_donwload_canvas.config(scrollregion=self.list_donwload_canvas.bbox("all"))


    def info_file(self) -> None:
        """
        Info_file receives the download link, gets the location where the video
        will be saved and writes in the download characteristics listbox
        """
        window: Toplevel = Toplevel()
        window.title("resolution")
        window.resizable(0, 0)
        window.geometry("300x200+300+200")

        frame: Frame = Frame(window)
        frame.pack(fill="x", pady=30)

        text = Label(frame, text="Selecione a resolução")
        text.pack(anchor='center')
        try:
            self.yt = DownloadYt(self.link.get())
            title = generate_title(self.yt.title, list(self.downloads.keys()))
            self.downloads[title] = self.yt
            self.resolutions_option: Combobox = Combobox(frame, values=list(self.yt.resolutions.keys()),
                                                     state="readonly",)
            self.resolutions_option.pack()

            frame2: Frame = Frame(window)
            frame2.pack(fill="x", side="bottom", pady=30)
            ok: Button = Button(frame2, text = "OK", command=lambda: self.capture_resolution(window, title))
            ok.pack()
        except AgeRestrictedError:
            window.destroy()
            self.msg("Este video tem restrição de idade!\nFaça login")
            self.msg()
            return
        except Exception as err:
            window.destroy()
            self.msg()

    def capture_resolution(self, window, title) -> None:
        resolution = self.resolutions_option.get()
        self.downloads[title].resolution = self.downloads[title].resolutions.get(resolution)
        Thread(target=self.download, args=[title]).start()
        window.destroy()

    def get_path_donwload(self):
        self.path_download = filedialog.askdirectory()
        self.label_path_download.configure(text='Caminho para download: ' + self.path_download)
    
    def get_path_donwload_event(self, event):
        self.get_path_donwload()

    def download(self, title) -> None:
        yt = self.downloads.get(title)
        f = Frame(self.inner_frame)
        f.pack(pady=3, anchor='center', expand=True)
        title = Label(f, text=title)
        title.pack(anchor='center', padx=3)
        progress = Progressbar(f, orient=HORIZONTAL, length=350,maximum=100, mode='determinate', bootstyle="warning-striped")
        progress.pack(pady=2, padx=5, anchor='center')
        self.on_canvas_configure(None)
        yt.progress_bar = progress
        yt.yt.register_on_progress_callback(self.on_progress)
        yt.yt.register_on_complete_callback(self.on_complete)
        yt.resolution.download(self.path_download)

    def on_complete(self, vid, chunk):
        yt = self.downloads[vid.title]
        yt.progress_bar.configure(bootstyle="success-striped")

    def on_progress(self, vid, chunk, bytes_remaining):
        yt = self.downloads[vid.title]
        total_size = vid.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100
        totalsz = (total_size/1024)/1024
        totalsz = round(totalsz,1)
        remain = (bytes_remaining / 1024) / 1024
        remain = round(remain, 1)
        dwnd = (bytes_downloaded / 1024) / 1024
        dwnd = round(dwnd, 1)
        percentage_of_completion = round(percentage_of_completion,2)
        yt.progress_bar.configure(value=percentage_of_completion)
        # print(f'Download Progress: {percentage_of_completion}%, Total Size:{totalsz} MB, Downloaded: {dwnd} MB, Remaining:{remain} MB')



    def msg(self, msg: str = 'Link Inválido!') -> None:
        windom: Toplevel = Toplevel()
        windom.title("ERROR")
        windom.resizable(0, 0)
        windom.geometry("300x200+300+200")
        texto: Label = Label(windom, text=msg)
        texto.pack(pady=30)
        
        ok: Button = Button(windom, text = "OK", command = windom.destroy)
        ok.pack()

    def on_canvas_configure(self, event):
        self.list_donwload_canvas.update_idletasks()
        self.list_donwload_canvas.configure(
            scrollregion=self.list_donwload_canvas.bbox("all")
        )



if __name__ == "__main__":
    Downloader()