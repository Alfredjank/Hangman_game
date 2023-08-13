import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage


class CategoryFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        frame_style = ttk.Style()
        frame_style.configure('frame.TFrame', background='black')

        self.background = PhotoImage(file='pictures/hangman_0.png')
        img_label = ttk.Label(self, image=self.background)
        img_label.grid(row=0, column=0, columnspan=3, rowspan=3)

        label = ttk.Label(self, text='Choose category', style='label.TLabel')
        label.config(font=('Comic Sans MS', 30))
        label.grid(row=0, column=1)

        button_frame = ttk.Frame(self, style='frame.TFrame')
        button_frame.grid(row=1, column=1, sticky='WE')

        self.countries_image = PhotoImage(file='pictures/countries.png')
        self.food_image = PhotoImage(file='pictures/food.png')
        self.building_image = PhotoImage(file='pictures/building.png')

        button1 = tk.Button(button_frame, text='Countries', image=self.countries_image, compound='top')
        button1.configure(command=container.start_game_countries)
        button1.grid(row=0, column=0)

        button2 = tk.Button(button_frame, text='Food', image=self.food_image, compound='top')
        button2.configure(command=container.start_game_food)
        button2.grid(row=0, column=1)

        button3 = tk.Button(button_frame, text='Buildings', image=self.building_image, compound='top')
        button3.configure(command=container.start_game_buildings)
        button3.grid(row=0, column=2)

        for button in button_frame.winfo_children():
            button.configure(font=('Comic Sans MS', 13), background='#393E46', foreground='#FFDD93')

        button_frame.columnconfigure(1, weight=1)
