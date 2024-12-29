# 42 Piscine Rush02 - Number to Words Converter

## Description
A python solution for 42 Piscine's rush02 project. It's a program that converts numbers into their written word representation. For example, "42" becomes "forty two". The program uses a dictionary file to map numbers to their written forms, allowing for customization of the output format and language.

## Features
- Converts positive integers to their word representation
- Handles numbers up to duodecillion ($10^{39}$)
- Error handling for invalid inputs and dictionary parsing
- Clean and modular code structure

## Usage
The program can be run in two ways:

1. With a single argument (number to convert):
```bash
python3 rush02.py 42
```

2. With two arguments (custom dictionary file and number):
```bash
python3 rush02.py custom_dict.txt 42
```

### Example Outputs
```bash
$ python3 rush02.py 42
forty two

$ python3 rush02.py 100000
one hundred thousand

$ python3 rush02.py 0
zero
```

## Dictionary Format
The dictionary file should follow this format:
```
[number][0 to n spaces]:[0 to n spaces][written form]
```

Example:
```
0: zero
1: one
2: two
...
20: twenty
30: thirty
100: hundred
1000: thousand
```

## Error Handling
The program handles various error cases:
- Invalid number input: Returns "Error"
- Dictionary parsing errors: Returns "Dict Error"
- Invalid file format: Returns "Dict Error"
- Numbers out of range: Returns "Error"
