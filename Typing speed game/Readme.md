# SEBIVALLO Typing Speed Game

A simple command-line interface (CLI) typing speed test game built using Python's `curses` library. Test your typing skills and measure your speed in Words Per Minute (WPM)!

## Features

*   **WPM Calculation:** Tracks and displays your current typing speed.
*   **Error Highlighting:** Highlights incorrect characters in red.
*   **Randomized Text:** Loads random text passages from a local `text.txt` file for varied tests.
*   **Interactive Interface:** Uses the `curses` library for a terminal-based, real-time interactive experience.

## Prerequisites

To run this game, you need Python installed on your system. It is recommended to use **Python 3.x**.

Additionally, you need a plain text file named `text.txt` in the same directory as the game script (`typing_game.py`). This file should contain different text passages on separate lines.

### Example `text.txt` content:

The quick brown fox jumps over the lazy dog
Programming is the art of telling a computer what to do
Hello world this is a simple test passage for the game
Python is a widely used high-level programming language
Sebivallo is building a cool typing speed game with curses


## Installation and Usage

1.  **Clone the repository** to your local machine:
    ```bash
    git clone 
github.com

    cd Simple-Calculator
    ```

2.  **Create the `text.txt` file** in the project's root directory with some sentences to type (see Prerequisites above).

3.  **Run the game** from your terminal:
    ```bash
    python typing_game.py
     ```

4.  **Follow the on-screen instructions** to start typing and view your results.

### Controls

*   **Any key:** Press to start the game from the welcome or restart screen.
*   **`ESC` (Escape key):** Press to exit the current test or quit the application loop.
*   **`BACKSPACE`:** Deletes the previous character.

## Technologies Used

*   **Python:** The core programming language.
*   **`curses` library:** Used for creating the terminal UI and handling real-time input.

## Contributing

This project is open for contributions! If you have suggestions for improvement, such as adding features, fixing bugs, or expanding the text loading functionality, feel free to open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

*   Thanks to the Python community for the robust `curses` library documentation.
*   Inspired by simple typing test websites and CLI tools.
