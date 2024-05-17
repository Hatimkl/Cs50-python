def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert_to_percentage(fraction)
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break
        except (ValueError, ZeroDivisionError):
            continue

def convert_to_percentage(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x > y or y == 0:
            raise ValueError
        percentage = (x / y) * 100
        return round(percentage)
    except (ValueError, ZeroDivisionError):
        raise

if __name__ == "__main__":
    main()
