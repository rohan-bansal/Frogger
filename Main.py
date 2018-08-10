import tkinter as tk
from tkinter import messagebox
import time
import os, sys

try:
    import pygame
except ImportError:
    if messagebox.askyesno('ImportFix', 'There are missing dependencies needed for the program to work (module "pygame"). Would you like the program to install them?\
    \nRestart the app after installation.') == True:    
        import subprocess
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--user', 'pygame'])
        import pygame
    else:
        sys.exit()

class Canvas():
    def __init__(self, root):
        self.root = root
        path = os.path.dirname(os.path.abspath(__file__))
        print(path)

        self.imageData = {
            "Background" : tk.PhotoImage(file = path + "/Images/Background.png"),
            "Player" : tk.PhotoImage(file = path + "/Images/avatar.png"),   
            "Car4" : tk.PhotoImage(file = path + "/Images/CarGreen.png"),
            "Car2" : tk.PhotoImage(file = path + "/Images/CarSilver.png"),
            "Car3" : tk.PhotoImage(file = path + "/Images/CarBlue.png"),
            "Car1" : tk.PhotoImage(file = path + "/Images/CarBrown.png"),
            "Bus" : tk.PhotoImage(file = path + "/Images/Bus.png"),
            "Bike" : tk.PhotoImage(file = path + "/Images/Bike.png")
        }

        self.canvas = tk.Canvas(self.root, width = 1000, height = 700)
        self.canvas.pack()

        background = self.canvas.create_image(0, 0, image = self.imageData["Background"], anchor = "nw")



    def get_canvas(self):
        return self.canvas

class Vehicle():
    ID = ""
    def __init__(self, canvas, row):
        self.row = row
        if row == 1:
            self.image = canvas.imageData['Car2']
            self.x = 0
            self.direc = "right"
            self.y = 560
            self.speed = 3
        elif row == 2:
            self.image = canvas.imageData['Car3']
            self.x = 900
            self.direc = "left"
            self.y = 470
            self.speed = 4
        elif row == 3:
            self.image = canvas.imageData['Car1']
            self.x = 0
            self.direc = "right"
            self.y = 380
            self.speed = 3
        elif row == 4:
            self.image = canvas.imageData['Car4']
            self.x = 900
            self.direc = "left"
            self.y = 305
            self.speed = 6
        elif row == 5:
            self.image = canvas.imageData['Bus']
            self.x = 0
            self.direc = "right"
            self.y = 235
            self.speed = 2
        elif row == 6:
            self.image = canvas.imageData['Bike']
            self.x = 900
            self.direc = "left"
            self.y = 150
            self.speed = 1

    def move(self):
        if self.direc == "right":
            self.x += self.speed
        else:
            self.x -= self.speed

    def draw(self, canvas):
        self.move()
        canvas.delete(self.ID)
        self.ID = canvas.create_image(self.x, self.y, image = self.image)

    def destroy(self, canvas, vehicles):
        if self.x > 1200:
            vehicles.remove(self)
            canvas.delete(self.ID)
            self.draw_more(board, vehicles)
        elif self.x < 0:
            vehicles.remove(self)
            canvas.delete(self.ID) 
            self.draw_more(board, vehicles)
        

    def draw_more(self, canvas, vehicles):
        vehicles.append(Vehicle(canvas, self.row))

    def detect_collision(self, player, board):
        if(len(board.get_canvas().find_overlapping(*board.get_canvas().bbox(player.player))) == 3):
            return True



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
                self.canvas.get_canvas().tag_raise(self.player)
                self.root.update()
        elif direction == "left":
            if(self.x == 5):
                pass
            else:    
                self.x -= 45
                self.canvas.get_canvas().delete(self.player)
                self.player = self.canvas.get_canvas().create_image(self.x, self.y, image = self.canvas.imageData["Player"], anchor = "nw")
                self.canvas.get_canvas().tag_raise(self.player)                
                self.root.update()
        elif direction == "up":
            if(self.y == 50):
                pass
            else:
                self.y -= 60
                self.canvas.get_canvas().delete(self.player)
                self.player = self.canvas.get_canvas().create_image(self.x, self.y, image = self.canvas.imageData["Player"], anchor = "nw")
                self.canvas.get_canvas().tag_raise(self.player)                
                self.root.update()
        elif direction == "down":
            if(self.y == 650):
                pass
            else:
                self.y += 60
                self.canvas.get_canvas().delete(self.player)
                self.player = self.canvas.get_canvas().create_image(self.x, self.y, image = self.canvas.imageData["Player"], anchor = "nw")
                self.canvas.get_canvas().tag_raise(self.player)                
                self.root.update() 

def start(canvas, vehicles):
    for vehicle in vehicles:
        vehicle.draw(canvas)
        vehicle.destroy(canvas, vehicles)
        if(vehicle.detect_collision(user, board)):
            canvas.create_text(500, 300, fill = "red", font = ("Comic Sans", 50), text = "Game Over...")
            canvas.create_text(490, 350, fill = "dark blue", font = ("Times", 20), text = "Restart to play again.")

    canvas.after(20, start, canvas, vehicles)

def beginInit():
    global board
    global user
    board = Canvas(window)
    user = Player(window, board)
    vehicles = [Vehicle(board, i) for i in range(1,7)]
    start(board.get_canvas(), vehicles)

path = os.path.dirname(os.path.abspath(__file__))
window = tk.Tk()
window.title("Frogger")
window.geometry("1000x700")
window.resizable(False, False)
window.update_idletasks()

pygame.mixer.init()
pygame.mixer.music.load(path + "/Sounds/Sunburst.mp3")
pygame.mixer.music.play()

beginInit()

window.mainloop()
