import tkinter as tk
import turtle

root = tk.Tk()

# Setups the window

root.title('Yoru Gatecrash Lineup Generator')

window_width = 1000
window_height = 700

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.resizable(False, False)

root.mainloop()
