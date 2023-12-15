from tkinter import StringVar, TOP
from tkinterdnd2 import TkinterDnD, DND_ALL
import customtkinter as ctk
import serial
from PIL import Image
import io
import os

class Tk(ctk.CTk, TkinterDnD.DnDWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
global path
path=r"path"
# get path of desktop
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

try:
    ser = serial.Serial('COM3', 300)
except:
    print("No device connected")
def get_path(event):
    global path
    pathLabel.configure(text = event.data)
    path = event.data
#root = TkinterDnD.Tk()
root = Tk()
root.geometry("500x600")
root.title("Li-Fi File Transfer")

nameVar = StringVar()
def clear():
    global path
    path=r""
    pathLabel.configure(text = path)
    status("Select a file")
def status(status):
    statusLabel.configure(text = status)
def image_send():
    print("Sending image")
    status("Sending image")
    with open(path, "rb") as image_file:
        image_data = image_file.read()
    chunk_size = 64
    for i in range(0, len(image_data), chunk_size):
        chunk = image_data[i:i + chunk_size]
        ser.write(chunk)
    ser.write(b'E')
    ser.close()
def image_recive():
    print("reciving image")
    status("reciving image")
    binary_data = ser.read()
    # Create an image from the binary data
    image = Image.open(io.BytesIO(binary_data))
    # save image to desktop
    image.save(desktop + "\Recived_image.jpeg")
    image.show()
def TextOrMusic_send():
    print("Sending Text or Music")
    status("Sending Text or Music")
    with open(path, "rb") as music:
        binary=music.read()
    ser.write(binary)
def TextOrMusic_recive():
    print("reciving Text or Music")
    status("reciving Text or Music")
    with open(desktop, "wb") as music_file:
        binary = ser.read()
        music_file.write(binary)
    # save music to desktop
    music_file.save(desktop + "\recived_music.mp3")
    print("done")
entryWidget = ctk.CTkEntry(root,height=300, width=300,border_color="blue",placeholder_text=" "*30 + "Drag a file here")
entryWidget.pack(side=TOP, padx=5, pady=5)

pathLabel = ctk.CTkLabel(root, text="Drag and drop file in the entry box")
pathLabel.pack(side=TOP)

entryWidget.drop_target_register(DND_ALL)
entryWidget.dnd_bind("<<Drop>>", get_path)
# get path from entry widget
path = entryWidget.get()
print(path)
# add button named send,recive
sendButton = ctk.CTkButton(root, text="Send", command=image_send)
sendButton.pack(side=TOP, padx=5, pady=5,ipadx=10, ipady=10,)

reciveButton = ctk.CTkButton(root, text="Recive", command=image_recive)
reciveButton.pack(side=TOP, padx=5, pady=5,ipadx=20, ipady=10,)

# add button named done
doneButton = ctk.CTkButton(root, text="Done", command=lambda: print("Done"))
doneButton.pack(side=TOP, padx=5, pady=5,ipadx=30, ipady=10,)

# add button named clear
clearButton = ctk.CTkButton(root, text="Clear", command=clear)
clearButton.pack(side=TOP, padx=5, pady=5,ipadx=40, ipady=10,)
# add a status lable at bottom of window
statusLabel = ctk.CTkLabel(root, text="Status: select a file")
statusLabel.pack(side=TOP, padx=5, pady=5,ipadx=50, ipady=10,)

root.mainloop()