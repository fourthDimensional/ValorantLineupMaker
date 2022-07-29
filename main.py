import tkinter as tk
import turtle

root = tk.Tk()

consoleList = ['Welcome to the Valorant Lineup Maker, a tool to help you make your own lineups for Valorant.', 'Errors/Info will show up here']
consoleVar = tk.StringVar(value=consoleList)

### Setups the window

root.title('Valorant Lineup Generator')

window_width = 1100
window_height = 700

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.resizable(False, False)

root.iconbitmap('./assets/Gatecrash.ico')

### Initializes the frames & widgets

mapFrame = tk.Frame(root, width=window_width*0.6, height=window_width*0.6, bg = '#cccccc')
mapFrame.pack(side='left', padx=(20,20), pady=(20,20))

settingsFrame = tk.Frame(root, width=window_width*0.4, height=window_height*0.4, bg = '#cccccc')
settingsFrame.pack(side='top', padx=(20,20), pady=(20,20))

consoleFrame = tk.Frame(root, width=window_width*0.4, height=window_height*0.6, bg = '#cccccc')
consoleFrame.pack(side='bottom', padx=(20,20), pady=(20,20))

# Creates the Console

consoleWidget = tk.Listbox(consoleFrame, listvariable=consoleList, width=440, height=420,)
consoleWidget.pack(padx=(20,20), pady=(20,20))

def items_selected(event):

    selected_indices = listbox.curselection()
    # get selected items
    selected_langs = ",".join([listbox.get(i) for i in selected_indices])
    msg = f'You selected: {selected_langs}'

    showinfo(
        title='Information',
        message=msg)


listbox.bind('<<ListboxSelect>>', items_selected)

root.mainloop()
