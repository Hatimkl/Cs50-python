def main():
    time_str = input("Enter the time (in 24-hour format HH:MM): ")
    time = convert(time_str)
    check_meal_time(time)

def convert(time):
    hours, minutes = map(int, time.split(":"))
    total_hours = hours + (minutes / 60)
    return total_hours

def check_meal_time(time):
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

if __name__ == "__main__":
    main()
