def main():
    text = input("Input: ")
    no_vowels_text = remove_vowels(text)
    print(f"Output: {no_vowels_text}")

def remove_vowels(text):
    vowels = "AEIOUaeiou"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result

if __name__ == "__main__":
    main()
