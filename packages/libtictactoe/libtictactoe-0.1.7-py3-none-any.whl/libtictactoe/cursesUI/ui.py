import curses

from libtictactoe.cursesUI import constants as const
from libtictactoe.cursesUI.base import TextUI
from libtictactoe.logic.game import GameLogic


class GameUI(TextUI):
    """ Class GameUI
        @:param TextUI from base file (TextUI - courses)
    """

    def __init__(self):
        super().__init__()
        self.game = GameLogic()

    def print_title(self) -> None:
        """ Print title of game """
        self.screen.addstr(1,
                           6,
                           const.GAME_TITLE,
                           curses.A_BOLD and curses.A_UNDERLINE)

    def print_board(self) -> None:
        """ Print board of game """
        self.screen.addstr(2,
                           3,
                           const.GAME_CONTROLS)
        self.screen.addstr(const.Y_SHIFT,
                           const.X_SHIFT + 4,
                           f'{self.game.board_game[0][0]} │ {self.game.board_game[0][1]} │ {self.game.board_game[0][2]}')
        self.screen.addstr(const.Y_SHIFT + 1,
                           const.X_SHIFT + 4,
                           const.BOARD_GRID)
        self.screen.addstr(const.Y_SHIFT + 2,
                           const.X_SHIFT + 4,
                           f'{self.game.board_game[1][0]} │ {self.game.board_game[1][1]} │ {self.game.board_game[1][2]}')
        self.screen.addstr(const.Y_SHIFT + 3,
                           const.X_SHIFT + 4,
                           const.BOARD_GRID)
        self.screen.addstr(const.Y_SHIFT + 4,
                           const.X_SHIFT + 4,
                           f'{self.game.board_game[2][0]} │ {self.game.board_game[2][1]} │ {self.game.board_game[2][2]}')

    def print_players(self) -> None:
        """ Print identification of players in each move """
        self.screen.addstr(const.Y_SHIFT + 6,
                           const.X_SHIFT + 4,
                           f'Player {self.game.Cell.CH_X.__str__()}',
                           curses.A_BOLD and curses.A_UNDERLINE if not self.game.player_flag else 0)
        self.screen.addstr(const.Y_SHIFT + 7,
                           const.X_SHIFT + 4,
                           f'Player {self.game.Cell.CH_O.__str__()}',
                           curses.A_BOLD and curses.A_UNDERLINE if self.game.player_flag else 0)

    def print_result(self) -> None:
        """ Print the game result. """
        if self.game.has_victory():
            self.screen.addstr(const.Y_SHIFT + 2,
                               const.X_SHIFT + 20,
                               (
                                   f'Player {self.game.Cell.CH_O.__str__()} wins'
                                   if self.game.player_flag
                                   else f'Player {self.game.Cell.CH_X.__str__()} wins'
                               ),
                               curses.A_REVERSE)
            self.screen.addstr(const.Y_SHIFT + 3,
                               const.X_SHIFT + 17,
                               const.MSG_QUIT,
                               curses.A_BLINK)
        elif self.game.has_draw():
            self.screen.addstr(const.Y_SHIFT + 2,
                               const.X_SHIFT + 20,
                               'Nobody win',
                               curses.A_REVERSE)
            self.screen.addstr(const.Y_SHIFT + 3,
                               const.X_SHIFT + 17,
                               const.MSG_QUIT,
                               curses.A_BLINK)

    def draw(self) -> None:
        """ Draw all the TUI of game """
        curses.resize_term(20, 50)
        self.screen.border()
        self.print_title()
        self.print_board()
        x_step = 4
        y_step = 2
        if not self.game.end_game:
            self.print_players()
            self.screen.move(const.Y_SHIFT + self.game.y_pos * y_step,
                             const.X_SHIFT + self.game.x_pos * x_step + 4)
        else:
            self.print_result()
            curses.curs_set(0)

    def input(self, key) -> None:
        """ All the input options for play the game. """
        if key in const.KEY_QUIT or (key and self.game.end_game):
            self.stop()
        else:
            self.game.update_input(key)

