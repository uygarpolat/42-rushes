import sys

def rot_90_clock(grid):
    return list(zip(*grid[::-1]))

def rot_90_c_clock(grid):
    return list(zip(*grid))[::-1]

def print_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        if row == 1 or row == len(grid) - 1:
            for _ in range(len(grid) + 2):
                print("-", end="")
            print("")
        for col in range(cols):
            if col == 1 or col == len(grid) - 1:
                print("|", end="")
            if grid[row][col] == 0:
                print(" ", end="")
            else:
                print(grid[row][col], end="")
        print("")

def is_row_valid(row):
    sublist = row[1:-1]
    sublist_without_zero = [x for x in sublist if x != 0]
    if len(sublist_without_zero) != len(set(sublist_without_zero)):
        return False
    return True

def traverse_grid(grid, row, col):
    if row > len(grid) - 2:
        return True

    for i in range(1, len(grid) - 1, 1):
        grid[row][col] = i
        grid2 = rot_90_clock(grid)
        grid3 = rot_90_c_clock(grid)

        if not is_row_valid(grid[row]) or not is_row_valid(grid2[col]):
            grid[row][col] = 0
            continue
        if (
            not get_visibility(grid[row][1:-1]) <= grid[row][0] or
            not get_visibility(grid3[len(grid3) - col - 1][1:-1]) <= grid3[len(grid3) - col - 1][0]):
            grid[row][col] = 0
            continue
        if not is_current_overall_visibility_correct(grid, row, col):
            grid[row][col] = 0
            continue
        else:
            left, right = get_next_location(grid, row, col)
            if not traverse_grid(grid, left, right):
                grid[row][col] = 0
                continue
            else:
                return True
    return False

def get_next_location(grid, row, col):
    length = len(grid)
    if col == length - 2:
        left, right = row + 1, 1
    else:
        left, right = row, col + 1
    return left, right

def is_current_overall_visibility_correct(grid, row, col):
    if col == len(grid) - 2:
        if not is_left_right_vis_correct(grid, row):
            return False
    if row != len(grid) - 2:
        return True
    grid2 = rot_90_clock(grid)
    if not is_left_right_vis_correct(grid2, col):
        return False
    return True

def is_left_right_vis_correct(grid, row):
    sublist_left_to_right = grid[row][1:-1]
    sublist_right_to_left = sublist_left_to_right[::-1]
    first = grid[row][0]
    last = grid[row][len(grid[row]) - 1]
    vis_left = get_visibility(sublist_left_to_right)
    vis_right = get_visibility(sublist_right_to_left)
    if vis_left != first or vis_right != last:
        return False
    return True

def create_grid(input):
    chunk_len = len(input) // 4

    colup_coldown = input[:(len(input) // 2)]
    rowleft_rowright = input[(len(input) // 2):]
    colup_coldown.insert(0,0)
    colup_coldown.append(0)

    colup = colup_coldown[:(len(colup_coldown) // 2)]
    coldown = colup_coldown[(len(colup_coldown) // 2):]
    colup.append(0)
    coldown.insert(0,0)

    temp = [0 for _ in range(chunk_len)]
    rows = [[] for _ in range(chunk_len)]
    for i in range(len(rows)):
        rows[i] = []
        rows[i].append(rowleft_rowright[i])
        rows[i].extend(temp)
        rows[i].append(rowleft_rowright[i+chunk_len])
    rows.insert(0,colup)
    rows.append(coldown)
    return rows

def get_visibility(order):
    max_height = 0
    count = 0
    for height in order:
        if height > max_height:
            max_height = height
            count += 1
    return count

def validate_input(argv):
    input_4x4 = "4 3 2 1 1 2 2 2 4 3 2 1 1 2 2 2"
    input_5x5 = "2 2 1 3 2 2 1 4 2 3 3 5 1 2 2 2 1 4 2 3"
    input_6x6 = "2 2 3 4 1 2 2 2 2 1 3 4 3 4 1 2 2 2 2 1 2 3 3 3"
    input_7x7 = "7 1 4 2 4 3 2 1 2 2 2 2 2 4 2 5 4 3 3 2 1 4 1 2 2 2 2 5"

    if len(argv) > 2:
        raise ValueError(f"Too many arguments.")
    elif len(argv) == 2:
        if argv[1] == "4x4":
            input = [int(arg) for arg in input_4x4.split()]
        elif argv[1] == "5x5":
            input = [int(arg) for arg in input_5x5.split()]
        elif argv[1] == "6x6":
            input = [int(arg) for arg in input_6x6.split()]
        elif argv[1] == "7x7":
            input = [int(arg) for arg in input_7x7.split()]
        else:
            input = [int(arg) for arg in argv[1].split()]
    else:
        input = [int(arg) for arg in input_4x4.split()]

    member_count = len(input)
    
    if member_count % 4 != 0:
        raise ValueError("Input size must be a multiple of 4.")
    
    if any(num < 0 for num in input):
        raise ValueError("Input contains negative numbers.")
    
    max_value = member_count // 4
    if any(num > max_value for num in input):
        raise ValueError(f"Numbers must not exceed {max_value} (member_count / 4).")
    return input

def main():
    try:
        input = validate_input(sys.argv)
        grid = create_grid(input)
        if traverse_grid(grid, 1, 1):
            print_grid(grid)
        else:
            print("Solution cannot be found.")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()