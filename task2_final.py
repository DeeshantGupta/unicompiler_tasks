import tkinter as tk
from tkinter import StringVar, messagebox, filedialog
from unittest import result
from pytube import YouTube
from typing import Text

windows = tk.Tk()
Dp = StringVar()



canvas = tk.Canvas(windows, width=400, height=400, bg="black")
canvas.pack()

label0 = tk.Label(windows, text="YouTube Video Downloader", fg="red",font="SegoeUI 14", padx=5, pady=5)
canvas.create_window(200, 50, window=label0)


label1 = tk.Label(windows, text="Link: ", font="SegoeUI 10")
canvas.create_window(70, 150, window=label1)

entry1 = tk.Entry(windows, width=30)
canvas.create_window(220, 150, window=entry1)

label2 = tk.Label(windows, text="Path: ", font="SegoeUI 10")
canvas.create_window(70, 200, window=label2)
entry2 = tk.Entry(windows, width=30, textvariable=Dp)
canvas.create_window(220, 200, window=entry2)

def browse():
    download_Directory = filedialog.askdirectory(
		initialdir="YOUR DIRECTORY PATH", title="Save Video")
    Dp.set(download_Directory)


browse_button = tk.Button(text="Browse", command=browse, font="SegoeUI 10")
canvas.create_window(350, 200, window=browse_button)







def download():
    link1 = entry1.get()
    path = entry2.get()
    try:
        yt = YouTube('{}'.format(link1))
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(path)
        result= "Download Complete"
        messagebox.showinfo("SUCCESSFULLY","DOWNLOADED AND SAVED IN\n"+ path)
    except:
        messagebox.showinfo("Error", "Not able to download.")

button1 = tk.Button(text="Download", command=download, font="SegoeUI 10", padx=10)
canvas.create_window(190, 270, window=button1)

windows.mainloop()