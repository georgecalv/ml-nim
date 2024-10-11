# George Calvert

import random
import copy
class NimPlayer:

    def __init__(self):
        pass

    def calc_heuristic(self, board):
        # else:
        #     return 16 - sum(board)
        result = 0
        for val in board:
            result = result + (result ^ val)
        return val
            


    def play(self, board):
        state = copy.deepcopy(board)
        parent_dict = {}
        parent_dict[-1] = state
        stack = []
        visited = [state]
        play = 1
        while sum(state) != 1:
            # key = h, val [state]
            min_h = {}
            indexes = self.get_sticks_index(state)
            new_state = []
            # go through pos turns
            for i in indexes:
                for x in range(state[i], -1, -1):
                    turn = copy.deepcopy(state)
                    turn[i] -= x
                    if turn not in visited:
                        stack.append(turn)
                        h = self.calc_heuristic(turn)
                        if h in min_h:
                            min_h[h].append(turn)
                        else:
                            min_h[h] = [turn]
            if len(min_h) == 0:
                new_state = stack[0]
                del stack[0]
            else:
                new_state = min_h[min(min_h)].pop()
                if min_h[min(min_h)] == None:
                    del min_h[min(min_h)]
                if new_state == state:
                    new_state = min_h[min(min_h)].pop()
                visited.append(new_state)
                parent_dict[str(state)] = new_state
            state = new_state
            if play == 0:
                play = 1
            else:
                play = 0
        try:
            return parent_dict[str(board)]
        except:
            # have to do a move
            index = self.get_sticks_index(board)
            board[index[0]] = 0
            return board


    def get_sticks_index(self, state):
        result = []
        for x in range(len(state)):
            if(state[x] > 0):
                result.append(x)
        return result

computer = NimPlayer()
player2 = NimPlayer()
board = [1, 3, 5, 7]
turn = 1
print(board)
while sum(board) != 0:
    # computer
    if turn == 1:
        board = computer.play(board)
        turn = 0
        print("After Computer turn: ", board)
    # player 2
    else:
        print(board)
        index = input("Please enter a index: ")
        num = input("Please enter the number you would like to take: ")
        board[int(index)] -= int(num)
        turn = 1
        print("After Player turn: ", board)
if turn == 1:
    print("Computer WON") 
else:
    print("Player WON")


