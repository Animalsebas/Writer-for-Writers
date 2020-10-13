import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from io import open
import os
import pygame
def WW():
    def chtheme():
        global themename
        Twindow = tkinter.Tk()
        Twindow.geometry("300x280")
        Twindow.title("Change Theme")
        Twindow.configure(background = "light gray")
        Twindow.resizable(False, False)

        theme = ttk.Combobox(Twindow, 
                            values=[
                                    "White", 
                                    "Black",
                                    "Night",
                                    "Matrix"], state = "readonly")
        theme.current(0)
        theme.pack()
        button_Image = tkinter.Button(Twindow, text = "Change", font = "Arial 20", command = lambda:[themech(), WWwindow.destroy(), Twindow.destroy(), WW()])
        button_Image.configure(width = 12, height = 1)
        button_Image.pack()
        def themech():
            global themename
            themename = theme.get()
        
    def NF():
        global url_file
        text.delete(1.0, "end")
        url_file = "[Untitled]"
        WWwindow.title(str(url_file) + " Writer for Writers")
    def NFE(event):
        global url_file
        text.delete(1.0, "end")
        url_file = "[Untitled]"
        WWwindow.title(str(url_file) + " Writer for Writers")
    def OF():
        global url_file
        url_file = filedialog.askopenfilename(initialdir = ".", filetype = (("Text file", ".txt"),), title = "Open File")

        if url_file != "":
            file = open(url_file, 'r')
            content = file.read()
            text.delete(1.0, "end")
            text.insert('insert', content)
            file.close
            WWwindow.title(str(url_file) + " Writer for Writers")
    def S():
        global url_file
        if url_file != "":
            content = text.get(1.0, "end")
            file = open(url_file, 'w+')
            file.write(content)
            WWwindow.title("[Saved] " + str(url_file) + " Writer for Writers")
        else:
            file = filedialog.asksaveasfile(title = "Save as", mode = 'w', defaultextension = ".txt")
            if file is not None:
                url_file = file.name
                content = text.get(1.0, "end-1c")
                file = open(url_file, 'w+')
                file.write(content)
                WWwindow.title("[Saved] " + str(url_file) + "Writer for Writers")
            else:
                url_file = ""
                WWwindow.title("[Not Saved] " + str(url_file) + "Writer for Writers")
    def SA():
        pass
    def EX(event):
        WWwindow.destroy()
    def select_folder():
        player = tkinter.Tk()
        player.title("Audio Player")
        player.geometry("205x500")
        player.resizable(False, False)
        def dosomething():
            pass
        music = filedialog.askdirectory(parent=player, initialdir=os.getcwd(), title="Select Folder")
        os.chdir(music)
        songlist = os.listdir()
        playlist = tkinter.Listbox(player,highlightcolor="yellow",selectmode = tkinter.SINGLE)
        player.protocol('WM_DELETE_WINDOW', dosomething)
        for item in songlist:
            pos = 0
            playlist.insert(pos, item)
            pos = pos + 1
            pygame.init()
            pygame.mixer.init()
        def Play():
            pygame.mixer.music.load(playlist.get(tkinter.ACTIVE))
            var.set(playlist.get(tkinter.ACTIVE))
            pygame.mixer.music.play() 
        def ExitPlayer():
            pygame.mixer.music.stop()
        def Pause():  
            pygame.mixer.music.pause()
        def UnPause():  
            pygame.mixer.music.unpause()
        button1 = tkinter.Button(player,width=5,height=3, text="PLAY",command=Play)
        button2 = tkinter.Button(player, width=5,height=3, text="STOP", command=ExitPlayer) 
        button3 = tkinter.Button(player, width=5,height=3, text="PAUSE", command=Pause)
        button4 = tkinter.Button(player, width=5,height=3, text="UNPAUSE", command=UnPause)
        button5 = tkinter.Button(player, width=5,height=3, text="SELECT FOLDER", command = lambda: [player.destroy(), ExitPlayer(), select_folder()])
        button6 = tkinter.Button(player, width=5,height=3, text="EXIT", command= lambda: [ExitPlayer(), player.destroy()])
        var = tkinter.StringVar()
        songtitle = tkinter.Label(player,textvariable=var)
        songtitle.pack()
        button1.pack(fill="x")
        button2.pack(fill="x")
        button3.pack(fill="x")
        button4.pack(fill="x")
        button5.pack(fill="x")
        button6.pack(fill="x")
        playlist.pack(fill="both", expand="yes")
        player.mainloop()
    global themename
    if themename == "White":
        WWwindow = tkinter.Tk()
        WWwindow.geometry("800x480")
        WWwindow.title("[Untitled] Writer for Writers")
        WWwindow.configure(background = "white")
        WWwindow.resizable(False, False)
        text = Text(WWwindow)
        text.pack(fill = "both", expand = 1)
        text.config(bd = 0, padx = 6, pady = 5, font = ("Arial", 12))
        bar = Menu(WWwindow)
        file_menu = Menu(bar, tearoff = 0)
        file_menu.add_command(label = "New File", accelerator="Ctrl+N", command = NF)
        file_menu.add_command(label = "Open...", command = OF)
        file_menu.add_command(label = "Save", command = S)
        file_menu.add_command(label = "Exit", accelerator="Ctrl+Q", command = quit)
        bar.add_cascade(menu = file_menu, label = "File")
        music_menu = Menu(bar, tearoff = 0)
        music_menu.add_command(label = "Music Player", command = select_folder)
        bar.add_cascade(menu = music_menu, label = "Music")
        Options_menu = Menu(bar, tearoff = 0)
        Options_menu.add_command(label = "Theme", command = lambda:[chtheme()])
        bar.add_cascade(menu = Options_menu, label = "Options")
        WWwindow.bind_all("<Control-q>", quit)
        WWwindow.bind_all("<Control-n>", NFE)
        WWwindow.config(menu = bar)
        WWwindow.mainloop()
    elif themename == "Black":
        WWwindow = tkinter.Tk()
        WWwindow.geometry("800x480")
        WWwindow.title("[Untitled] Writer for Writers")
        WWwindow.configure(background = "Black")
        WWwindow.resizable(False, False)
        text = Text(WWwindow)
        text.pack(fill = "both", expand = 1)
        text.config(bd = 0, padx = 6, pady = 5, font = ("Arial", 12), bg = "Black", fg = "white", insertbackground='white')
        bar = Menu(WWwindow)
        file_menu = Menu(bar, tearoff = 0)
        file_menu.add_command(label = "New File", accelerator="Ctrl+N", command = NF)
        file_menu.add_command(label = "Open...", command = OF)
        file_menu.add_command(label = "Save", command = S)
        file_menu.add_command(label = "Exit", accelerator="Ctrl+Q", command = quit)
        bar.add_cascade(menu = file_menu, label = "File")
        music_menu = Menu(bar, tearoff = 0)
        music_menu.add_command(label = "Music Player", command = select_folder)
        bar.add_cascade(menu = music_menu, label = "Music")
        Options_menu = Menu(bar, tearoff = 0)
        Options_menu.add_command(label = "Theme", command = lambda:[chtheme()])
        bar.add_cascade(menu = Options_menu, label = "Options")
        WWwindow.bind_all("<Control-q>", quit)
        WWwindow.bind_all("<Control-n>", NFE)
        WWwindow.config(menu = bar)
        WWwindow.mainloop()
    elif themename == "Night":
        WWwindow = tkinter.Tk()
        WWwindow.geometry("800x480")
        WWwindow.title("[Untitled] Writer for Writers")
        WWwindow.configure(background = "white")
        WWwindow.resizable(False, False)
        text = Text(WWwindow)
        text.pack(fill = "both", expand = 1)
        text.config(bd = 0, padx = 6, pady = 5, font = ("Arial", 12), bg = "khaki")
        bar = Menu(WWwindow)
        file_menu = Menu(bar, tearoff = 0)
        file_menu.add_command(label = "New File", accelerator="Ctrl+N", command = NF)
        file_menu.add_command(label = "Open...", command = OF)
        file_menu.add_command(label = "Save", command = S)
        file_menu.add_command(label = "Exit", accelerator="Ctrl+Q", command = quit)
        bar.add_cascade(menu = file_menu, label = "File")
        music_menu = Menu(bar, tearoff = 0)
        music_menu.add_command(label = "Music Player", command = select_folder)
        bar.add_cascade(menu = music_menu, label = "Music")
        Options_menu = Menu(bar, tearoff = 0)
        Options_menu.add_command(label = "Theme", command = lambda:[chtheme()])
        bar.add_cascade(menu = Options_menu, label = "Options")
        WWwindow.bind_all("<Control-q>", quit)
        WWwindow.bind_all("<Control-n>", NFE)
        WWwindow.config(menu = bar)
        WWwindow.mainloop()
    elif themename == "Matrix":
        WWwindow = tkinter.Tk()
        WWwindow.geometry("800x480")
        WWwindow.title("[Untitled] Writer for Writers")
        WWwindow.configure(background = "white")
        WWwindow.resizable(False, False)
        text = Text(WWwindow)
        text.pack(fill = "both", expand = 1)
        text.config(bd = 0, padx = 6, pady = 5, font = ("Arial", 12), bg = "Black", fg = "lime", insertbackground='lime')
        bar = Menu(WWwindow)
        file_menu = Menu(bar, tearoff = 0)
        file_menu.add_command(label = "New File", accelerator="Ctrl+N", command = NF)
        file_menu.add_command(label = "Open...", command = OF)
        file_menu.add_command(label = "Save", command = S)
        file_menu.add_command(label = "Exit", accelerator="Ctrl+Q", command = quit)
        bar.add_cascade(menu = file_menu, label = "File")
        music_menu = Menu(bar, tearoff = 0)
        music_menu.add_command(label = "Music Player", command = select_folder)
        bar.add_cascade(menu = music_menu, label = "Music")
        Options_menu = Menu(bar, tearoff = 0)
        Options_menu.add_command(label = "Theme", command = lambda:[chtheme()])
        bar.add_cascade(menu = Options_menu, label = "Options")
        WWwindow.bind_all("<Control-q>", quit)
        WWwindow.bind_all("<Control-n>", NFE)
        WWwindow.config(menu = bar)
        WWwindow.mainloop()

def CWP():
    window.destroy()
def WWCWP():
    WWwindow.destroy()
def themeget():
    global themename
    themename = theme.get()
url_file = ""
window = tkinter.Tk()
window.geometry("600x480")
window.title("Welcome to WfW!")
window.configure(background = "light gray")
window.resizable(False, False)
program_version = tkinter.Label(window, text = "Version Pre-Alpha", font = "Arial 15")
program_version.pack(side = tkinter.BOTTOM)
title = tkinter.Label(window, text = "Writer for Writers", bg = "gray", font = "Arial 30")
title.pack(fill = tkinter.X)
made_by = tkinter.Label(window, text = "Made by SHC Software on Python", font = "Arial 15")
made_by.pack(side = tkinter.BOTTOM)
button_Image = tkinter.Button(window, text = "Start", font = "Arial 20", command = lambda:[themeget(), CWP(), WW()])
button_Image.configure(width = 12, height = 1)
button_Image.place(x = 200, y = 120)
theme = ttk.Combobox(window, 
                            values=[
                                    "White", 
                                    "Black",
                                    "Night",
                                    "Matrix"], state = "readonly")
theme.current(0)
theme.place(x = 235, y = 80)
window.mainloop()
