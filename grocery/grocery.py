def main():
    grocery_list = {}

    while True:
        try:
            item = input().strip().lower()
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        except EOFError:
            print()  # Print a newline for a clean exit
            break

    for item in sorted(grocery_list):
        print(f"{grocery_list[item]} {item.upper()}")

if __name__ == "__main__":
    main()
