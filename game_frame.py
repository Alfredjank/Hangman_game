import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import random
from playsound import playsound
from beggining_frame import BeginningFrame

class GameFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.wrong_guessed = 1
        self.guessing_word = ''
        self.button_dict = {}

        labels1_style = ttk.Style()
        labels1_style.configure('guessing.TLabel', background='black', foreground='white', font=('Comic Sans MS', 20))

        labels2_style = ttk.Style()
        labels2_style.configure('game_over.TLabel', background='black', foreground='#5B9A8B', font=('Comic Sans MS', 17))

        labels3_style = ttk.Style()
        labels3_style.configure('game_status.TLabel', background='black', foreground='#FFDBC3', font=('Comic Sans MS', 23))

        over_style = ttk.Style()
        over_style.configure('game_over.TFrame', background='black', bordercolor='#FFDD93', borderwight=5, relief='groove')

        self.background = PhotoImage(file='pictures/hangman_0.png')
        img_label = ttk.Label(self, image=self.background)
        img_label.grid(row=0, column=0, columnspan=3, rowspan=4)

        round_frame = ttk.Frame(self, style='frame.TFrame')
        round_frame.grid(row=1, column=2)

        round_nr = tk.StringVar()
        self.round_value = 1
        round_nr.set(f'Round:\n{self.round_value}/5')
        round_label = tk.Label(round_frame, textvariable=round_nr)
        round_label.grid(row=0, column=0)

        points = tk.StringVar()
        self.points_value = 0
        points.set(f'Points:\n{self.points_value}')
        points_label = tk.Label(round_frame, textvariable=points)
        points_label.grid(row=1, column=0)

        quit_button = tk.Button(self, text='Quit Game', command=lambda a=BeginningFrame: container.show_frame(a))
        quit_button.configure(font=('Comic Sans MS', 13), background='#393E46', foreground='#5B9A8B')
        quit_button.grid(row=2, column=2, sticky='N')

        for label in round_frame.winfo_children():
            label.configure(font=('Comic Sans MS', 15), background='black', foreground='#5B9A8B')

        button_frame1 = ttk.Frame(self, style='frame.TFrame')
        button_frame2 = ttk.Frame(self, style='frame.TFrame')
        button_frame3 = ttk.Frame(self, style='frame.TFrame')

        button_frame1.grid(row=0, column=0, sticky='NE', pady=5)
        button_frame2.grid(row=0, column=1, sticky='N', pady=5)
        button_frame3.grid(row=0, column=2, sticky='NW', pady=5)

        a = tk.Button(button_frame1, text='A', command=lambda a='A': guessing(a))
        b = tk.Button(button_frame1, text='B', command=lambda a='B': guessing(a))
        c = tk.Button(button_frame1, text='C', command=lambda a='C': guessing(a))
        d = tk.Button(button_frame1, text='D', command=lambda a='D': guessing(a))
        e = tk.Button(button_frame1, text='E', command=lambda a='E': guessing(a))
        f = tk.Button(button_frame1, text='F', command=lambda a='F': guessing(a))
        g = tk.Button(button_frame1, text='G', command=lambda a='G': guessing(a))
        h = tk.Button(button_frame1, text='H', command=lambda a='H': guessing(a))
        i = tk.Button(button_frame1, text='I', command=lambda a='I': guessing(a))
        j = tk.Button(button_frame2, text='J', command=lambda a='J': guessing(a))
        k = tk.Button(button_frame2, text='K', command=lambda a='K': guessing(a))
        l = tk.Button(button_frame2, text='L', command=lambda a='L': guessing(a))
        m = tk.Button(button_frame2, text='M', command=lambda a='M': guessing(a))
        n = tk.Button(button_frame2, text='N', command=lambda a='N': guessing(a))
        o = tk.Button(button_frame2, text='O', command=lambda a='O': guessing(a))
        p = tk.Button(button_frame2, text='P', command=lambda a='P': guessing(a))
        q = tk.Button(button_frame2, text='Q', command=lambda a='Q': guessing(a))
        r = tk.Button(button_frame3, text='R', command=lambda a='R': guessing(a))
        s = tk.Button(button_frame3, text='S', command=lambda a='S': guessing(a))
        t = tk.Button(button_frame3, text='T', command=lambda a='T': guessing(a))
        u = tk.Button(button_frame3, text='U', command=lambda a='U': guessing(a))
        v = tk.Button(button_frame3, text='V', command=lambda a='V': guessing(a))
        w = tk.Button(button_frame3, text='W', command=lambda a='W': guessing(a))
        x = tk.Button(button_frame3, text='X', command=lambda a='X': guessing(a))
        y = tk.Button(button_frame3, text='Y', command=lambda a='Y': guessing(a))
        z = tk.Button(button_frame3, text='Z', command=lambda a='Z': guessing(a))

        self.button_dict['A'] = a
        self.button_dict['B'] = b
        self.button_dict['C'] = c
        self.button_dict['D'] = d
        self.button_dict['E'] = e
        self.button_dict['F'] = f
        self.button_dict['G'] = g
        self.button_dict['H'] = h
        self.button_dict['I'] = i
        self.button_dict['J'] = j
        self.button_dict['K'] = k
        self.button_dict['L'] = l
        self.button_dict['M'] = m
        self.button_dict['N'] = n
        self.button_dict['O'] = o
        self.button_dict['P'] = p
        self.button_dict['Q'] = q
        self.button_dict['R'] = r
        self.button_dict['S'] = s
        self.button_dict['T'] = t
        self.button_dict['U'] = u
        self.button_dict['V'] = v
        self.button_dict['W'] = w
        self.button_dict['X'] = x
        self.button_dict['Y'] = y
        self.button_dict['Z'] = z

        for child in button_frame1.winfo_children():
            child.configure(font=('Comic Sans MS', 13), background='#393E46', foreground='#FFDD93')

        for child in button_frame2.winfo_children():
            child.configure(font=('Comic Sans MS', 13), background='#393E46', foreground='#FFDD93')

        for child in button_frame3.winfo_children():
            child.configure(font=('Comic Sans MS', 13), background='#393E46', foreground='#FFDD93')

        a.grid(row=0, column=0, padx=5)
        b.grid(row=0, column=1, padx=5)
        c.grid(row=0, column=2, padx=5)
        d.grid(row=0, column=3, padx=5)
        e.grid(row=0, column=4, padx=5)
        f.grid(row=1, column=1, padx=5, pady=3)
        g.grid(row=1, column=2, padx=5, pady=3)
        h.grid(row=1, column=3, padx=5, pady=3)
        i.grid(row=1, column=4, padx=5, pady=3)
        j.grid(row=0, column=0, padx=5)
        k.grid(row=0, column=1, padx=5)
        l.grid(row=0, column=2, padx=5)
        m.grid(row=0, column=3, padx=5)
        n.grid(row=1, column=0, padx=5, pady=3)
        o.grid(row=1, column=1, padx=5, pady=3)
        p.grid(row=1, column=2, padx=5, pady=3)
        q.grid(row=1, column=3, padx=5, pady=3)
        r.grid(row=0, column=0, padx=5)
        s.grid(row=0, column=1, padx=5)
        t.grid(row=0, column=2, padx=5)
        u.grid(row=0, column=3, padx=5)
        v.grid(row=0, column=4, padx=5)
        w.grid(row=1, column=0, padx=5, pady=3)
        x.grid(row=1, column=1, padx=5, pady=3)
        y.grid(row=1, column=2, padx=5, pady=3)
        z.grid(row=1, column=3, padx=5, pady=3)

        guessing_word_frame = ttk.Frame(self, style='frame.TFrame')
        guessing_word_frame.grid(row=3, column=0, columnspan=3)

        self.underscore = PhotoImage(file='pictures/underscore.png')
        self.user_name = tk.StringVar()

        def setting_word():
            dict = container.category
            length = len(dict[self.round_value])
            rand_number = random.randrange(0, length)
            self.word = dict[self.round_value][rand_number].upper()
            self.guessed_word = []
            for letter in range(len(self.word)):
                label = ttk.Label(guessing_word_frame, style='guessing.TLabel', image=self.underscore)
                label.configure(compound='bottom')
                label.grid(row=0, column=letter)
                self.guessed_word.append('')

        setting_word()

        def guessing(letter_g):
            button_disable(letter_g)
            index = 0
            guessed = False
            # print(self.word, ' -- word you need to guess') # --for checking is everything works
            for letter in list(self.word):
                if letter == letter_g:
                    playsound('sounds/correct_sound.mp3', False)
                    label = ttk.Label(guessing_word_frame, style='guessing.TLabel', image=self.underscore,
                                      compound='bottom', text=letter_g)
                    label.grid(row=0, column=index)
                    guessed = True
                    self.guessed_word[index] = letter_g
                    set_points('correct')
                    check_answer(self.guessed_word)
                index += 1

            if guessed == False and self.wrong_guessed < 11:
                playsound('sounds/wrong_sound.mp3', False)
                img2 = PhotoImage(file=f'pictures/hangman_{self.wrong_guessed}.png')
                img_label.configure(image=img2)
                img_label.image = img2
                self.wrong_guessed += 1
                set_points('wrong')

            if self.wrong_guessed == 11:
                game_over()

        def check_answer(list_word):
            self.guessing_word = ''.join(list_word)
            if self.guessing_word == self.word:
                self.round_value += 1
                if self.round_value <= 5:
                    round_nr.set(f'Round\n{self.round_value}/5')
                    next_round()
                elif self.round_value > 5:
                    game_over()

        def set_points(guess):
            if guess == 'correct':
                self.points_value += 100
                points.set(f'Points:\n{self.points_value}')
            elif guess == 'wrong':
                self.points_value -= 20
                points.set(f'Points:\n{self.points_value}')

        def next_round():
            img2 = PhotoImage(file='pictures/hangman_0.png')
            img_label.configure(image=img2)
            img_label.image = img2
            button_active()
            delete_labels()
            # setting parameters to initial values
            self.guessed_word = []
            self.wrong_guessed = 1

            setting_word()

        def button_disable(letter):
            button = self.button_dict[letter]
            button['state'] = tk.DISABLED

        def all_buttons_disable():
            for key, values in self.button_dict.items():
                button = self.button_dict[key]
                button['state'] = tk.DISABLED

        def button_active():
            for key, values in self.button_dict.items():
                button = self.button_dict[key]
                button['state'] = tk.NORMAL

        def delete_labels():
            for label in guessing_word_frame.winfo_children():
                label.destroy()

        def game_over():
            game_status = tk.StringVar()
            all_buttons_disable()
            quit_button['state'] = tk.DISABLED

            game_over_frame = ttk.Frame(self, style='game_over.TFrame')
            game_over_frame.grid(row=1, column=0, rowspan=2, columnspan=3)

            label_game_status = tk.Label(game_over_frame, textvariable=game_status)
            label_game_status.configure(background='black', foreground='#FFDBC3', font=('Comic Sans MS', 23))

            label = ttk.Label(game_over_frame, style='game_over.TLabel', text='Enter name: ')
            entry_name = tk.Entry(game_over_frame, width=10, textvariable=self.user_name)
            entry_name.configure(background='#393E46', foreground='#5B9A8B', font=('Comic Sans MS', 15))

            save_button = tk.Button(game_over_frame, text='Enter', command=get_name)
            save_button.configure(background='#393E46', foreground='#5B9A8B', font=('Comic Sans MS', 13))

            label_game_status.grid(row=0, column=0, columnspan=3, pady=10)
            label.grid(row=1, column=0, padx=5)
            entry_name.grid(row=1, column=1, padx=5)
            save_button.grid(row=2, column=1, pady=3, padx=7, sticky='WE')

            entry_name.focus()

            if self.round_value == 6 and self.guessing_word == self.word:
                game_status.set('You Win!')
            else:
                game_status.set('Game Over')

        def get_name():
            user_name = self.user_name.get()
            container.score(user_name, self.points_value)   # opening ScoreFrame and passing user_name and score
