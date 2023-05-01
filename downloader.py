from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from pytube import YouTube, Stream


class Downloader:

    def __init__(self) -> None:
        #  creating window
        self.window: Tk = Tk()
        self.window.title("Youtube_Downloader")
        self.window.resizable(0, 0)
        self.window.geometry('640x480+300+200')
        
        
        #  Attributes that receive the images and icons for the look
        self.img_logo: PhotoImage = PhotoImage(file="img/1x/youtube_logo_white.png")
        self.img_file: PhotoImage = PhotoImage(file="img/file.png")
        self.img_download: PhotoImage = PhotoImage(file="img/download.png")
        
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
        
        # self.resolutions_options: Combobox = Combobox(self.frame2, values=self.resolutions, state="readonly")
        # self.resolutions_options.set("Escolha a resolução")
        # self.resolutions_options.pack(side="left")
        
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
        window: Toplevel = Toplevel()
        window.title("resolution")
        window.resizable(0, 0)
        window.geometry("300x200+300+200")

        frame: Frame = Frame(window, pady=30)
        frame.pack(fill="x")
        self.info_video_()
        self.resolutions_option: Combobox = Combobox(frame, values=self.resolutions, state="readonly",)
        self.resolutions_option.pack()
        frame2: Frame = Frame(window, pady=30)
        frame2.pack(fill="x", side="bottom")
        ok: Button = Button(frame2, text = "OK", command = window.destroy)
        ok.pack()

        self.info.delete(0, END)
        self.info.insert(1,"»» YouTube Download Init")
        try:
            self.info.insert(1,55*"=")
            self.info.insert(1, f"»» Title: {self.yt.title}")
            self.info.insert(2, f"»» Author: {self.yt.author}")
            self.info.insert(3, f"»» length: {self.yt.lenght}")
            self.info.insert(3, f"»» initial_data: {self.yt.initial_data}")
            self.info.insert(1, 55*"=")
        except:
            # self.msg()
            print("erro")
            
    def info_video_(self: object):
        self.yt: YouTube = YouTube(self.link.get())
        self.resolutions = [StreamYt(stream) for stream in self.yt.streams.filter(progressive=True)] + [StreamYt(stream) for stream in self.yt.streams.filter(only_audio=True)]
        self.file : filedialog = filedialog.askdirectory()
        
    def download(self: object) -> None:
        """
        """
        self.info.delete(0, END)
        try:
            resolution = self.resolutions_option.get()
            itag = resolution.stream.itag
            stream = self.yt.strams.get_by_itag(itag)
            stream.download()
            self.info.insert(1,"»» Download Conclude")
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
            
class StreamYt:
    def __init__(self, stream: Stream) -> None:
        self.__stream: Stream = stream

    @property
    def stream(self: object) -> Stream:
        return self.__stream

    def __str__(self: object) -> str:
        return f" {self.__stream.mime_type} {self.__stream.res}"

if __name__ == "__main__":
    Downloader()