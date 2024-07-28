import os
import time


def main():
    choice = ""
    while choice != "3":
        clear_screen()
        print("What would you like to do?")
        print("1 - Add an entry")
        print("2 - View entries")
        print("3 - Quit\n")
        choice = input(">>> ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            get_entries()
        elif choice == "3":
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
        with open("french.txt", "a") as f:
            sentence = f.write(input("Sentence: "))
            definition = f.write(input("Definition: "))
            list_dict[sentence] = definition
            print("Added!\n")

        choice = input("Continue? [y/n] ").lower()
        if choice == "n":
            break


def get_entries():
    clear_screen()
    f = open("french.txt", "r")
    print(f.read())

    while True:
        choice = input("Press 1 to go back\n>>> ")
        if choice == "1":
            break


if __name__ == "__main__":
    main()
