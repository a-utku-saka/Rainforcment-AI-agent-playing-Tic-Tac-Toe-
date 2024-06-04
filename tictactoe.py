#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# tictactoe.py
import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1
        self.done = False
        self.winner = None

    def reset(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1
        self.done = False
        self.winner = None
        return self.board.flatten()

    def step(self, action):
        row, col = divmod(action, 3)
        if self.board[row, col] == 0 and not self.done:
            self.board[row, col] = self.current_player
            if self.check_winner(self.current_player):
                self.done = True
                self.winner = self.current_player
                reward = 1
            elif np.all(self.board != 0):
                self.done = True
                self.winner = 0  # Draw
                reward = 0.5
            else:
                reward = 0
                self.current_player = -self.current_player  # Switch player
        else:
            reward = -1  # Invalid move
        return self.board.flatten(), reward, self.done

    def check_winner(self, player):
        for i in range(3):
            if np.all(self.board[i, :] == player) or np.all(self.board[:, i] == player):
                return True
        if np.all(np.diag(self.board) == player) or np.all(np.diag(np.fliplr(self.board)) == player):
            return True
        return False

    def render(self):
        symbols = {1: 'X', -1: 'O', 0: '-'}
        for row in self.board:
            print(' '.join(symbols[x] for x in row))
        print()