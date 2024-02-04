# Battleship-Algo
## Description
This python script is meant to represent which tile in a game of Battleship is best to target based on what tiles have been hit on the board.

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/8FctDuTfcO8/0.jpg)](https://www.youtube.com/watch?v=8FctDuTfcO8)

The idea for this script comes from the last strategdy the video talks about, interweaving targeting in a diagonal line with basic probability. Each tile on the board is given a number value tied to it that starts at 0 before the algorithm is run. Every time there is a possibility for a part of a ship to be on a tile 1 is added to its value. This is repeated for all the ship lengths (2,3,3,4,5), to show to the user what tile has the highest possibility of a ship being there.

Here are a few screenshots taken from the video above to help visualize what the algorithm does.

**Blank Board**

*Note: Instead of numbers here the video uses how red a square is.*

<img src = "https://i.gyazo.com/bfa7ebc0927189404cf73c4f761a39f1.png" width = "250" length = "250"> <img src = "https://i.gyazo.com/61ceb6f60984af6b33e891d744148600.png" width = "250" lenght = "250">


## Future Updates
If I ever feel the need to come back to this and change a few things these are the top priorities 
* Add a print function that shows you what squares have the highest probability.
* Add being able to hit a ship and how that would affect the board:
   * If a ship is hit, highlight its adjacent squares.
   * Unti the ship is sunken do not show the probability values for the rest of the board.
   * Once the ship is sunk, remove the highted affect and change the ship tiles to the regular "--" symbol used for the rest of the code.
* Fix line 28 in main.py so the code does not crash if you type in an invalid coordinate.


## Ending Notes
This is my first public repository on Github. This project wasn't really focused on any particular skill or aspect of programming, but more for me to refresh my python knowledge. In the future I'll be posting projects that are more focused on a certain skill, so when I look back on my account in a couple years I can see all different things I've tried out.
