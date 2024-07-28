import os
import time


def main():
    choice = ""
    while choice != "2":
        clear_screen()
        print("What would you like to do?")
        print("1 - Add an entry")
        print("2 - Quit\n")
        choice = input(">>> ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            print("Au revoir!")
            break
        else:
            print("Oops! That is an invalid input. Try again...")
            time.sleep(2)


def clear_screen():
    os.system("clear")


def add_entry():
    list_dict = {}
    while True:
        clear_screen()
        print("======= New Entry ========")
        sentence = input("Sentence: ")
        definition = input("Definition: ")
        list_dict[sentence] = definition
        print("Added!\n")

        choice = input("Continue? [y/n] ").lower()
        if choice == "n":
            break


if __name__ == "__main__":
    main()
