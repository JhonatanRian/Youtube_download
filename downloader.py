from tkinter import *
from tkinter import filedialog
from pytube import YouTube


class Downloader:


    def __init__(self) -> None:
        self.window: Tk = Tk()
        self.window.title("Youtube_Downloader")
        self.window.resizable(0, 0)
        self.window.geometry('640x480+300+200')
        
        self.img_logo: PhotoImage = PhotoImage(file = "img/1x/youtube_logo_white.png")
        
        self.audio: bool = False
        self.video: bool = False
        
        self.frame: Frame = Frame(self.window, bg = "#C9020C")
        self.frame.pack(fill="x")
        
        self.label_logo: Label = Label(self.frame, image = self.img_logo, bg = "#C9020C")
        self.label_logo.pack()
        
        self.frame2: Frame = Frame(self.window, pady = 20)
        self.frame2.pack()
        
        self.label_insert: Label = Label(self.frame2, text = " Insert link: ", font = 'arial 12')
        self.label_insert.pack(side = 'left')
        
        self.link: Entry = Entry(self.frame2, font = "arial 16", width = 40)
        self.link.pack(side = "left")
        
        self.play: Button = Button(self.frame2, bg = "red", text = ">", bd = 0, command = lambda: self.download(self.link.get()))
        self.play.pack(side = "left")
        
        self.frame3: Frame = Frame(self.window)
        self.frame3.pack()
        
        self.radio: Radiobutton = Radiobutton(self.frame3, text = "Audio", value = 0, command = self.validate_audio)
        self.radio.pack(side = "left")
        self.radio2: Radiobutton = Radiobutton(self.frame3, text = "Video", value = 1, command = self.validate_video)
        self.radio2.pack(side = "left")
        self.radio3: Radiobutton = Radiobutton(self.frame3, text = "Audio and Video", value = 2, command = self.validate_all)
        self.radio3.pack(side = "left")
        
        self.window.mainloop()
    
    def validate_audio(self: object) -> None:
        self.audio: bool = True
        self.video: bool = False
    
    def validate_video(self: object) -> None:
        self.video: bool = True
        self.audio: bool = False
        
    def validate_all(self: object) -> None:
        self.audio: bool = False
        self.video: bool = False
        

    def download(self: object, link: str) -> None:
        try:
            if self.audio:
                file = filedialog.askdirectory()
                YouTube(link).streams.filter(only_audio = True).get_highest_resolution().download(file)
                self.complete()
            elif self.video:
                file = filedialog.askdirectory()
                YouTube(link).streams.filter(only_video = True).get_highest_resolution().download(file)
                self.complete()
            else:
                file = filedialog.askdirectory()
                YouTube(link).streams.get_highest_resolution().download(file)
                self.complete()
        except:
            self.msg()
    
    def msg(self: object) -> None:
        windom: Toplevel = Toplevel()
        windom.title("ERROR")
        windom.resizable(0, 0)
        windom.geometry("300x200+300+200")
        
        texto: Label = Label(windom, text = "The link is not valid", pady = 30)
        texto.pack()
        
        ok: Button = Button(windom, text = "OK", command = windom.destroy)
        ok.pack()
        
    def complete(self: object) -> None:
        windom: Toplevel = Toplevel()
        windom.title("COMPLETED")
        windom.resizable(0, 0)
        windom.geometry("300x200+300+200")
        
        texto: Label = Label(windom, text = "Download completed", pady = 30)
        texto.pack()
        
        ok: Button = Button(windom, text = "OK", command = windom.destroy)
        ok.pack()
        
Downloader()