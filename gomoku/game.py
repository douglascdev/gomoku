class Gomoku:
    BLANK = ' '

    def __init__(self, order: int = 15):
        self.order = order
        self.table = [[self.BLANK] * order for _ in range(order)]
        self.current_player_symbol = "O"

    def play(self, position: tuple):
        x, y = position
        if not (0 <= x <= self.order and 0 <= y <= self.order):
            raise ValueError(f"Position {position} is out of bounds for order {self.order}")
        if self.table[x][y] != self.BLANK:
            raise ValueError(f"Position {position} is not blank!")
        self.table[x][y] = self.current_player_symbol
        self.current_player_symbol = "O" if self.current_player_symbol == "X" else "X"

    def get_formatted_table(self):
        return "\n".join(f"|{'|'.join(line)}|" for line in self.table)

    def check_for_victory(self, last_move_position: tuple):
        x, y = last_move_position

        # horizontal_victory = "".join([self.current_player_symbol] * 5)
        # if y - 5 >= 0 and self.table[x][y - 5:y] == horizontal_victory and y - 6 >= 0 or self.table[x][y - 6] != self.current_player_symbol:
        #     return True
        # if y + 5 < self.order and self.table[x][y:y + 5] == horizontal_victory and y + 6 < self.order or self.table[x][y + 6] != self.current_player_symbol:
        #     return True

        # vertical_victory = []
        # elif y + 5 < self.order and self.table[x][y:y + 5] == horizontal_victory and y + 6 < self.order or self.table[x][y + 6] != self.current_player_symbol:


if __name__ == '__main__':
    game = Gomoku()
    game.play((1, 1))
    game.play((1, 2))
    print(game.get_formatted_table())
