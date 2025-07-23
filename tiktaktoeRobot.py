import random
# X = robot, O = opponent, N = empty

class tiktaktoeRobot():
    
    boardModel = ""
    values = dict()
    learningRate = 0
    
    
    
    def __init__(self, rate):
        pass
        learningRate = rate
    
    def calculateInitialValue(self, board):
        
        #horizontal wins, check squares in the center column
        for i in range(1, 8, 3):
            print(board)
            if board[i] == board[i+1] == board[i-1]:
                if board[i] == 'X':
                    return 1
                elif board[i] == 'O':
                    return 0.0
                else:
                    continue
                
        
        #Vertical wins, check squares in the center row

        for i in range(3, 6, 1):
            if board[i] == board[i-3] == board[i+3]:
                if board[i] == "X":
                    return 1
                elif board[i] == 'O':
                    return 0
                else:
                    continue

        #Diagonal win, check diagonal
        if board[0] == board[4] == board[8]:
            if board[0] == "X":
                return 1
            if board[0] == 'O':
                return 0   
        elif board[2] == board[4] == board[6]:
            if board[2] == "X":
                return 1
            if board[2] == 'O':
                return 0
        return 0.5
                
        
    #For every board state, initialize its values to 0, 0.5, or 1. 

    def calculateInitialValues(self, board):
        if(len(board) == 9):
            value = self.calculateInitialValue(board)
            self.values[board] = value
        else:
            self.calculateInitialValues(board + "X")
            self.calculateInitialValues(board + "O")
            self.calculateInitialValues(board + "N")
            

    def pickMove(self, board, mode):
        options = dict()
        maxValue = 0
        bestMove = -1
        for i in range(9):
            if board[i] == "N":
                value = self.values[board[:i] + "X" + board[i+1:]]
                options[i] = value
                
                if value > maxValue: 
                    maxValue = value
                    bestMove = i
                
        if mode == "greedy" and bestMove != -1:
            newBoard = board[:bestMove] + "X" + board[bestMove+1:]
            self.updateValue(board, newBoard)
            return newBoard
        else:
            newBoard = random.choice(list(options.keys()))
            return newBoard
    
        
    def updateValue(self, prevBoard, currentBoard):
        self.values[prevBoard] = self.values[prevBoard] + self.learningRate * (self.values[currentBoard] - self.values[prevBoard])
        
    def printValues(self):
        self.values["test"] = 1
        print(self.values)

    def opponentPicks(self, board):
        options = []
        minValue = 0
        bestMove = 1
        for i in range(9):
            if board[i] == "N":
                options.append(i)
        value =  random.choice(options)
        newBoard = board[:value] + "O" + board[value+1:]

    #Model plays a game, returns 0 for win, 1 for lose
    def playGame(self):
        board = "NNNNNNNNN"
        firstPlayer = random.randrange(0, 1)
        if(firstPlayer == 1):
            board = self.opponentPicks(board)
        else:
            while(True):
                #Robot Wins
                if self.calculateInitialValue(board) == 1:
                    "Robot wins!"
                    return 0
                #Opponent Wins
                if self.calculateInitialValue(board) == 0:
                    "Opponent wins!"
                    return 1
                
                else:
                    board = self.pickMove(board, "greedy")
                    board = self.opponentPicks(board)
                    continue
            


steve = tiktaktoeRobot(0.1)
steve.calculateInitialValues("")
print("success")
numTrials = 1
board = "NNNNNNNNN"
value = steve.calculateInitialValue(board)
print(value)
firstLetter = board[0]
print(firstLetter)
for i in range(numTrials):
    result = steve.playGame()
    print(result)

steve.printValues()