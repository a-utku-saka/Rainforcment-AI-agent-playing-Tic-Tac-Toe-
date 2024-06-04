# Rainforcment-AI-agent-playing-Tic-Tac-Toe

This project is an implementation of a Tic-Tac-Toe game where an AI learns to play using the Q-learning algorithm. The project is divided into three main Python files: `tictactoe.py`, `q_learning.py`, and `play.py`. You can run the entire code by executing the `main.py` file.

## File Structure:

- `tictactoe.py`: Contains the `TicTacToe` class which defines the game logic and mechanics.
- `q_learning.py`: Implements the Q-learning algorithm to train the AI model.
- `play.py`: Provides functionality to play against the trained AI model.
- `main.py`: The main file to run the training and play against the AI.

## Installation:

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/tictactoe-qlearning.git
   cd tictactoe-qlearning
2. **Install the required dependencies:**

Ensure you have numpy installed. 
If not, you can install it using pip:

  ```sh
  pip install numpy
  ```
## Usage:
**Training the Q-learning Model**
To train the Q-learning model, simply run:

 ```sh
python main.py
```
This will train the model for 1,000,000 episodes and save the Q-table to a file named `q_table.npy`.

**Playing Against the Trained AI**

After training, you can play against the AI by running the same `main.py` file. The AI will use the trained Q-table to make its moves.

**Customizing Training Parameters**
If you want to customize the training parameters, you can modify the t`rain_q_learning` function in the `q_learning.py` file. Parameters such as `alpha` (learning rate), `gamma` (discount factor), `epsilon` (exploration rate), and `episodes` can be adjusted to suit your needs.

## Reinforcement learning algorithm structure:
Q-Learning algorithm is used in this project. The alpha value is kept low to ensure the most stable learning. The gamma value was kept high because every move in the Tic-Tac-Toe game has a direct effect on the result. This way the agent cares more about future rewards. The algorithm is modified using the greedy/epsilon structure. The Epsilon structure is reduced on an episode-by-episode basis to keep the agent's exploration tendency high at first, and then the agent is allowed to use the strategies it has learned.

## Lisance 
This project is licensed under the MIT License.






