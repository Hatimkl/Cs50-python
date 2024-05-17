import random

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        X = generate_integer(level)
        Y = generate_integer(level)
        if ask_problem(X, Y):
            score += 1
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass
        print("Please enter a valid level (1, 2, or 3).")

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")

def ask_problem(X, Y):
    for _ in range(3):
        try:
            answer = int(input(f"{X} + {Y} = "))
            if answer == X + Y:
                return True
            else:
                print("EEE")
        except ValueError:
            print("EEE")
    print(f"{X} + {Y} = {X + Y}")
    return False

if __name__ == "__main__":
    main()
