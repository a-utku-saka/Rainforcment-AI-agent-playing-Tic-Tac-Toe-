#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:38:23 2024

@author: utku
"""

# q_learning.py
import numpy as np
from tictactoe import TicTacToe

def train_q_learning(episodes=1000000):
    q_table = np.zeros((3**9, 9))
    alpha = 0.1  # Learning rate
    gamma = 0.9  # Discount factor
    epsilon = 0.3  # Initial exploration rate
    epsilon_decay = 0.0001  # Epsilon decay rate per step

    for episode in range(episodes):
        game = TicTacToe()
        state = game.reset()
        state_idx = int("".join(str(s+1) for s in state), 3)
        print(episode)
        while not game.done:
            if np.random.rand() < epsilon:
                action = np.random.choice(np.where(game.board.flatten() == 0)[0])
            else:
                action_values = q_table[state_idx]
                action = np.argmax(action_values)

            next_state, reward, done = game.step(action)
            next_state_idx = int("".join(str(s+1) for s in next_state), 3)

            q_table[state_idx, action] = q_table[state_idx, action] + \
                alpha * (reward + gamma * np.max(q_table[next_state_idx]) - q_table[state_idx, action])

            state_idx = next_state_idx

            # Update epsilon
            epsilon = max(0.1, epsilon - epsilon_decay)

    # Save the Q-table for future use
    np.save('q_table.npy', q_table)
    return q_table