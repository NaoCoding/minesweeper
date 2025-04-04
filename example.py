from minesweeper import minesweeper

new_game = minesweeper(width=15 , height=15 , bomb_count=7)
print(new_game.select(x=0 , y=0))