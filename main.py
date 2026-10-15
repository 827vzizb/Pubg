# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

Window.clearcolor = (0.1, 0.12, 0.18, 1)
if Window.width > 600:
    Window.size = (420, 780)


class TicTacToeApp(App):
    def build(self):
        self.title = "Sahi Game - Tic Tac Toe"
        self.current_player = "X"
        self.board = [""] * 9
        self.game_active = True

        root = BoxLayout(orientation='vertical', padding=15, spacing=15)

        header = Label(text="[b]TIC TAC TOE[/b]", markup=True,
                       font_size='26sp', size_hint_y=None, height='60dp',
                       color=(0.9, 0.95, 1, 1))
        root.add_widget(header)

        self.status_lbl = Label(text="Player X's Turn", font_size='18sp',
                                size_hint_y=None, height='40dp',
                                color=(0.7, 0.8, 1, 1))
        root.add_widget(self.status_lbl)

        grid = GridLayout(cols=3, spacing=8)
        self.buttons = []
        for i in range(9):
            btn = Button(text="", font_size='40sp',
                         background_color=(0.2, 0.25, 0.35, 1),
                         background_normal='')
            btn.bind(on_release=lambda inst, idx=i: self.on_cell_pressed(idx))
            self.buttons.append(btn)
            grid.add_widget(btn)
        root.add_widget(grid)

        reset_btn = Button(text="Restart Game", size_hint_y=None,
                           height='50dp', font_size='16sp',
                           background_color=(0.2, 0.6, 0.8, 1))
        reset_btn.bind(on_release=self.reset_game)
        root.add_widget(reset_btn)

        return root

    def on_cell_pressed(self, index):
        if not self.game_active or self.board[index] != "":
            return
        self.board[index] = self.current_player
        self.buttons[index].text = self.current_player
        if self.current_player == "X":
            self.buttons[index].color = (0.2, 0.7, 1, 1)
        else:
            self.buttons[index].color = (1, 0.4, 0.4, 1)

        if self.check_winner(self.current_player):
            self.status_lbl.text = "Player %s Wins!" % self.current_player
            self.game_active = False
            return
        if "" not in self.board:
            self.status_lbl.text = "It's a Draw!"
            self.game_active = False
            return

        self.current_player = "O" if self.current_player == "X" else "X"
        self.status_lbl.text = "Player %s's Turn" % self.current_player

    def check_winner(self, player):
        wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6)]
        return any(self.board[a] == player and self.board[b] == player
                   and self.board[c] == player for a, b, c in wins)

    def reset_game(self, instance):
        self.board = [""] * 9
        self.game_active = True
        self.current_player = "X"
        self.status_lbl.text = "Player X's Turn"
        for btn in self.buttons:
            btn.text = ""


if __name__ == '__main__':
    TicTacToeApp().run()
