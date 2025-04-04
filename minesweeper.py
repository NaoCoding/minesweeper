# I'll do the task with a class structure since I think it will be more clear and easier to maintain
class minesweeper:

    # This is the initiaize function of the class, there are also some default numbers for parameters.
    def __init__(self , width : 10 , height : 10 , bomb_count : 10) -> None:
        self.width = width
        self.height = height
        self.bomb_count = bomb_count
        self.board = [['#' for _ in range(width)] for _ in range(height)]
        pass

# if __name__ == "__main__":
# The example are listed in example.py.