import random


class TicTacToe:
    def __init__(self):
        self.table = []

    def create_table(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.table.append(row)

    @staticmethod
    def first_player():
        return random.randint(0, 1)

    def fix_point(self, row, col, player):
        self.table[row][col] = player

    def player_win(self, player):
        n = len(self.table)
        for i in range(n):
            win = True
            for j in range(n):
                if self.table[i][j] != player:
                    win = False
                    break
            if win:
                return win

        for i in range(n):
            win = True
            for j in range(n):
                if self.table[j][i] != player:
                    win = False
                    break

            if win:
                return win

        win = True
        for i in range(n):
            if self.table[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.table[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

    def table_filled(self):
        for row in self.table:
            for item in row:
                if item == '-':
                    return False
        return True

    @staticmethod
    def next_player_turn(player):
        return 'X' if player == 'O' else 'O'

    def show_table(self):
        for row in self.table:
            for item in row:
                print(item, end=' ')
            print()

    def start(self):
        self.create_table()
        player = 'X' if self.first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_table()

            row, col = list(
                map(int, input("Enter row and column numbers to fix point: ").split()))
            print()

            self.fix_point(row - 1, col - 1, player)

            if self.player_win(player):
                print(f"Player {player} wins the game!")
                break

            if self.table_filled():
                print('Match Draw!')
                break

            player = self.next_player_turn(player)

            print()

            self.show_table()


if __name__ == "__main__":
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()
