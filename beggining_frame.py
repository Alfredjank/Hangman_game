import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage


class BeginningFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        label_style = ttk.Style()
        label_style.configure('label.TLabel', background='black', foreground='white')

        button_style = ttk.Style()
        button_style.configure('buttons.TButton', background='black')

        frame_style = ttk.Style()
        frame_style.configure('frameB.TFrame', background='black')

        self.background = PhotoImage(file='pictures/hangman.png')
        img_label = ttk.Label(self, image=self.background, borderwidth=0, relief='raised')
        img_label.grid(row=0, column=0, columnspan=3, rowspan=3)

        label = ttk.Label(self, text='HANGMAN', style='label.TLabel')
        label.config(font=('Comic Sans MS', 35))
        label.grid(row=0, column=1, sticky='E')

        button_frame = ttk.Frame(self, style='frameB.TFrame')
        button_frame.grid(row=1, column=1, sticky='NE')

        button1 = tk.Button(button_frame, text='START', command=container.show_categories)
        button2 = tk.Button(button_frame, text='EXIT', command=container.destroy)

        button1.grid(row=0, column=0, ipady=10, ipadx=10, sticky='WE', pady=5)
        button2.grid(row=1, column=0, ipady=10, ipadx=10, sticky='WE')

        for button in button_frame.winfo_children():
            button.configure(font=('Comic Sans MS', 15), background='#393E46', foreground='#FFDD93')