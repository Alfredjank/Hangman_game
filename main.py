import tkinter as tk
from files import words
from beggining_frame import BeginningFrame
from category_frame import CategoryFrame
from game_frame import GameFrame
from score_frame import ScoreFrame


class Start(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('800x536')
        self.resizable(False, False)
        self.title('Hangman')

        self.category = {}
        self.frame_dict = {}

        frame = BeginningFrame(self)
        self.frame_dict[BeginningFrame] = frame
        frame.grid(row=0, column=0)

        frame_game = CategoryFrame(self)
        self.frame_dict[CategoryFrame] = frame_game
        frame_game.grid(row=0, column=0)

        self.show_frame(BeginningFrame)

    def show_categories(self):
        self.show_frame(CategoryFrame)

    def start_game_countries(self):
        self.category = words.countries
        self.category_name = 'Countries'
        frame_game = GameFrame(self)
        self.frame_dict[GameFrame] = frame_game
        frame_game.grid(row=0, column=0)
        self.show_frame(GameFrame)

    def start_game_food(self):
        self.category = words.food
        self.category_name = 'Food'
        frame_game = GameFrame(self)
        self.frame_dict[GameFrame] = frame_game
        frame_game.grid(row=0, column=0)
        self.show_frame(GameFrame)

    def start_game_buildings(self):
        self.category = words.buildings
        self.category_name = 'Buildings'
        frame_game = GameFrame(self)
        self.frame_dict[GameFrame] = frame_game
        frame_game.grid(row=0, column=0)
        self.show_frame(GameFrame)

    def score(self, name, score):
        frame_score = ScoreFrame(self, name, score)
        self.frame_dict[ScoreFrame] = frame_score
        frame_score.grid(row=0, column=0)
        self.show_frame(ScoreFrame)

    def show_frame(self, name):
        frame = self.frame_dict[name]
        frame.tkraise()


root = Start()
root.iconbitmap(r'pictures/hangman_icon.ico')
root.mainloop()
