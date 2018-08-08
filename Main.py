import tkinter as tk

class Canvas():
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width = 1000, height = 700)
        self.canvas.pack()
        self.imageData = {
            "Background" : tk.PhotoImage(file = r"Frogger/Background.png"),
            "Player" : tk.PhotoImage(),
            "Car1" : tk.PhotoImage(file = r"Frogger/CarGreen.png"),
            "Car2" : tk.PhotoImage(),
            "Truck" : tk.PhotoImage(),
            "Bike" : tk.PhotoImage()
        }
        self.canvas.create_image(0,0, image = self.imageData["Background"], anchor = "nw")
        self.canvas.create_image(0,0, image = self.imageData["Car1"], anchor = "nw")


class Player():
    def __init__(self, root):
        self.root = root
        self.x = 500
        self.y = 670       
    
    def draw_player(self):
        pass

window = tk.Tk()
window.title("Frogger")
window.geometry("1000x700")
window.resizable(False, False)
window.update_idletasks()

user = Player(window)
board = Canvas(window)

window.mainloop()