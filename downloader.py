from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from pytube import YouTube


class Downloader:

    def __init__(self) -> None:
        #  creating window
        self.window: Tk = Tk()
        self.window.title("Youtube_Downloader")
        self.window.resizable(0, 0)
        self.window.geometry('640x480+300+200')
        
        #  Attribute representing download options
        self.resolutions: tuple = ("144p", "360p", "480p", "720p", "1080p", "apenas audio")
        
        #  Attributes that receive the images and icons for the look
        self.img_logo: PhotoImage = PhotoImage(file="img/1x/youtube_logo_white.png")
        self.img_file: PhotoImage = PhotoImage(file="img/file.png")
        self.img_download: PhotoImage = PhotoImage(file="img/download.png")
        self.img_quality: PhotoImage = PhotoImage(file="img/quality.png")
        
        #  Logo frame
        self.frame: Frame = Frame(self.window, bg="#C9020C")
        self.frame.pack(fill="x")
        self.label_logo: Label = Label(self.frame, image=self.img_logo, bg="#C9020C")
        self.label_logo.pack()
        
        #  Frame that receives features for data entry
        self.frame2: Frame = Frame(self.window, pady=20)
        self.frame2.pack()
        
        self.label_insert: Label = Label(self.frame2, text=" Insert link: ", font='arial 12')
        self.label_insert.pack(side='left')
        
        self.link: Entry = Entry(self.frame2, font="arial 12", width=30)
        self.link.pack(side="left")
        
        self.file_button: Button = Button(self.frame2, image=self.img_file, border=0, width=60, command=self.info_file)
        self.file_button.pack(side="left")
        
        self.resolutions_options: Combobox = Combobox(self.frame2, values=self.resolutions, state="readonly")
        self.resolutions_options.set("Escolha a resolução")
        self.resolutions_options.pack(side="left")
        
        #  Frame where it will show the status of the file
        self.frame3: Frame = Frame(self.window, pady=30)
        self.frame3.pack()
        
        self.info: Listbox = Listbox(self.frame3, relief="flat", width=55, height=40)
        self.info.pack(side="left")
        
        self.button_download: Button = Button(self.frame3, image=self.img_download, border=0, width=70, command=self.download)
        self.button_download.pack(side="left")
        
        
        
        self.window.mainloop()
    
    
    def info_file(self) -> None:
        """
        Info_file receives the download link, gets the location where the video
        will be saved and writes in the download characteristics listbox
        """
        self.info.delete(0, END)
        self.info.insert(1,"»» YouTube Download Init")
        try:
            self.info_video_()
            self.info.insert(1,55*"=")
            self.info.insert(1, f"»» Title: {self.video_title}")
            self.info.insert(2, f"»» Author: {self.video_author}")
            self.info.insert(3, f"»» length: {self.video_lenght}")
            self.info.insert(1, 55*"=")
        except:
            self.msg()
            
    def info_video_(self: object):
        self.video_info: YouTube = YouTube(self.link.get())
        self.video_author: YouTube = self.video_info.author
        self.video_title: YouTube = self.video_info.title
        self.video_lenght: YouTube = self.video_info.length
        self.file : filedialog = filedialog.askdirectory()
        
    def download(self: object) -> None:
        """
        """
        self.info.delete(0, END)
        try:
            if self.resolutions_options.get() == "audio/mp3":
                self.video_info.streams.get_audio_only().download(self.file)
                self.info.insert(1,"»» DOWNLOAD CONCLUDED")
                self.info.insert(1, f"»» Title: {self.video_title}")
            elif self.resolutions_options.get() == "Escolha a resolução":
                self.video_info.streams.get_highest_resolution().download(self.file)
                self.info.insert(1,"»» DOWNLOAD CONCLUDED")
                self.info.insert(1, f"»» Title: {self.video_title}")
            else:
                self.info.insert(1, f"»» resolution: {self.resolutions_options.get()}")
                self.video_info.streams.get_by_resolution(self.resolutions_options.get()).download(self.file)
                self.info.insert(1,"»» DOWNLOAD CONCLUDED")
                self.info.insert(1, f"»» Title: {self.video_title}")
        except:
            self.info.delete(0, END)
            self.info.insert(1,"»» Something went wrong.")
            self.info.insert(1,"»» Verify the chosen folder.")
            self.info.insert(1,"»» Try changing resolutions.")
    
    def msg(self: object) -> None:
        windom: Toplevel = Toplevel()
        windom.title("ERROR")
        windom.resizable(0, 0)
        windom.geometry("300x200+300+200")
        
        texto: Label = Label(windom, text = "The link is not valid", pady = 30)
        texto.pack()
        
        ok: Button = Button(windom, text = "OK", command = windom.destroy)
        ok.pack()
            
        
Downloader()