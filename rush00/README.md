# 42 Rush00 Python Implementation

This project is a Python implementation of the Rush 00 project from 42's C Piscine. While the original project requires implementing one of five possible pattern generators in C, this version implements all five patterns in Python.

## About the Project

The Rush 00 project asks students to create a program that generates rectangular patterns using ASCII characters. Each pattern variant (rush00 through rush04) has its own unique set of characters and rules for the corners and edges of the rectangle.

### Pattern Examples

For a 5x3 rectangle, each rush variant produces:

```
rush00:
o---o
|   |
o---o

rush01:
/***\
*   *
\***/

rush02:
ABBBA
B   B
CBBBC

rush03:
ABBBC
B   B
ABBBC

rush04:
ABBBC
B   B
CBBBA
```

## Usage

```bash
python3 rush00.py [width] [height]
```

Where:
- `width`: The width of the rectangle (must be positive integer)
- `height`: The height of the rectangle (must be positive integer)

Example:
```bash
python3 rush00.py 5 3
```

This will display all five rush patterns with the specified dimensions.

## Error Handling

The program includes error handling for:
- Incorrect number of arguments
- Non-integer arguments
- Negative or zero dimensions

When an error occurs, usage instructions are displayed.
