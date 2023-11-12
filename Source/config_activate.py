import tkinter as tk, configparser
config = configparser.ConfigParser()
config.read('config.ini')
win = tk.Tk()
win.title(config.get('WIN', 'title'))
win.iconbitmap(config.get('WIN', 'icon'))
win.geometry(config.get('WIN', 'geometry'))
win.config(bg=config.get('WIN', 'bgcolor'))
win.resizable(width=False, height=False)
glitter = [False, 1, False]