import tkinter as tk

class Canvas():
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width = 1000, height = 700)
        self.canvas.pack()
        self.imageData = {
            "Background" : tk.PhotoImage(file = r"Frogger/Background.png"),
            "Player" : tk.PhotoImage(file = r"Frogger/avatar.png"),
            "Car1" : tk.PhotoImage(file = r"Frogger/CarGreen.png"),
            "Car2" : tk.PhotoImage(file = r"Frogger/CarSilver.png"),
            "Car3" : tk.PhotoImage(file = r"Frogger/CarBlue.png"),
            "Car4" : tk.PhotoImage(file = r"Frogger/CarBrown.png"),
            "Bus" : tk.PhotoImage(file = r"Frogger/Bus.png"),
            "Bike" : tk.PhotoImage()
        }
        self.canvas.create_image(0, 0, image = self.imageData["Background"], anchor = "nw")

    def get_canvas(self):
        return self.canvas

    

class Player():
    def __init__(self, root, canvas):
        self.x = 500
        self.y = 650
        self.root = root
        self.canvas = canvas
        self.player = self.canvas.get_canvas().create_image(self.x, self.y, image = self.canvas.imageData["Player"], anchor = "nw")
        self.root.bind("<Left>", lambda event, direction = "left": self.move(direction))
        self.root.bind("<Right>", lambda event, direction = "right": self.move(direction))
        self.root.bind("<Up>", lambda event, direction = "up": self.move(direction))
        self.root.bind("<Down>", lambda event, direction = "down": self.move(direction))

    def move(self, direction):
        if direction == "right":
            if(self.x == 950):
                pass
            else:
                self.x += 45
                self.canvas.get_canvas().delete(self.player)
                self.player = self.canvas.get_canvas().create_image(self.x, self.y, image = self.canvas.imageData["Player"], anchor = "nw")
                self.root.update()
        elif direction == "left":
            if(self.x == 5):
                pass
            else:    
                self.x -= 45
                self.canvas.get_canvas().delete(self.player)
                self.player = self.canvas.get_canvas().create_image(self.x, self.y, image = self.canvas.imageData["Player"], anchor = "nw")
                self.root.update()
        elif direction == "up":
            if(self.y == 50):
                pass
            else:
                self.y -= 60
                self.canvas.get_canvas().delete(self.player)
                self.player = self.canvas.get_canvas().create_image(self.x, self.y, image = self.canvas.imageData["Player"], anchor = "nw")
                self.root.update()
        elif direction == "down":
            if(self.y == 650):
                pass
            else:
                self.y += 60
                self.canvas.get_canvas().delete(self.player)
                self.player = self.canvas.get_canvas().create_image(self.x, self.y, image = self.canvas.imageData["Player"], anchor = "nw")
                self.root.update() 

class Obstacle():
    def __init__(self, root):
        self.root = root
        self.x = 0
        self.y = 0        

window = tk.Tk()
window.title("Frogger")
window.geometry("1000x700")
window.resizable(False, False)
window.update_idletasks()

board = Canvas(window)
user = Player(window, board)

window.mainloop()
