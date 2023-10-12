####################################################################
#   Aaren Patel
#   I pledge my honor that I have abided by the Stevens Honor System
#   12/10/22
#   Cs 115 - HW 13
####################################################################

class Board(object):
    """A class for a Connect 4 Board object"""

    # The constructor is always named __init__.
    def __init__(self, width = 7, height = 6):
        """The constructor for objects of type Board."""
        self.width = width
        self.height = height
        self.board = []
        col = []
        for i in range(self.height):
            for j in range(self.width):
                col += [" "]
            self.board += [col]
            col = []

    def __str__(self):
        """This method returns a string representation for the object of type Board that calls it (named self)."""
        string = ""
        for i in range(self.height):
            for j in range(self.width):
                string += "|" + self.board[i][j]
            string += "|\n"
        string + "_" * (2 * self.width - 1)
        for i in range(self.width):
            string += " " + str(i)
        return string

    def allowsMove(self, col):
        """Returns a boolean on whether or not the input col can hold another token"""
        if col >= self.width or col < 0:
            return False
        return self.board[0][col] == " "

    def addMove(self, col, ox):
        """Adds a move to the board in the given col with the value of what is in ox"""
        for i in range(self.height - 1, -1, -1):
            if self.board[i][col] == " ":
                self.board[i][col] = ox
                break

    def setBoard(self, moves):
        """Sets the board in the turn order of moves"""
        char = "X"
        for i in moves:
            if self.allowsMove(int(i)):
                self.addMove(int(i), char)
                if char == "X":
                    char = "O"
                else:
                    char = "X"

    def delMove(self, col):
        """Deletes the topmost move in a column given"""
        for i in range(self.height):
            if self.board[i][col] != " ":
                self.board[i][col] = " "
                break

    def winsFor(self, ox):
        """Determnes if the given symbol in ox has won the game"""
        count = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == ox:
                    count += 1
                else:
                    count = 0
                if count > 3:
                    return True
            count = 0
        count = 0
        for j in range(self.width):
            for i in range(self.height):
                if self.board[i][j] == ox:
                    count += 1
                else:
                    count = 0
                if count > 3:
                    return True
        count = 0
        for i in range(self.height):
            for j in range(self.width):
                i1 = i
                j1 = j
                while 0 <= i1 < self.height and 0 <= j1 < self.width:
                    if self.board[i1][j1] == ox:
                        count += 1
                    else:
                        count = 0
                    if count > 3:
                        return True
                    i1 += 1
                    j1 += 1
                count = 0
                i1 = i
                j1 = j
                while 0 <= i1 < self.height and 0 <= j1 < self.height:
                    if self.board[i1][j1] == ox:
                        count += 1
                    else:
                        count = 0
                    if count > 3:
                        return True
                    i1 += 1
                    j1 -= 1
                count = 0
        return False

    def hostGame(self):
        """Hosts a game of Connect 4"""
        char = "X"
        while True:
            print(self)
            choice = input("\n" + char + "'s Turn:  ")
            while not self.allowsMove(int(choice)):
                choice = input("Invalid Choice - Try Again:  ")
            self.addMove(int(choice), char)
            if self.winsFor(char):
                print(self)
                print("Congrats, " + char + " wins")
                break
            if char == "X":
                char = "O"
            else:
                char = "X"

