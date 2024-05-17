import sys
import random
import pyfiglet

def main():
    # Check command-line arguments
    if len(sys.argv) not in [1, 3]:
        sys.exit("Usage: figlet.py or figlet.py -f <fontname>")

    # Determine if a specific font is provided
    if len(sys.argv) == 3:
        if sys.argv[1] not in ['-f', '--font']:
            sys.exit("Usage: figlet.py -f <fontname>")
        font = sys.argv[2]
        # Validate the font name
        if font not in pyfiglet.FigletFont.getFonts():
            sys.exit("Invalid font name")
    else:
        # Use a random font if no specific font is provided
        font = random.choice(pyfiglet.FigletFont.getFonts())

    # Prompt the user for input text
    user_input = input("Input: ")

    # Create a Figlet object with the specified or random font
    figlet = pyfiglet.Figlet(font=font)

    # Output the text in the desired font
    print(figlet.renderText(user_input))

if __name__ == "__main__":
    main()
