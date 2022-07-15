import tkinter as tk
import spintax
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile, asksaveasfile, askopenfilename

root = tk.Tk()

input_text = "{This is Spintext|This Text is Spintext} {Write spintext here|Write or upload spintext}."

spin_text = "Spun text goes here"

root.configure(bg = "#000000", highlightbackground = "#000000")

canvas = tk.Canvas(root, width = 10, height = 10, bg = "#000000", highlightbackground = "#000000")
canvas.grid(columnspan = 2, rowspan = 10)

#logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image = logo)
logo_label.image = logo
logo_label.configure(bg = "#000000", highlightbackground = "#000000")
logo_label.grid(column = 0, row = 0)

#open file
def open_file():
    browse_text.set("Loading...")
    filename = askopenfilename()
    if filename:
        print(filename)
        with open(filename, 'r') as file:
            data = file.read().replace('\n',' ')
            text_box.delete('1.0', tk.END)
            text_box.insert(1.0, data)


#spin text
def spin_txt_input():
    input_text = text_box.get(1.0,tk.END)
    spin_btn_text.set("Spinning...")
    spin_text = spintax.spin("{"+input_text+"}")
    text_box2.delete('1.0', tk.END)
    text_box2.insert(1.0, spin_text)
    spin_btn_text.set("Spin")

#loop
def loop_spin():
    loop = 0
    input_text = text_box.get(1.0,tk.END)
    loop_btn_text.set("Spinning...")
    while(loop < 1000):
        spin_text = spintax.spin("{"+input_text+"}")
        text_box2.insert(1.0, spin_text+"\n")
        loop += 1
    loop_btn_text.set("Loop 1000")

#save text
def save_txt():
    save_btn_text.set("Saving...")
    save_dir = asksaveasfile(mode='w', defaultextension=".txt")
    if save_dir is None:
        return
    text2save = str(text_box2.get(1.0,tk.END))
    save_dir.write(text2save)
    save_dir.close()
    save_btn_text.set("Save")

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable = browse_text, command = lambda:open_file())
browse_btn.configure(bg = "#f86c4d", highlightbackground = "#f86c4d", font = "ubuntu", fg = "white", height = 4, width = 30)
browse_text.set("Browse")
browse_btn.grid(column = 0, row = 1)

#spin button
spin_btn_text = tk.StringVar()
spin_btn = tk.Button(root, textvariable = spin_btn_text, command = lambda:spin_txt_input())
spin_btn_text.set("Spin")
spin_btn.configure(bg = "#f86c4d", highlightbackground = "#f86c4d", font = "ubuntu", fg = "white", height = 4, width = 30)
spin_btn.grid(column = 0, row = 2)

#loop button
loop_btn_text = tk.StringVar()
loop_btn = tk.Button(root, textvariable = loop_btn_text, command = lambda:loop_spin())
loop_btn.configure(bg = "#f86c4d", highlightbackground = "#f86c4d", font = "ubuntu", fg = "white", height = 4, width = 30)
loop_btn_text.set("Loop")
loop_btn.grid(column = 0, row = 3)

#save button
save_btn_text = tk.StringVar()
save_btn = tk.Button(root, textvariable = save_btn_text, command = lambda:save_txt())
save_btn.configure(bg = "#f86c4d", highlightbackground = "#f86c4d", font = "ubuntu", fg = "white", height = 4, width = 30)
save_btn_text.set("Save")
save_btn.grid(column = 0, row = 4)

#text boxes
text_box = tk.Text(root, height = 10, width = 100, padx = 15, pady = 15, font = "ubuntu", highlightbackground = "#000000", fg = "white")
text_box.insert(1.0, input_text)
text_box.configure(bg = "#000000", highlightbackground = "#000000")
text_box.grid(column = 1, row = 0)

text_box2 = tk.Text(root, height = 10, width = 100, padx = 15, pady = 15, font = "ubuntu", highlightbackground = "#000000", fg = "white")
text_box2.configure(bg = "#000000", highlightbackground = "#000000")
text_box2.grid(column = 1, row = 1)

root.mainloop()