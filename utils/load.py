from ttkbootstrap import Frame, Label, Canvas
import math


class LoadingScreen(Frame):
    def __init__(self, master, text="Carregando..."):
        super().__init__(master)
        self.title("Carregando")
        self.geometry("200x100")
        self.text = text
        self.label = Label(self, text=self.text)
        self.label.pack(pady=10)
        self.canvas = Canvas(self, width=100, height=100)
        self.canvas.pack()
        self.arrow_length = 30
        self.angle = 0
        self.after(100, self.animate_loading)

    def draw_arrow(self):
        x0, y0 = 50, 50
        x1 = x0 + self.arrow_length * math.cos(math.radians(self.angle))
        y1 = y0 + self.arrow_length * math.sin(math.radians(self.angle))
        self.canvas.create_line(x0, y0, x1, y1, arrow='last', width=5, fill="black")

    def animate_loading(self):
        self.canvas.delete("all")
        self.draw_arrow()
        self.angle = (self.angle + 10) % 360
        self.after(100, self.animate_loading)
