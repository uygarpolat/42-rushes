import sys

def parse_file(filepath):
    try: 
        dict = {}
        with open(filepath, 'r') as file:
            for line in file:
                if not line.strip():
                    continue
                left, right = line.strip().split(':')
                dict[int(left.strip())] = right.strip()
        return dict
    except:
        raise ValueError

def display_number(dict, num, result):
    try: 
        if num >= 1000:
            num1 = num
            count = 0
            while num1 >= 1000:
                num1 = num1 // 1000
                count += 1
            amount = 10 ** (count * 3)

            result = display_number(dict, num1, result)
            result += " " + dict[amount]
            if num % amount != 0:
                result = display_number(dict, num % amount, result)
        elif num >= 100:
            result += " " + dict[num // 100]
            result += " " + dict[100]
            if num % 100 != 0:
                result = display_number(dict, num % 100, result)
        elif num >= 20:
            result += " " + dict[num // 10 * 10]
            if num % 10 != 0:
                result = display_number(dict, num % 10, result)
        elif num > 0:
            result += " " + dict[num]
        else:
            result += " " + dict[num]
        return result
    
    except ValueError:
        raise ValueError("Error")
    except (TypeError, KeyError):
        raise TypeError("Dict Error")

def validate_number(argv, filepath):
    if len(argv) < 2 or len(argv) > 3:
        raise ValueError("Error")
    elif len(argv) == 3:
        filepath = argv[1]
        num = argv[2]
    else:
        num = argv[1]

    try:
        num = int(num)
        dict = parse_file(filepath)
    except ValueError as e:
        if 'invalid literal for int()' in str(e):
            raise ValueError("Error")
        else:
            raise ValueError("Dict Error")

    if num < 0:
        raise ValueError("Error")
    return num, dict
    
def main():
    filepath = "dict_en.txt"
    try: 
        num, dict = validate_number(sys.argv, filepath)
        result = ""
        result = display_number(dict, num, result)[1:]
        print(result)
    except (ValueError, TypeError) as e:
        print(e)

if __name__ == "__main__":
    main()