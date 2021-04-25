import random
class Game:
    def __init__(self,p1:str,p2:str):
        self.gameOver = True
        self.turn = ""
        self.player1 = p1
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
            self.gameOver = False
            # xo = self.xo(num)
            # print("{} Turn! {}".format(self.turn,xo))
            self.rungame()

    def rungame(self):
        if not self.gameOver:
            self.render()
            if self.turn == self.player1:
                num = 1
            elif self.turn == self.player2:
                num = 2
            xo = self.xo(num)
            print("{} Turn! ({})".format(self.turn,xo))
        nump = int(input("Select 1-9: "))
        checkresult = self.checkempty(nump)
        if checkresult:
            self.place(nump)
            self.windetect()
            if self.gameOver :
                self.stop()
            else:
                self.changeturn()
                self.rungame()
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
    def windetect(self):
        if self.turn == self.player1:
            num = 1
        if self.turn == self.player2:
            num = 2
        #check |
        for i in range(3):
            if self.board[i][0] == num and self.board[i][1] == num and self.board[i][2] == num:
                self.gameOver = True
        
        #check -
        for i in range(3):
            if self.board[0][i] == num and self.board[1][i] == num and self.board[2][i] == num:
                self.gameOver = True
        
        #check /
        if self.board[0][2] == num and self.board[1][1] == num and self.board[2][0] == num:
            self.gameOver = True

        #check \
        if self.board[0][0] == num and self.board[1][1] == num and self.board[2][2] == num:
            self.gameOver = True
    def changeturn(self):
        if self.turn == self.player1:
            self.turn = self.player2
        elif self.turn == self.player2:
            self.turn = self.player1
    def place(self,nump):
        if self.turn == self.player1:
            num = 1
        elif self.turn == self.player2:
            num = 2
        if nump >= 1 and nump <= 3:
            self.board[0][nump-1] = num
        elif nump >= 4 and nump <= 6:
            self.board[1][nump-4] = num
        elif nump >= 7 and nump <= 9:
            self.board[2][nump-7] = num
    def render(self):
        print()
        for count, i in enumerate(self.board):
            if count != 0 :
                print("-"*5)
            for c, j in enumerate(i):
                p = self.xo(j)
                if c != 0:
                    print("|{}".format(p),end='')
                else:
                    print(p,end='')
            print()
        print()
    def xo(self,j):
        if j == 0:
            p = "#"
        elif j == 1:
            p = "X"
        elif j == 2:
            p = "O"
        return p
    def stop(self):
        self.render()
        print("Congratulations {} win!".format(self.turn))


if __name__ == '__main__':
    game = Game("<Player1>","<Player2>")
    game.start()