def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return (
        is_correct_length(s) and
        starts_with_two_letters(s) and
        no_middle_numbers(s) and
        no_invalid_characters(s)
    )

def is_correct_length(s):
    return 2 <= len(s) <= 6

def starts_with_two_letters(s):
    return len(s) >= 2 and s[0:2].isalpha()

def no_middle_numbers(s):
    number_started = False
    for i, char in enumerate(s):
        if char.isdigit():
            if not number_started:
                number_started = True
                if char == '0': 
                    return False
            elif not s[i:].isdigit():
                return False
    return True

def no_invalid_characters(s):
    return all(char.isalnum() for char in s)

if __name__ == "__main__":
    main()
