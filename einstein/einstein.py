def Joules(mass):
    c = 300000000
    Joul = mass * c**2
    return Joul

def main():
    user_input = int(input("Please enter your mass in kilograms :"))
    joul_clc = Joules(user_input)
    print(joul_clc)

main()
