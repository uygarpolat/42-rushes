# Skyscraper Puzzle Solver

A Python solution to 42 Piscine's rush01 project, also known as the [skyscraper problem](https://www.brainbashers.com/skyscrapers.asp). While the original project specification requires solving 4x4 grids, this implementation provides a general solution to handle larger grid sizes.

## The Puzzle

- Each row and column must contain one of each number from 1 to N (where N is the grid size)
- The numbers around the grid indicate how many skyscrapers are visible from that direction
- A skyscraper blocks the view of all shorter skyscrapers behind it

## Usage

```
python3 rush01.py [input]
```

### Input Format Options

1. **No Arguments**: 
   - Defaults to solving the example 4x4 grid provided in the subject PDF of the project
   ```
   python3 rush01.py
   ```

2. **Predefined Grid Sizes**:
   - Available options: "4x4", "5x5", "6x6", "7x7"
   ```
   python3 rush01.py 4x4
   python3 rush01.py 5x5
   python3 rush01.py 6x6
   python3 rush01.py 7x7
   ```

3. **Custom Input**:
   - For a 4x4 grid, provide 16 numbers representing the constraints in this order:
   ```
   python3 rush01.py "col1up col2up col3up col4up col1down col2down col3down col4down row1left row2left row3left row4left row1right row2right row3right row4right"
   ```
   - Example:
   ```
   python3 rush01.py "4 3 2 1 1 2 2 2 4 3 2 1 1 2 2 2"
   ```

### Error Handling

The program will display appropriate error messages if:
- More than one command-line argument is provided
- Input numbers are invalid (negative or exceed grid size)
- Input size is not appropriate for the grid
- Input format is incorrect

## Output

The program will either:
- Display the solved grid if a solution is found
- Print "Solution cannot be found" if no valid solution exists

## Note

This implementation uses a recursive backtracking algorithm to find the solution. For grid sizes larger than 6x6, the computation time may increase significantly due to the increased complexity of the puzzle.