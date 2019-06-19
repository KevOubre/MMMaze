# MMMaze

This is a python program written by an inexperienced program kept alive as a testament to my development as a programmer. It generates mazes using pygame. Read on if you really want to use this program.

| COMMAND | NUMBER | WHAT IT DOES |
|---------|--------|--------------|
|function | 0      | Uses either Prim's algorithm or Backtracking to draw a maze that can be solved by moving a small rectangle around to get to a randomly assigned exit point. Once you reach that point, the game shows you the path you took and how long it took. Finally, it restarts and draws a new maze for you to play in |
|function | 1      | Creates a maze only using Prim's algorithm. Cannot play on it|
|function | 2      | Creates a maze only using Backtracking. Cannot play on it |
|function | 3      | Draws the maze but making each cell a rainbow. Somehow different than function 4|
|function | 4      | Draws the maze but making each cell a rainbow. Somehow different than function 3|
|function | 5      | Makes it a race for two players to solve the maze before the other person. Also is infinite|

| COMMAND | NUMBER | WHAT IT DOES
| -------- |-------|-------------|
|fullscreen| 0   | Makes it not fullscreen |
|fullscreen| 1   | Makes it fullscreen     |

| COMMAND | NUMBER | WHAT IT DOES
| -------- |-------|-------------|
| screeny | infinite| determines the screen's y resolution |
| screnx  | infinite| determines the screen's x resolution |

| COMMAND | NUMBER | WHAT IT DOES
| -------- |-------|-------------|
|width    |>2|  determines how to divide the screen (the smaller it gets the longer it takes to run |

# Dependencies:
Pygame ( I included the .whl for easy installation. JK it's a bug turned into a feature)

# Running:
Modify the option.txt based on the table above and then run the MainLoop.py. If it causes burnin or eyepain, change the black and white levels.
