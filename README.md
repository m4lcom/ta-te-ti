# Ta-Te-Ti

**Ta-Te-Ti** is an implementation of the classic "Tic-Tac-Toe" game developed in Python.

## Description

Ta-Te-Ti is a console game where two players take turns placing their marks on a 3x3 grid, aiming to align three of their marks in a row, column, or diagonal.

## Features

- Two-player game.
- Command-line interface.
- Win and draw detection.
- Restartable game.

## Technologies and Tools

- **Python**: Programming language used to develop the game.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/m4lcom/ta-te-ti.git

    Navigate to the project directory:

    bash

    cd ta-te-ti

    No additional dependencies are required to run this project. Make sure you have Python installed on your system.

Usage

To play, run the main script:

bash

python ta_te_ti.py

Follow the on-screen instructions to play. The game will prompt you to enter coordinates to place your mark and will notify you when someone wins or if the game ends in a draw.
Code
Main Functions

    MostrarTablero(tablero): Displays the current state of the board in the console.

    SiguienteMovimiento(tablero): Allows the human player to enter their move and updates the board.

    LugaresVacios(tablero): Returns a list of empty positions on the board.

    Ganador(tablero, simbolo): Determines if the player with the given symbol (O or X) has won the game.

    MovimientoMaquina(tablero): Makes an automatic move for the machine (player X).

Game Flow

The game starts by creating a 3x3 board with numbers from 1 to 9. The machine makes its first move in the center. Turns alternate between the human player and the machine. The game ends when someone wins or the board is filled (draw).
Contributing

If you want to contribute to this project, please follow these steps:

    Fork the repository.
    Create a new branch for your changes.
    Make your modifications and commit them.
    Submit a pull request with a description of your changes.

License

This project is licensed under the MIT License. See the LICENSE file for more details.
Contact

If you have any questions, feel free to contact me:

    Email: malcom.foca@gmail.com
    GitHub: m4lcom
