def main():
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
    if is_valid_answer(answer):
        print("Yes")
    else:
        print("No")


def is_valid_answer(answer):
    normalized_answer = answer.strip().lower()
    if (normalized_answer == "42" or
        normalized_answer == "forty-two" or
        normalized_answer == "forty two"):
        return True
    return False


main()
