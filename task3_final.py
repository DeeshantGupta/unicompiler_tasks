from cgitb import text
from tempfile import TemporaryFile
from typing import List
from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog, messagebox

songs = {}

def play():
    try:
        current_list = songs[Listofsongs.get(ACTIVE)]
        current = current_list[0]
        Listofsongs.selection_set(current_list[1])
        mixer.music.load(f'{current}')
        mixer.music.play()
    except:
        pass

def pause():
    mixer.music.pause()

def next():
    try:
        try:
            next_song = Listofsongs.curselection()[0]
        except:
            next_song = songs[Listofsongs.get(ACTIVE)][1]

        if next_song == len(songs)-1:
            stop()
            return 0
        else:
            next_song = next_song + 1

        try:
            ns = songs[Listofsongs.get(next_song)][0]
        except:
            try:
                ns = songs[Listofsongs.get(0)][0]
            except:
                messagebox.showinfo("","0 songs available in the queue")
                return 0
        mixer.music.load(f'{ns}')
        mixer.music.play()
        Listofsongs.selection_clear(0, END)
        Listofsongs.activate(next_song)
        Listofsongs.selection_set(next_song)
    except:
        pass
    

def previous():
    try:
        try:
            previous_song = Listofsongs.curselection()[0]
        except:
            previous_song = songs[Listofsongs.get(ACTIVE)][1]
        if (previous_song == 0):
            previous_song = 1
        previous_song = previous_song-1
        Listofsongs.selection_set(previous_song)

        try:
            ps = songs[Listofsongs.get(previous_song)][0]
        except:
            try:
                ps = songs[Listofsongs.get(END)][0]
            except:
                messagebox.showinfo("","0 songs available in the queue")
                return 0
        mixer.music.load(f'{ps}')
        mixer.music.play()

        Listofsongs.selection_clear(0, END)
        Listofsongs.activate(previous_song)
        Listofsongs.selection_set(previous_song)
    except:
        pass

def resume():
    try:
        song_pla = songs[Listofsongs.get(ACTIVE)]
        mixer.music.load(song_pla[0])
        mixer.music.play()
        Listofsongs.selection_set(song_pla[1])
    except:
        pass

def stop():
    mixer.music.stop()
    Listofsongs.selection_clear(ACTIVE)

def addsongs():
    song=filedialog.askopenfilenames(initialdir="Music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))

    for i in song:
        e = i.split("/")[-1]
        songs[e] = [i, len(songs)]
        Listofsongs.insert(END, e)

def deletesong():
    try:
        current=Listofsongs.curselection()
        songs.pop(Listofsongs.get(current[0]))
        Listofsongs.delete(current[0])
    except:
        messagebox.showerror("Error", "No song is selected")

root = Tk()
root.title("Media Player")
mixer.init()
Listofsongs = Listbox(root, selectmode= SINGLE, bg="black", fg="green", font=('arial',15),height=12,width=47,selectbackground="gray",selectforeground="black")
Listofsongs.grid(columnspan=9)


defined_font = font.Font(family='Helvetica')

play_but = Button(root, text="Play", width=7, command=play)
play_but['font'] = defined_font
play_but.grid(row=1, column=0)

pause_but = Button(root, text="Pause", width=7, command=pause)
pause_but['font'] = defined_font
pause_but.grid(row=1, column=1)

next_but = Button(root, text="Next", width=7, command=next)
next_but['font'] = defined_font
next_but.grid(row=1, column=2)

previous_but = Button(root, text="Previous", width=7, command=previous)
previous_but['font'] = defined_font
previous_but.grid(row=1, column=3)

Resume_but = Button(root, text="Resume", width=7, command=resume)
Resume_but['font'] = defined_font
Resume_but.grid(row=1, column=4)

stop_but = Button(root, text="Stop", width=7, command=stop)
stop_but['font'] = defined_font
stop_but.grid(row=1, column=5)


nav = Menu(root)
root.config(menu = nav)
add_song_menu=Menu(nav)
nav.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Add songs",command=addsongs)
add_song_menu.add_command(label="Delete song",command=deletesong)


mainloop()