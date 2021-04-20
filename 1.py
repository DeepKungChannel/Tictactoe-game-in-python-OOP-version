import random
class Game:
    def __init__(self,p1:str,p2:str):
        self.gameOver = True
        self.turn = ""
        self.player1 = p1,
        self.player2 = p2
        self.board = [
                [0,0,0],
                [0,0,0],
                [0,0,0]
                ]
    def start(self):
        if self.gameOver :
            num = random.randint(1,2)
            if num == 1:
                self.turn = self.player1
            elif num == 2:
                self.turn = self.player2
            self.rungame()
    def rungame(self):
        nump = int(input("Select 1-9: "))
        checkresult = self.checkempty(nump)
        if checkresult:
            self.place(nump)

        else:
            print("Can't place. Please select again.")
            self.rungame()
    def checkempty(self,nump):
        if nump >= 1 and nump <= 3:
            if self.board[0][nump-1] == 0:
                return True
            else:
                return False
        elif nump >= 4 and nump <= 6:
            if self.board[1][nump-4] == 0:
                return True
            else:
                return False
        elif nump >= 7 and nump <= 9:
            if self.board[2][nump-7] == 0:
                return True
            else:
                return False
    def place(self,nump):
        if self.turn == self.player1:
            self.turn = self.player2
            num = 1
        elif self.turn == self.player2:
            self.turn = self.player1
            num = 2
        if nump >= 1 and nump <= 3:
            self.board[0][nump-1] = num
        elif nump >= 4 and num <= 6:
            self.board[1][nump-4] = num
        elif nump >= 7 and nump <= 9:
            self.board[2][nump-7] = num
    def render(self):
        for i in self.board:
            for j in i:
                if j == 0:
                    p = "#"
                elif j == 1:
                    p = "x"
                elif j == 2:
                    p = "o"
                if j != 0:
                    print("|{}".format(p))
                else:
                    print(p)


if __name__ == '__main__':
    game = Game("P1","P2")
    game.start()
