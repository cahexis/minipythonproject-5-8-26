import tkinter as tk
from PIL import Image, ImageTk


base = tk.Tk()
base.title("Motivational Robin")
base.geometry("300x200")


img = Image.open("C:/Users/#####/####/#####/python_projs/giggles.png") 
sizerimg = img.resize((200,200))
img2 = ImageTk.PhotoImage(sizerimg)


my_label = tk.Label(base, image=img2)
my_label.pack(pady=6)

base.mainloop()
