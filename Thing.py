from tkinter import *
import random

def random_char():
    return str(random.randint(0, 1))

def random_color():
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 0), random.randint(0, 0))

def update_lines():
    global lines, bg_color
    lines.pop()
    new_line = ''.join(random_char() for _ in range(line_length))
    lines.insert(0, new_line)
    label.config(text='\n'.join(lines))
    bg_color = 'red' if bg_color == 'black' else 'black'
    label.config(bg=bg_color)
    label.config(fg=random_color())
    label.after(50, update_lines)

window = Tk()
window.geometry("680x680")
window.title("Test")
icon = PhotoImage(file='PYicon.png')
window.iconphoto(True,icon)
bg_color = '#000000'
window.config(background=bg_color)
window.configure(bg='black')
window.attributes('-fullscreen', True)
num_lines = 100
line_length = 2000
lines = [''.join(random_char() for _ in range(line_length)) for _ in range(num_lines)]
bg_color = 'red'
label = Label(window, text='\n'.join(lines), font=('Courier', 12), fg='red', bg='red')
label.pack(expand=True, fill='both')
update_lines()
fg_color = '#00FF00'
window.mainloop()