#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from q_learning import train_q_learning
from play import play_against_human

if __name__ == "__main__":
    # Train the Q-learning model
    q_table = train_q_learning()

    # Play against the trained AI
    play_against_human(q_table)