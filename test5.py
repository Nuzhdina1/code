import tkinter
import random
from tkinter import PhotoImage

def prepare_and_start():
    global player

    canvas.delete("all")
    player_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
    player = canvas.create_image((player_pos[0], player_pos[1]), image = player_pic, anchor = 'nw')
    label.config(text = "Найди выход!")
    master.bind('<KeyPress>', key_pressed)

def move_wrap(obj, move_x, move_y):
    xy = canvas.coords(obj)
    print(xy)
    if xy[0] <= 0:
        canvas.move(obj, WIDTH, 0)
    if xy[0] >= WIDTH:
        canvas.move(obj, -WIDTH, 10)
    if xy[0] <= 0:
        canvas.move(obj, HEIGHT, 10)
    if xy[0] >= HEIGHT:
        canvas.move(obj, -HEIGHT, 10)

def key_pressed(event):
    if event.keysym == 'Up':
        canvas.move(player, 0, -20)
    elif event.keysym == 'Down':
        canvas.move(player, 0, 20)
    elif event.keysym == 'Right':
        canvas.move(player, 20, 0,)
    elif event.keysym == 'Left':
        canvas.move(player, -20, 0)

master = tkinter.Tk()

step = 32
N_X = 10
N_Y = 10
WIDTH = step * N_X
HEIGHT = step * N_Y
a = False
player_pic = tkinter.PhotoImage(file = r".\pixil-frame-0.png")

canvas = tkinter.Canvas(master, bg = "white", width = WIDTH, height = HEIGHT)

player_pos = (random.randint(0, N_X - 1) * step, random.randint(0, N_Y - 1) * step)
print(player_pos)
label = tkinter.Label(master, text = "Не попадись!")
restart = tkinter.Button(master, text = "Начать заново", command = prepare_and_start)
restart.pack()
label.pack()
canvas.pack()
prepare_and_start()
master.bind("<KeyPress>", key_pressed)
master.mainloop()
