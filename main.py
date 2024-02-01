"""
Future Ideas;
    * Add a print function that shows you what squares have the highest probability
    * Add being able to hit a ship and how that would affect the board: If a ship is hit add an indicator to its
      adjacent squares
    * fix line 28 in main.py so the code doesn't crash if you type in an invalid coord
"""
import util
board_format = """      
        [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10]
        [B1, B2, B3, B4, B5, B6, B7, B8, B9, B10]
        [C1, C2, C3, C4, C5, C6, C7, C8, C9, C10]
        [D1, D2, D3, D4, D5, D6, D7, D8, D9, D10]
        [E1, E2, E3, E4, E5, E6, E7, E8, E9, E10]
        [F1, F2, F3, F4, F5, F6, F7, F8, F9, F10]
        [G1, G2, G3, G4, G5, G6, G7, G8, G9, G10]
        [H1, H2, H3, H4, H5, H6, H7, H8, H9, H10]
        [I1, I2, I3, I4, I5, I6, I7, I8, I9, I10]
        [J1, J2, J3, J4, J5, J6, J7, J8, J9, J10] 
        """
print("This is a representation of your opponents board\n" + board_format +
      "\n\n""Enter the coordinate you have fired at to update the board by typing one of the examples above.\n")

playing = True

while playing:
    shot = input("Enter coordinate: ")
    if shot[0] not in util.letters and int(shot[1]) not in range(1, 11):
        print(board_format)
        shot = input("Enter one of the coordinates above: ")

    util.hit_board(shot[0], int(shot[1]))
    util.update_board()
    choice = str(input("Would you like to keep playing? (y/n)"))
    if choice is "N" or "n":
        playing = False