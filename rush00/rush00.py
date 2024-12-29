import sys

class Rush:
    def __init__ (
        self, topleft,
        topright,
        bottomleft,
        bottomright,
        edge_hor,
        edge_ver):

        self.topleft = topleft
        self.topright = topright
        self.bottomleft = bottomleft
        self.bottomright = bottomright
        self.edge_hor = edge_hor
        self.edge_ver = edge_ver

def print_rushes(rush, x, y):
    for i in range(len(rush)):
        print(f"rush0{i} ({x},{y}):")
        for row in range(y):
            for col in range(x):
                loc = (row,col)
                if loc == (0,0):
                    print(rush[i].topleft, end= "")
                elif loc == (0, x - 1):
                    print(rush[i].topright, end= "")
                elif loc == (y - 1, 0):
                    print(rush[i].bottomleft, end= "")
                elif loc == (y - 1, x - 1):
                    print(rush[i].bottomright, end= "")
                elif row == 0 or row == y - 1:
                    print(rush[i].edge_hor, end= "")
                elif col == 0 or col == x - 1:
                    print(rush[i].edge_ver, end= "")
                else:
                    print(" ", end="")
            print("")
        print("--------------")

def main():
    try:
        if len(sys.argv) != 3:
            raise ValueError
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        if x < 1 or y < 1:
            raise ValueError
        rush = [
            Rush('o', 'o', 'o', 'o', '-', '|'),
            Rush('/', '\\', '\\', '/', '*', '*'),
            Rush('A', 'A', 'C', 'C', 'B', 'B'),
            Rush('A', 'C', 'A', 'C', 'B', 'B'),
            Rush('A', 'C', 'C', 'A', 'B', 'B'),
        ]
        print_rushes(rush, x, y)
        
    except ValueError:
        print("Usage: rush00.py [width] [height]")

if __name__ == "__main__":
    main()