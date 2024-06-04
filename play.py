#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
from tictactoe import TicTacToe

def play_against_human(q_table):
    game = TicTacToe()
    state = game.reset()
    state_idx = int("".join(str(s+1) for s in state), 3)

    print("Starting a new game. You are O, AI is X.")
    game.render()
    while not game.done:
        if game.current_player == -1:
            available_actions = np.where(game.board.flatten() == 0)[0]
            if len(available_actions) == 1:
                action = available_actions[0]
                print(f"Automatically chosen move: {action}")
            else:
                action = int(input("Your move (0-8): "))
        else:
            available_actions = np.where(game.board.flatten() == 0)[0]
            if len(available_actions) == 1:
                action = available_actions[0]
            else:
                action = np.argmax(q_table[state_idx])
                print(f"AI's move: {action}")

        next_state, reward, done = game.step(action)
        next_state_idx = int("".join(str(s+1) for s in next_state), 3)
        state_idx = next_state_idx

        game.render()
    if game.winner == 1:
        print("AI wins!")
    elif game.winner == -1:
        print("You win!")
    else:
        print("It's a draw!")