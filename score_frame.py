import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import datetime
import pickle
from beggining_frame import BeginningFrame



class ScoreFrame(ttk.Frame):
    def __init__(self, container, name, score):
        super().__init__(container)

        self.name = name
        self.score = score
        self.category_name = container.category_name
        self.current_date = str(datetime.date.today())
        self.score_table = {}
        self.indexes = []

        score_style = ttk.Style()
        score_style.configure('score.TLabel', background='black', foreground='white', font=('Comic Sans MS', 17, 'bold'))

        data_style = ttk.Style()
        data_style.configure('data.TLabel', background='black', foreground='white', font=('Comic Sans MS', 13))

        self.background = PhotoImage(file='pictures/hangman_0.png')
        img_label = ttk.Label(self, image=self.background)
        img_label.grid(row=0, column=0, columnspan=5, rowspan=11)

        label_head = ttk.Label(self, text='Score Table')
        label_head.configure(background='black', foreground='white', font=('Comic Sans MS', 25, 'bold'))
        label_head.grid(row=0, column=0, columnspan=5)

        label_1 = ttk.Label(self, text='Name', style='score.TLabel')
        label_2 = ttk.Label(self, text='Category', style='score.TLabel')
        label_3 = ttk.Label(self, text='Score', style='score.TLabel')
        label_4 = ttk.Label(self, text='Date', style='score.TLabel')

        label_1.grid(row=1, column=1)
        label_2.grid(row=1, column=2)
        label_3.grid(row=1, column=3)
        label_4.grid(row=1, column=4)

        self.index = tk.StringVar()
        self.index_value = 1
        self.index.set(f'{self.index_value}')
        self.row_id = 2


        try:
            with open('files/score_table.pkl', 'rb') as file:
                self.score_table = pickle.load(file)
        except FileNotFoundError:
            pass

        keys_number = len(self.score_table.keys())
        self.score_table[keys_number + 1] = [self.name, self.category_name, self.score, self.current_date]

        with open('files/score_table.pkl', 'wb') as file:
            pickle.dump(self.score_table, file)

        values = list(self.score_table.values())
        points = []
        for data in values:
            points.append(data[2])    #data[2] is self.score in list score_table
        ordered_list = sorted(points, reverse=True)
        for number in ordered_list:
            index = points.index(number)
            self.indexes.append(index)
            points[index] = ''

        back_button = tk.Button(self, text='BACK', command=lambda a=BeginningFrame: container.show_frame(a))
        back_button.configure(font=('Comic Sans MS', 13), background='#393E46', foreground='#FFDD93')
        back_button.grid(row=10, column=0, columnspan=5, ipadx=10)
        self.write_data()

    def write_data(self):
        id_nr = 1
        for index in self.indexes:
            if id_nr <= 8:
                name = self.score_table[index+1][0]
                category = self.score_table[index + 1][1]
                score = self.score_table[index + 1][2]
                date = self.score_table[index + 1][3]
                print(f'{name}, {category}, {score}, {date}' )

                label_id = ttk.Label(self, text=id_nr, style='data.TLabel')
                label_name = ttk.Label(self, text=name, style='data.TLabel')
                label_category = ttk.Label(self, text=category, style='data.TLabel')
                label_score = ttk.Label(self, text=score, style='data.TLabel')
                label_date = ttk.Label(self, text=date, style='data.TLabel')

                label_id.grid(row=self.row_id, column=0, sticky='E', padx=5)
                label_name.grid(row=self.row_id, column=1)
                label_category.grid(row=self.row_id, column=2)
                label_score.grid(row=self.row_id, column=3)
                label_date.grid(row=self.row_id, column=4)

                self.row_id += 1
                id_nr += 1