def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    doll = int(d.replace("$", " "))
    return doll

def percent_to_float(p):
    per = int(p.replace("%", " "))
    per = per / 100
    return per

main()
