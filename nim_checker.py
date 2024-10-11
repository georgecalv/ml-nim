"""
Date: 10/4/2022
Author: Caleb Barker
Desc: this File will run 4 tests on students nim players in order to check that they are defining their 
class and play function correctly. This checker also does some basic testing to make sure they are following the rules.  
"""

import copy



try:
    import nim_player 
    print("Test 1: Pass")
except:
    print("Test 1: Fail (Put this file in the same directory as your \'nim_player.py\'",end="")
    print(" Or, rename your file for the assignment to \'nim_player.py\')")

try:
    p1 = nim_player.NimPlayer()
    print("Test 2: Pass")
except:
    print("Test 3: Fail (Make sure that your class is named \'NimPlayer\')")    

try:
    p1.play([1,2,3,4])
    print("Test 3: Pass ")
except :
    print("Test 3: Fail (play should be defined as \"def play(self,board)\"")




def check():
    board = [1,3,5,7]
    while sum(board) != 1:
        prev_board = copy.deepcopy(board)
        board = p1.play(board)
        changes =0
        for i,val in enumerate(board):
            if val <0:
                print("Test 4: Fail (Returning negative number of sticks in board)")
                return
            if val != prev_board[i]:
                changes +=1
            if val > prev_board[i]:
                print("Test 4: Fail (Increasing number of sticks in Board)")
                return
        if changes > 1:
            print("Test 4: Fail (Changing multiple rows)") 
            return
        if changes < 1:
            print("Test 4: Fail (No change to board state)")
            return

    print("Test 4: Pass")

try:
    check()
except :
    print("Test 4: Fail")