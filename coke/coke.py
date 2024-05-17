def main():
    cost = 50
    total_inserted = 0
    accepted_coins = [25, 10, 5]

    while total_inserted < cost:
        print(f"Amount Due: {cost - total_inserted}")
        coin = int(input("Insert Coin: "))

        if coin in accepted_coins:
            total_inserted += coin
        else:
            print("Invalid coin. Please insert 25, 10, or 5 cents.")

    change = total_inserted - cost
    print(f"Change Owed: {change}")

if __name__ == "__main__":
    main()
