from tkinter import *
from tkinter.ttk import Combobox

class Teste:
    
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("teste")
        self.window.geometry("400x300")
        
        self.resolutions: tuple = ("144p", "360p", "480p", "720p", "1080p")
        
        self.frame3: Frame = Frame(self.window)
        self.frame3.pack()
        
        self.resolutions_options: Combobox = Combobox(self.frame3, values=self.resolutions, state="readonly")
        self.resolutions_options.set("Escolha a resolução")
        self.resolutions_options.pack(side="left")
        
        self.butom = Button(self.frame3, text="X", command=self.mo).pack()
        
        
        self.window.mainloop()
    
    def mostra(self):
        print(self.resolutions_options.get())
    
Teste()